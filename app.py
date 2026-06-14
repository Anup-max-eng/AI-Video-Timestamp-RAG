import os


os.environ[
    "TOKENIZERS_PARALLELISM"
] = "false"



import streamlit as st


from transcribe import process_video
from embedding import create_embeddings





# Page setup

st.set_page_config(
    page_title="Video Time Stamp Provider",
    layout="wide"
)





# CSS styling

st.markdown(
"""
<style>

.block-container {
    padding-top: 2rem;
}

h1 {
    font-size: 42px;
    font-weight: 700;
}

.subtitle {
    color: #9ca3af;
    font-size:17px;
}

[data-testid="stSidebar"] {
    background-color:#111827;
}

.stButton button {
    border-radius:8px;
}

</style>
""",
unsafe_allow_html=True
)








# Session variables

if "processed" not in st.session_state:


    st.session_state.processed = os.path.exists(
        "video_index.faiss"
    )



if "messages" not in st.session_state:


    st.session_state.messages = []



if "timestamps" not in st.session_state:


    st.session_state.timestamps = []



if "video_time" not in st.session_state:


    st.session_state.video_time = 0







# Header

st.markdown(
"""
<h1>Video TimeStamp Provider</h1>

<p class="subtitle">
Search inside videos using natural language
</p>
""",
unsafe_allow_html=True
)









# Sidebar

with st.sidebar:


    st.header(
        "Workspace"
    )



    video = st.file_uploader(
        "Upload video",
        type=["mp4"]
    )





    if video is not None:


        with open(
            "uploaded_video.mp4",
            "wb"
        ) as file:


            file.write(
                video.getbuffer()
            )



        st.success(
            "Video uploaded"
        )








        if st.button(
            "Process video"
        ):


            with st.spinner(
                "Processing video..."
            ):


                process_video(
                    "uploaded_video.mp4"
                )



                create_embeddings()



                st.session_state.processed = True




            st.success(
                "Ready"
            )








    if st.button(
        "Clear chat"
    ):


        st.session_state.messages = []

        st.session_state.timestamps = []

        st.rerun()









# Layout

left, right = st.columns(
    [1.1,1]
)









# Video

with left:


    st.subheader(
        "Video"
    )


    if os.path.exists(
        "uploaded_video.mp4"
    ):


        st.video(
            "uploaded_video.mp4",
            start_time=st.session_state.video_time
        )


    else:


        st.info(
            "Upload a video to begin"
        )









# Chat

with right:


    st.subheader(
        "Ask questions"
    )





    for role, message in st.session_state.messages:


        with st.chat_message(
            role
        ):


            st.write(
                message
            )








    if st.session_state.processed:


        question = st.chat_input(
            "Ask about this video"
        )




        if question:


            st.session_state.messages.append(
                (
                    "user",
                    question
                )
            )





            with st.spinner(
                "Searching..."
            ):


                from rag import ask_question


                answer, timestamps = ask_question(
                    question
                )





            st.session_state.messages.append(
                (
                    "assistant",
                    answer
                )
            )



            st.session_state.timestamps = timestamps



            st.rerun()







    else:


        st.info(
            "Process video before asking questions"
        )










# Timestamp references

if len(
    st.session_state.timestamps
) > 0:



    with st.expander(
        "Referenced moments"
    ):



        for start, end in st.session_state.timestamps:



            minutes, seconds = start.split(
                ":"
            )



            jump_time = (
                int(minutes) * 60
                +
                int(seconds)
            )




            if st.button(
                start + " - " + end
            ):


                st.session_state.video_time = jump_time


                st.rerun()