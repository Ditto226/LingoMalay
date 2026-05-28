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
├── App/                             # Flutter Mobile Application
│   ├── android/, ios/, web/         # Native platform configurations
│   ├── assets/                      # Global assets (icons, placeholder audio, etc.)
│   └── lib/                      
│        ├── models/                 # Data structures 
│        ├── provider/               # State management 
│        ├── routes/                 # App navigation mapping
│        ├── screens/                # UI Views 
│        ├── themes/                 # App styling and color palettes
│        ├── utils/                  # Helper functions
│        ├── widgets/                # Reusable UI components
│        ├── firebase_options.dart               
│        └── main.dart            
└── Models_Transcribe/   
    ├── API/                        # Core backend API services and endpointsand server deployment configurations sent to Google Cloud (GDC)
    ├── Model/                      # Fine-tuned Whisper model checkpoints
    ├── Dataset/                    # Specialized audio datasets
    └── NoteBook/                   # Jupyter Notebooks used for model training, evaluation, and inference testing
