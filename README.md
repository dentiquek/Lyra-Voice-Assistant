# 🎙️ Lyra Voice Assistant

Lyra is an intelligent **voice-controlled assistant** built with Python, designed to perform tasks, respond to queries, and interact with users using natural language. It works just like popular voice assistants (Alexa, Google Assistant, Siri) — but fully customizable for your needs.

---

## 📌 Features

- 🎤 **Voice Recognition** – Understands spoken commands using speech-to-text.
- 🔊 **Text-to-Speech** – Responds in a human-like voice.
- 🎶 **Music Playback** – Play songs from a music library.
- 🌐 **Information Search** – Fetch answers from the internet.
- ⏰ **Reminders & Timers** – Set alarms and reminders.
- 🖥 **Desktop Automation** – Open applications, browse the web, and more.
- 🧠 **Modular Design** – Easy to extend with new commands.

---

## ⚙️ How It Works

1. **Wake Word Detection** – Lyra listens for a trigger phrase.
2. **Speech Recognition** – Converts your voice into text.
3. **Command Processing** – Interprets the text and matches it with available commands.
4. **Execution** – Runs the associated function (play music, fetch data, etc.).
5. **Response** – Converts the output to speech and speaks back to you.

---

## 🛠 Tech Stack

- **Python 3.x**
- **SpeechRecognition** – For converting speech to text.
- **PyAudio** – Capturing audio from microphone.
- **gTTS / pyttsx3** – Text-to-speech conversion.
- **Other APIs** – For internet search, music, and more.

---

## 📂 Project Structure

```

Mega project 1 - Lyra/
│
├── main.py              # Entry point to run Lyra
├── musicLibrary.py      # Music library handling
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API keys, configs)
├── Lyra\_main/           # Virtual environment
├── .gitignore
└── .git/                # Git repository data

````

---

## 🚀 Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/lyra-voice-assistant.git
   cd lyra-voice-assistant
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:

   * Create a `.env` file and add any required API keys/configuration.

5. **Run Lyra**:

   ```bash
   python main.py
   ```

---

## 🖥 Usage

* Speak your command after the wake word.
* Examples:

  * “Play music”
  * “What’s the weather?”
  * “Open YouTube”
  * “Set a timer for 5 minutes”

---

## 🔮 Future Enhancements

* 🌍 Multi-language support.
* 📱 Mobile app integration.
* 🤖 AI-powered contextual conversations.
* 🗂 More plugins (email, calendar, home automation).

---

## 🤝 Contributing

Contributions are welcome!
Fork the repo, make your changes, and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify it.

---
