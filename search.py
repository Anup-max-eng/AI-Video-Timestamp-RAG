# Import FAISS for loading and searching vector database
import faiss

# Import JSON to read saved timestamp metadata
import json

# Import numpy for vector format conversion
import numpy as np


# Import embedding model
from sentence_transformers import SentenceTransformer

# Function to convert seconds into minute:second format

def format_time(seconds):

    minutes = int(seconds // 60)

    seconds = int(seconds % 60)

    return f"{minutes}:{seconds:02d}"



# STEP 1: Load saved FAISS vector database

print("Loading FAISS index...")

index = faiss.read_index(
    "video_index.faiss"
)



# STEP 2: Load metadata file

print("Loading metadata...")

with open(
    "metadata.json",
    "r",
    encoding="utf-8"

) as file:

    metadata = json.load(file)



# STEP 3: Load same embedding model

print("Loading embedding model...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)



# STEP 4: Take user question

query = input(
    "Ask question from video: "
)



# STEP 5: Convert question into vector

query_embedding = model.encode(
    [query]
)


# FAISS requires float32 format
query_embedding = np.array(
    query_embedding
).astype(
    "float32"
)



# STEP 6: Search similar vectors in FAISS

# k means how many similar results we want
k = 3


distances, indexes = index.search(
    query_embedding,
    k
)



# STEP 7: Display matching video parts

print("\nBest matching video sections:\n")


for i in indexes[0]:


    result = metadata[i]


    print(
    "Time:",
    format_time(result["start"]),
    "→",
    format_time(result["end"])
    )


    print(
        "Text:",
        result["text"]
    )


    print(
        "-" * 50
    )