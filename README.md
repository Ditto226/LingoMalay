# LingoMalay 🎙️

LingoMalay is a specialized mobile application developed using Flutter designed to record, upload, and transcribe Malay speech, with a specific focus on regional dialects such as **Kedah** and **Kelantan**. 

Built for research purposes, this project explores dialect-sensitive Automatic Speech Recognition (ASR) by leveraging fine-tuned Whisper models and integrating with Mesolitica's cutting-edge APIs. The backend architecture relies on Firebase for secure user authentication, structured data storage, and real-time state management.

---

## 🚀 Features

- **Dialect-Specific Transcription:** Tailored handling of Kedah and Kelantan speech variations.
- **Real-Time Inference:** High-accuracy Malay audio-to-text processing powered by fine-tuned OpenAI Whisper models and Mesolitica APIs.
- **Audio Management:** Native-level audio recording, playback, and local file handling within a Flutter interface.
- **Robust Cloud Infrastructure:** Fully integrated with Firebase Auth for user management and Firebase Storage/Firestore for audio assets and transcription metadata.

---

## 📁 Repository Structure

Based on the project's architecture, the repository is organized into the following key modules:

```text
├── API/                        # Core backend API services and endpoints
│   ├── Kedah/                  # Server deployment configurations sent to Google Cloud (GDC) for Kedah dialect
│   └── Kelantan/               # Server deployment configurations sent to Google Cloud (GDC) for Kelantan dialect
├── Model/        
│   ├── Kedah/                  # Fine-tuned Whisper model checkpoints and specialized audio datasets
│   └── Kelantan/               # Fine-tuned Whisper model checkpoints and specialized audio datasets
├── Dataset/        
│   ├── Kedah/                  # Fine-tuned Whisper model checkpoints and specialized audio datasets
│   └── Kelantan/
└── NoteBook/                
    ├── Train.ipynb                 # Jupyter Notebooks used for model training
    ├── Evaluation.ipynb                  # Jupyter Notebooks used for model evaluation, and inference testing
    └── Inference.ipynb                  # Jupyter Notebooks used for model evaluation, and inference testing

