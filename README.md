# Ollama Gradio Chat UI

This project is a lightweight Gradio interface for interacting with [Ollama](https://ollama.com/) local language models. It enables real-time streamed conversations with a selected model (default: `gemma3n:e2b`).

## 🧠 Features

- 🔁 Streaming chat responses
- ⚡ Fast local inference via Ollama
- 🧩 Model selection ready via `gr.State`
- 🧼 Simple and minimal interface

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/dibend/gradio-ollama-chat-client.git
cd ollama-gradio-chat-client
```

### 2. Install Dependencies

Make sure you have Python 3.9+ and [Ollama](https://ollama.com/) running locally.

```bash
pip install gradio ollama
```

### 3. Run the App

```bash
python app.py
```

It will launch a local web UI on `http://127.0.0.1:7860`

## 🛠 Configuration

You can change the default model in the script:

```python
DEFAULT_MODEL = "gemma3n:e2b"
```

Make sure the model is pulled using `ollama run` beforehand or manually via:

```bash
ollama pull gemma3n:e2b
```

## 📁 File Structure

```
.
├── app.py         # Main application
├── README.md      # This file
```

## 🧩 Dependencies

- [Gradio](https://gradio.app/)
- [Ollama Python Client](https://pypi.org/project/ollama/)

## 🙏 Credits

Made with ❤️ using [Ollama](https://ollama.com) + [Gradio](https://gradio.app)
