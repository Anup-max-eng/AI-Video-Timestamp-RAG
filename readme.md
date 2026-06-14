# AI Video Timestamp Provider using RAG

An AI-powered application that allows users to upload a video and ask questions about its content.  
The system analyzes the video, understands the spoken content, and returns the most relevant video sections with accurate timestamps using Retrieval Augmented Generation (RAG).

---

## Overview

Searching information inside long videos manually is time-consuming.  
This project solves that problem by converting video content into searchable knowledge.

The system extracts speech from a video, converts it into timestamped text, creates semantic embeddings, stores them inside a FAISS vector database, and retrieves relevant moments based on user queries.

---

## Features

- Upload video through web interface
- Automatic speech-to-text conversion
- Timestamp generation for video segments
- Semantic search inside video content
- Question answering from video data
- Returns relevant video timestamps
- Jump to specific video moments
- Interactive Streamlit UI

---

## Tech Stack

### Programming Language
- Python

### AI / Machine Learning
- OpenAI Whisper
- Sentence Transformers
- Hugging Face Transformers

### Vector Database
- FAISS (Facebook AI Similarity Search)

### Frontend
- Streamlit

### Libraries
- PyTorch
- NumPy
- JSON
- FFmpeg

---

## System Architecture


Video Upload
        |
        v
FFmpeg Processing
        |
        v
Whisper Speech Recognition
        |
        v
Timestamp Transcript Generation
        |
        v
Sentence Transformer Embeddings
        |
        v
FAISS Vector Database
        |
        v
Semantic Similarity Search
        |
        v
Relevant Answer + Timestamp


---

## How It Works

### 1. Video Processing

The uploaded video is processed and audio information is extracted.

Whisper model converts speech into text while preserving timestamps.

Output example:

```json
{
    "start": 10.5,
    "end": 18.2,
    "text": "Explanation of networking concepts"
}
2. Embedding Generation

Each transcript segment is converted into numerical vector representation using:

SentenceTransformer - all-MiniLM-L6-v2

These embeddings capture the semantic meaning of the text.

3. Vector Storage

Generated embeddings are stored inside FAISS.

FAISS enables fast similarity search among thousands of text chunks.

Generated files:

video_index.faiss
metadata.json
4. Question Answering

User question is converted into an embedding.

FAISS performs similarity search and finds the closest matching video segments.

The application returns:

Relevant content
Starting timestamp
Ending timestamp
Project Structure
Video-Timestamp-RAG/

│
├── app.py                 # Streamlit application
│
├── transcribe.py          # Whisper transcription
│
├── embedding.py           # Embedding creation + FAISS storage
│
├── rag.py                 # Question answering pipeline
│
├── search.py              # FAISS testing
│
├── metadata.json          # Timestamp metadata
│
├── video_index.faiss      # Vector database
│
├── requirements.txt       # Dependencies
│
└── README.md
Installation

Clone the repository:

git clone <repository-url>

Install dependencies:

pip install -r requirements.txt

Install FFmpeg and add it to system PATH.

Run Application

Start Streamlit:

streamlit run app.py

Open browser:

http://localhost:8501
Example Usage

Upload a video.

Ask:

What is TCP?

Output:

TCP creates a reliable connection between devices.

Timestamp:
04:30 - 04:48

Click the timestamp to navigate to that video section.

#Applications
Online learning platforms
Lecture video search
Meeting recordings
Tutorials
Research videos
Content analysis


#Future Improvements
Support multiple videos
Add advanced LLM answer generation
Cloud deployment
User authentication
Database storage