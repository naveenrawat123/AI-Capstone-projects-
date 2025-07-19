# 🎯 VisionAssist – Voice-to-Vision AI System

**VisionAssist** is a multimodal AI system that combines **voice input**, **object detection** (YOLO), **language reasoning** (OpenAI GPT), and **text-to-speech** (Google TTS) to help users identify and locate objects in images using natural voice commands.

---

## 🧠 System Architecture

```
Voice Input → Whisper ASR → GPT-3.5 (Object Extraction) → YOLO Object Detection
                    ↘              ↘
                   Fallback Logic    → TTS Response
```

---

## 📦 Modules Overview

| Module         | Description |
|----------------|-------------|
| `asr/`         | Transcribes voice input using OpenAI Whisper |
| `llm/`         | Extracts object name from transcribed query using OpenAI GPT |
| `detection/`   | Runs YOLO object detection and checks if object exists |
| `fallback/`    | Generates standard fallback response if object not found |
| `tts/`         | Converts final text response into speech (Google TTS) |
| `training/`    | YOLO dataset and training wrapper |
| `main.py`      | End-to-end orchestration script |

---

## 🚀 Setup & Installation

### 🔧 Requirements
- Python 3.8+
- pip

### 📥 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔑 Set up OpenAI Key
Export your key as an environment variable:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

---

## ▶️ Run the System

```bash
python main.py
```

By default, it looks for:
- `sample.wav` – voice command audio file
- `demo.jpg` – input image for object detection

---

## 🧪 Sample Input / Output

### 🎤 Voice Command:
> “Where is the red shoe?”

### 🧠 LLM Extracts:
> `"red shoe"`

### 🖼️ YOLO Detects:
> `"shoe detected at [x1, y1, x2, y2]"`

### 🔁 If Not Found:
> Fallback: “Sorry, I couldn’t find the red shoe.”

### 🔊 Final Response:
> Spoken via Google TTS

---

## 🏋️‍♂️ Train Your Own YOLO Model

Edit `training/custom.yaml` and place your dataset in:
```
training/dataset/images/train
training/dataset/labels/train
```

Then run:
```bash
python training/train.py
```

---

## 📄 License

MIT License © 2025 Naveen Rawat

---

## 🙌 Credits

- [YOLOv5](https://github.com/ultralytics/yolov5)
- [Whisper](https://github.com/openai/whisper)
- [OpenAI GPT](https://openai.com/)
- [Google TTS](https://pypi.org/project/gTTS/)