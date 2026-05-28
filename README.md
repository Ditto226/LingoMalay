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
└── Models_Transcribe/   
    ├── API/                        # Core backend API services and server deployment configurations sent to Google Cloud (GDC) along with the model architecture
    ├── Dataset/                    # Specialized audio datasets
    └── NoteBook/                   # Jupyter Notebooks used for model training, evaluation, and inference testing
```

You can view this project report and apk here:
https://drive.google.com/drive/u/0/folders/1pZC3Z7EewRsrIU2zEP2wW10Uui-lGyRC
