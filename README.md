# StoryTeller-TTS
A Voice generator based on input file with multipe dialogs or monologs

**StoryTeller-TTS** is a modular, multi-speaker text-to-speech (TTS) project designed for storytelling, audiobooks, dialogue simulations, and prototyping voice pipelines.

It supports:
- Multiple characters with consistent voices
- Pluggable TTS backends (local, cloud, simple/robotic)
- Docker-based execution
- Flexible output (per line, per speaker, or merged audio)

The project is intentionally **simple, extensible, and backend-agnostic**.

---

## ✨ Current Features

### ✅ Multi-Speaker Script Parsing
Input text supports named speakers with voice hints:

```
Person A (female): I have been to the beach.
Person B (female): That is great, have you had fun?
Person C (male): I want to go sometime as well.
```

Each speaker is:
- Detected automatically
- Assigned a consistent voice
- Reused across the entire script

---

### 🔌 Pluggable TTS Backends

You can switch between TTS engines using a single configuration flag.

| Backend | Description | Status |
|------|------------|--------|
| simple_tts_robotic | Local pyttsx3 (robotic/system voices) | ✅ Working |
| cloud_tts_voice_creator | Cloud TTS (OpenAI-style API) | ✅ Working |
| local_tts_voice_creator | Local TTS (Coqui / Piper ready) | 🚧 Stub |

---

### 🧠 Voice Registry
- Ensures each character keeps the same voice
- Supports unlimited speakers
- Simple gender-based allocation (extensible later)

---

### 🎧 Audio Output
- Per-line audio files
- Optional merged final audio (`full_story.mp3`)
- Uses pydub + ffmpeg

---

### 🐳 Docker-Ready
- No local Python environment required
- Input/output folders mounted to host
- Ready for CI/CD and deployment workflows

---

## 📁 Project Structure

```
StoryTeller-TTS/
├── core/
├── local_tts_voice_creator/
├── cloud_tts_voice_creator/
├── simple_tts_robotic/
├── input/
├── output/
├── config.py
├── main.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## ⚙️ Configuration

Edit `config.py`:

```
USE_LOCAL_TTS = False
USE_CLOUD_TTS = True
USE_SIMPLE_TTS = False

MERGE_AUDIO = True
OUTPUT_FORMAT = "mp3"
```

---

## 🚀 Running with Docker

```
export OPENAI_API_KEY="sk-xxxx"
docker-compose build
docker-compose up
```

Generated audio appears under `output/`.

---

## 🧪 Intended Use Cases

- Audiobooks with multiple characters
- Dialogue simulation
- Voice prototyping
- AI storytelling
- TTS backend experimentation

---

## 🔮 Future Optimizations

- CLI flags instead of config.py
- Environment-based configuration
- Better logging and error handling
- Unit tests

### Voice & Audio
- Emotion tags
- Per-speaker voice tuning
- Background music
- Pause and pacing control

---

## 🚀 Future Extensions

- FastAPI REST service
- Web UI
- Voice cloning
- Automatic speaker detection
- Style transfer

---

## 💡 Philosophy

StoryTeller-TTS favors:
- Clarity over cleverness
- Extensibility over premature optimization
- Backend independence

---

## 📜 License

Apache-2.0
