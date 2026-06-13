# AI Video Timestamp Detection using RAG

## System Requirements

### Operating System
- Windows 10/11
- Linux (Ubuntu recommended)
- macOS supported (CPU mode)

### Python Version
- Python 3.10 - 3.11 recommended

### Hardware Requirements

Minimum:
- CPU: Quad Core Processor
- RAM: 8 GB
- Storage: 5 GB free space
- GPU: Optional

Recommended:
- CPU: AMD Ryzen 5 / Intel i5 or higher
- RAM: 16 GB
- GPU: NVIDIA GPU with CUDA support
- VRAM: 4GB+ recommended

Tested System:
- Processor: AMD Ryzen 5 7235HS
- GPU: NVIDIA GeForce RTX 3050 Laptop GPU (6GB VRAM)
- Python: 3.11.5
- CUDA Supported

---

## Required External Tools

### FFmpeg

Used for:
- video processing
- audio extraction

FFmpeg must be installed and added to system PATH.

---

## Project Pipeline

Video Input
        |
        v
FFmpeg / MoviePy
        |
        v
Audio Extraction
        |
        v
OpenAI Whisper
        |
        v
Speech-to-Text + Timestamp Generation
        |
        v
Sentence Transformer Embeddings
        |
        v
FAISS Vector Database
        |
        v
Semantic Search
        |
        v
Return Relevant Video Timestamp