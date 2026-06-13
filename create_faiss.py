# Import JSON library to read transcript data
import json

# Import FAISS library for storing and searching vectors
import faiss

# Import numpy for handling embeddings as arrays
import numpy as np

# Import SentenceTransformer model for converting text into vectors
from sentence_transformers import SentenceTransformer




# STEP 1: Load transcript JSON file


print("Loading JSON...")

# Opening the JSON file created after Whisper transcription
with open("transcripts/test.json", "r", encoding="utf-8") as file:

    # Loading all video segments
    # Each segment contains start time, end time and text
    segments = json.load(file)




# STEP 2: Extract only text data


texts = []

# Taking only the transcript text because
# embeddings are created from text, not timestamps
for segment in segments:

    texts.append(
        segment["text"]
    )




# STEP 3: Load embedding model


print("Loading model...")

# This model converts sentences into numerical vectors
# Output vector size = 384 dimensions
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)




# STEP 4: Create embeddings


print("Creating embeddings...")


# Convert every text chunk into vector representation
embeddings = model.encode(
    texts
)


# FAISS works with float32 format,
# so converting embeddings into numpy float32 array
embeddings = np.array(
    embeddings
).astype(
    "float32"
)




# STEP 5: Create FAISS database


print("Creating FAISS index...")


# Get vector size
# Example: 384 dimensions
dimension = embeddings.shape[1]


# Create FAISS index
# IndexFlatL2 uses Euclidean distance
# to find similar vectors
index = faiss.IndexFlatL2(
    dimension
)



# Store all transcript vectors inside FAISS
index.add(
    embeddings
)



# Display total vectors stored
print(
    "Vectors stored:",
    index.ntotal
)



# STEP 6: Save FAISS index



# Saving vector database
# We can use this later without creating embeddings again
faiss.write_index(
    index,
    "video_index.faiss"
)




# STEP 7: Save metadata



# FAISS only stores vectors,
# so timestamps and original text are saved separately

with open(
    "metadata.json",
    "w",
    encoding="utf-8"

) as file:


    json.dump(
        segments,
        file,
        indent=4
    )



print("FAISS index saved")

print("Metadata saved")