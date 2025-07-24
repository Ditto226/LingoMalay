from fastapi import FastAPI, File, UploadFile
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import torchaudio
import io
import os

app = FastAPI()

# Load model and processor
MODEL_PATH = "/app/model"  # inside Docker container
processor = WhisperProcessor.from_pretrained(MODEL_PATH)
model = WhisperForConditionalGeneration.from_pretrained(MODEL_PATH)

model.eval()
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    try:
        audio_bytes = await file.read()
        if not audio_bytes:
            return JSONResponse(status_code=400, content={"error": "Empty audio file"})

        # Load audio
        waveform, sr = torchaudio.load(io.BytesIO(audio_bytes))
        if sr != 16000:
            resampler = torchaudio.transforms.Resample(orig_freq=sr, new_freq=16000)
            waveform = resampler(waveform)
        waveform = waveform.squeeze().numpy()

        inputs = processor.feature_extractor(waveform, sampling_rate=16000, return_tensors="pt")
        input_features = inputs.input_features.to(device)

        with torch.no_grad():
            predicted_ids = model.generate(input_features, max_new_tokens=64, eos_token_id=eos_token_id)

        transcription = processor.tokenizer.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        return {"transcription": transcription}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

