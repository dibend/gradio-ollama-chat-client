import gradio as gr
import ollama

DEFAULT_MODEL = "gemma3n:e2b"

def chat_fn(message, history, model_name):
    history = history or []
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    messages += history
    messages.append({"role": "user", "content": message})

    partial_response = ""
    for chunk in ollama.chat(model=model_name, messages=messages, stream=True):
        content = chunk["message"]["content"]
        if content:
            partial_response += content
            yield history + [
                {"role": "user", "content": message},
                {"role": "assistant", "content": partial_response}
            ]

with gr.Blocks(title="Ollama LLM Chat UI") as demo:
    model_state = gr.State(DEFAULT_MODEL)  # ✅ wrap model in gr.State
    chatbot = gr.Chatbot(type="messages", label="Chat")
    user_input = gr.Textbox(label="Your message", placeholder="Type your question...")
    send_btn = gr.Button("Chat!")

    send_btn.click(
        fn=chat_fn,
        inputs=[user_input, chatbot, model_state],  # ✅ pass the state instead of string
        outputs=chatbot
    )

if __name__ == "__main__":
    demo.launch()
