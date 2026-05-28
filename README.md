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

## 🛠️ System Architecture

```text
+----------------------------+
|     Mobile Application     |
|----------------------------|
| - Audio Record/Upload      |
| - Playback & UI            |
| - Dialect Selection        |
| - Upload to Firebase       |
| - Display Transcription    |
+-------------+--------------+
              |
              v
+----------------------------+
|     Firebase Services      |
|----------------------------|
| - Authentication           |
| - Firestore (Metadata)     |
| - Storage (Audio Files)    |
+-------------+--------------+
              |
              v
+-----------------------------------------------+
|           Transcription Routing Layer          |
|-----------------------------------------------|
| Based on selected dialect, route to:           |
| - Custom Whisper API (Kedah / Kelantan)        |
| - Mesolitica API (Standard Malay / fallback)   |
+-------------+--------------+------------------+
              |                              |
              v                              v
+----------------------------+     +----------------------------+
| Custom Whisper API Server  |     |   Mesolitica API Endpoint  |
|----------------------------|     |----------------------------|
| - FastAPI backend          |     | - Hosted ASR service       |
| - Whisper-small fine-tuned |     | - RESTful API              |
+-------------+--------------+     +-------------+--------------+
              \                              /
               \                            /
                v                          v
         +----------------------------+
         |  Transcription Response     |
         | - JSON with transcript text |
         +-------------+--------------+
                       |
                       v
         +----------------------------+
         | Mobile App UI (Display)    |
         | - Show result in correct   |
         |   section with metadata    |
         +----------------------------+
```

## 📁 Repository Structure

Based on the project's architecture, the repository is organized into the following key modules:

```text
└── Models_Transcribe/   
    ├── API/                        # Core backend API services and server deployment configurations sent to Google Cloud (GDC) along with the model architecture
    ├── Dataset/                    # Specialized dialect audio datasets
    └── NoteBook/                   # Jupyter Notebooks used for model training, evaluation, and inference testing
```

📦 Deliverables & Testing

Because the mobile application codebase is exceptionally large, the pre-built application binary and the comprehensive research project report are hosted externally:

📄 [Read the Full Project Report](https://drive.google.com/drive/u/0/folders/1pZC3Z7EewRsrIU2zEP2wW10Uui-lGyRC
)

📱 [Download the LingoMalay APK](https://drive.google.com/drive/u/0/folders/1pZC3Z7EewRsrIU2zEP2wW10Uui-lGyRC
)

