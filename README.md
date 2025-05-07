# 🧠 Text Summarizer using BART and Gradio

A simple yet powerful web-based text summarization app built with [Hugging Face Transformers](https://huggingface.co/transformers/) and [Gradio](https://www.gradio.app/). This app uses the `facebook/bart-large-cnn` model to summarize text in seconds.

## 🚀 Features

- ✍️ Accepts up to **1000 characters** of input text.
- 📉 Generates concise summaries with a **maximum of 100 tokens** (about 400 characters).
- 📊 Live character count updates as you type.
- 🧪 Powered by the **BART** model, fine-tuned for summarization tasks.
- 🌐 Interactive and user-friendly **Gradio interface**.

## 🧰 Tech Stack

- **Python**
- **Hugging Face Transformers** (`facebook/bart-large-cnn`)
- **Gradio** (UI)

## 🛠️ How It Works

1. User enters input text in the textbox (max 1000 characters).
2. The live counter updates the character count.
3. On clicking **Summarize**, the text is processed by the BART model.
4. The summary is returned and displayed in the output box.

## 📦 Installation & Run

```bash
pip install transformers gradio
python app.py
