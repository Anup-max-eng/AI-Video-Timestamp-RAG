# RAG question answering file


def format_time(seconds):

    minutes = int(seconds // 60)

    seconds = int(seconds % 60)

    return f"{minutes}:{seconds:02d}"






def ask_question(question):


    import faiss
    import json
    import numpy as np

    from sentence_transformers import SentenceTransformer







    # Load embedding model

    embedding_model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )








    # Load FAISS database

    index = faiss.read_index(
        "video_index.faiss"
    )








    # Load timestamp metadata

    with open(
        "metadata.json",
        "r",
        encoding="utf-8"
    ) as file:


        metadata = json.load(
            file
        )









    # Convert question into vector

    question_vector = embedding_model.encode(
        [question]
    )


    question_vector = np.array(
        question_vector
    ).astype(
        "float32"
    )









    # Search FAISS

    distance, indexes = index.search(
        question_vector,
        5
    )









    # Prepare answer

    answer = ""

    timestamps = []




    for i in indexes[0]:


        data = metadata[i]


        answer += (
            data["text"]
            +
            "\n\n"
        )




        timestamps.append(
            (

                format_time(
                    data["start"]
                ),


                format_time(
                    data["end"]
                )

            )
        )








    return (
        answer,
        timestamps
    )