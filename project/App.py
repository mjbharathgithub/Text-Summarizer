!pip install transformers gradio

from transformers import pipeline
import gradio as gr


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

MAX_INPUT_CHARACTERS = 1000  # Maximum allowed input characters
MAX_OUTPUT_CHARACTERS = 400   # Approximate maximum output characters (we'll use tokens)
MAX_OUTPUT_TOKENS = 100 # Maximum output tokens.  Adjust as needed to get 400 chars approax.

def summarize_text(text):
    """
    Takes input text, checks its length, and returns the summarized text (up to a token limit).
    """
    if len(text) > MAX_INPUT_CHARACTERS:
        return f"Error: Input text exceeds the maximum limit of {MAX_INPUT_CHARACTERS} characters."

    summary = summarizer(text, max_length=MAX_OUTPUT_TOKENS, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def update_character_count(text):
    """
    Updates the character count displayed below the input textbox.
    """
    return f"Character Count: {len(text)} / {MAX_INPUT_CHARACTERS}"

with gr.Blocks(title="Text Summarizer") as iface:
    gr.Markdown("<h1 style='text-align: center;'>Text Summarizer - Developed by Joseph Bharath</h1>") 
    gr.Markdown(f"Enter text (up to {MAX_INPUT_CHARACTERS} characters) to summarize. The character count updates as you type.  The output will be approximately {MAX_OUTPUT_CHARACTERS} characters.")

    input_textbox = gr.Textbox(lines=5, placeholder=f"Enter text to summarize (max {MAX_INPUT_CHARACTERS} characters)...")
    char_count_output = gr.Textbox(label="Character Count", value=f"Character Count: 0 / {MAX_INPUT_CHARACTERS}", interactive=False)
    output_textbox = gr.Textbox(lines=3, placeholder=f"Generated summary (approx. {MAX_OUTPUT_CHARACTERS} characters)...")

    input_textbox.change(fn=update_character_count, inputs=input_textbox, outputs=char_count_output)

    submit_button = gr.Button("Summarize")
    submit_button.click(fn=summarize_text, inputs=input_textbox, outputs=output_textbox)

iface.launch(share=True)
