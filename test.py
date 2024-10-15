
import os
import pyaudio
import json
from vosk import Model, KaldiRecognizer

# Step 3: Load Vosk model
model_path = "model"
if not os.path.exists(model_path):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)

model = Model(model_path)

# Step 4: Initialize microphone
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Step 5: Capture audio
rec = KaldiRecognizer(model, 16000)

print("Please say your authentication phrase...")

while True:
    data = stream.read(4000, exception_on_overflow=False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result_dict = json.loads(result)
        text = result_dict.get("text", "")
        
        # Step 6: Recognize speech
        print(f"Recognized: {text}")
        
        # Step 7: Authenticate user
        if text == "bonjour":
            print("Authentication successful!")
            break
        else:
            print("Authentication failed. Please try again.")