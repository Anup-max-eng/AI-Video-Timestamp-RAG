# RAG question answering file

import faiss
import json
import numpy as np
import streamlit as st

from sentence_transformers import SentenceTransformer





def format_time(seconds):

    minutes = int(seconds // 60)

    seconds = int(seconds % 60)

    return f"{minutes}:{seconds:02d}"









# Load embedding model only once

@st.cache_resource
def load_embedding_model():


    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


    return model









# Load FAISS only once

@st.cache_resource
def load_faiss_index():


    index = faiss.read_index(
        "video_index.faiss"
    )


    return index









# Load metadata only once

@st.cache_data
def load_metadata():


    with open(
        "metadata.json",
        "r",
        encoding="utf-8"
    ) as file:


        metadata = json.load(
            file
        )


    return metadata












def ask_question(question):


    embedding_model = load_embedding_model()


    index = load_faiss_index()


    metadata = load_metadata()







    # Convert question to vector

    question_vector = embedding_model.encode(
        [question]
    )


    question_vector = np.array(
        question_vector
    ).astype(
        "float32"
    )







    # FAISS similarity search

    distance, indexes = index.search(
        question_vector,
        5
    )







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