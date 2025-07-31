import whisper

# Load the Whisper model (base or tiny for speed)
model = whisper.load_model("base")

# Path to your audio file
audio_path = "no_english.mp3"  # Replace with the actual path if needed

# Transcribe with language detection
result = model.transcribe(audio_path, language=None)

# Show results
print("Detected Language:", result["language"])
print("Transcription:", result["text"])
