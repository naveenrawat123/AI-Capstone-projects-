from asr.whisper_transcriber import transcribe_audio
from llm.openai_query import extract_object
from detection.detect import run_yolo
from fallback.logic import handle_missing
from tts.google_tts import speak

def process_voice_command(audio_path, image_path):
    text_query = transcribe_audio(audio_path)
    print("User said:", text_query)

    object_query = extract_object(text_query)
    print("Looking for:", object_query)

    detected, location = run_yolo(image_path, object_query)

    if detected:
        response = f"The {object_query} is at location {location}"
    else:
        response = handle_missing(object_query)

    speak(response)

if __name__ == "__main__":
    process_voice_command("sample.wav", "demo.jpg")