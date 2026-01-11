import os
from dotenv import load_dotenv
import gradio as gr
from litellm import completion

load_dotenv(override=True)


def build_system_message(display_name: str, actual_model: str) -> str:
    return f"""You are running as: {display_name} ({actual_model}).
You must NOT claim to be ChatGPT, GPT-4, or any OpenAI-hosted model
unless the selected model explicitly is one.
If you do not know your identity, say so.
If you don't know the answer, say so.

You are an insightful, encouraging assistant.
Explain things clearly, with light humor and practical examples.
Be concise but thorough.
Assume the user is smart but not a professional programmer or mathematician.
"""


# provider is encoded in model prefix
MODELS = {
    "🧠 OpenAI | GPT-4.1 (large)": {
        "model": "openai/gpt-4.1",
    },
    "⚡ OpenAI | GPT-4o": {
        "model": "openai/gpt-4o",
    },
    "💸 OpenAI | gpt-4.1-nano": {
        "model": "openai/gpt-4.1-nano",
    },
    "🚀 OpenAI | GPT-4.1-mini": {
        "model": "openai/gpt-4.1-mini",
    },
    "🧪 Anthropic | Claude Sonnet": {
        "model": "claude-sonnet-4-5-20250929",
    },
    "🔥 Groq | Llama 3.3 70B": {
        "model": "groq/llama-3.3-70b-versatile",
    },
    "🖥️ Ollama | gpt-oss:20b (local)": {
        "model": "ollama/gpt-oss:20b",
        "api_base": "http://localhost:11434",
    },
}

import os
from dotenv import load_dotenv
import gradio as gr
from litellm import completion

load_dotenv(override=True)


def build_system_message(display_name: str, actual_model: str) -> str:
    return f"""You are running as: {display_name} ({actual_model}).
You must NOT claim to be ChatGPT, GPT-4, or any OpenAI-hosted model
unless the selected model explicitly is one.
If you do not know your identity, say so.
If you don't know the answer, say so.

You are an insightful, encouraging assistant.
Explain things clearly, with light humor and practical examples.
Be concise but thorough.
Assume the user is smart but not a professional programmer or mathematician.
"""


MODELS = {
    "🧠 OpenAI | GPT-4.1 (large)": {"model": "openai/gpt-4.1"},
    "⚡ OpenAI | GPT-4o": {"model": "openai/gpt-4o"},
    "💸 OpenAI | gpt-4.1-nano": {"model": "openai/gpt-4.1-nano"},
    "🚀 OpenAI | GPT-4.1-mini": {"model": "openai/gpt-4.1-mini"},
    "🧪 Anthropic | Claude Sonnet": {"model": "claude-sonnet-4-5-20250929"},
    "🔥 Groq | Llama 3.3 70B": {"model": "groq/llama-3.3-70b-versatile"},
    "🖥️ Ollama | gpt-oss:20b (local)": {
        "model": "ollama/gpt-oss:20b",
        "api_base": "http://localhost:11434",
    },
}

def stream_chat(prompt, model_choice, chat_history, llm_history):
    if not prompt.strip():
        yield chat_history, llm_history, "⚠️ **Empty message**", ""
        return

    config = MODELS[model_choice]
    actual_model = config["model"]
    system_message = build_system_message(model_choice, actual_model)

    # ➕ UI: user message
    chat_history.append({"role": "user", "content": prompt})
    chat_history.append({"role": "assistant", "content": ""})

    yield chat_history, llm_history, "⏳ **Request sent…**", actual_model

    messages = [
        {"role": "system", "content": system_message},
        *llm_history,
        {"role": "user", "content": prompt},
    ]

    response = completion(
        model=actual_model,
        api_base=config.get("api_base"),
        messages=messages,
        stream=True,
        drop_params=True,
        fallbacks=[],
    )

    assistant_msg = ""

    for chunk in response:
        delta = chunk.choices[0].delta.get("content", "")
        if delta:
            assistant_msg += delta
            chat_history[-1]["content"] = assistant_msg
            yield chat_history, llm_history, "🟢 **Responding…**", actual_model

    # LLM his
    llm_history.append({"role": "user", "content": prompt})
    llm_history.append({"role": "assistant", "content": assistant_msg})

    yield chat_history, llm_history, "✅ **Done**", actual_model


def reset_chat():
    return [], [], "ℹ️ **Conversation reset**", ""


with gr.Blocks(title="LLM Playground") as demo:
    gr.Markdown("## 💬 LLM Playground")

    chat_state = gr.State([])
    llm_state = gr.State([])

    model_selector = gr.Dropdown(
        choices=list(MODELS.keys()),
        value="🖥️ Ollama | gpt-oss:20b (local)",
        label="Model",
    )

    chatbot = gr.Chatbot(height=450)

    prompt = gr.Textbox(
        lines=3,
        placeholder="Type your message here…",
        label="Your message",
    )

    send_btn = gr.Button("Send")

    status = gr.Markdown("ℹ️ **Idle**")
    actual_model_box = gr.Markdown()

    send_btn.click(
        stream_chat,
        inputs=[prompt, model_selector, chat_state, llm_state],
        outputs=[chatbot, llm_state, status, actual_model_box],
    ).then(
        lambda: "",
        outputs=prompt,  # clear textbox after send
    )

    model_selector.change(
        reset_chat,
        outputs=[chatbot, llm_state, status, actual_model_box],
    )

demo.launch(inbrowser=True, share=False)




# MODELS Description:
# 🧠 OpenAI | GPT-4.1 (large): 
#    Full-size GPT-4.1. Highest quality responses, large context, slower and more expensive.
# ⚡ OpenAI | GPT-4o: 
#    Optimized GPT-4. Faster and cheaper, still supports long context, great for extended conversations.
# 💸 OpenAI | gpt-4.1-nano: 
#    Ultra-light GPT-4.1 variant. Fast, cheap, limited context, good for short prompts and quick tests.
# 🚀 OpenAI | GPT-4.1-mini: 
#    Lightweight GPT-4.1. Faster than large, moderate quality, shorter context.
# 🧪 Anthropic | Claude Sonnet: 
#    Claude 3.5 Sonnet. Friendly, supportive assistant. Good at explanations and light humor.
# 🔥 Groq | Llama 3.3 70B: 
#    Large LLaMA 3.3 70B model. Powerful, requires high memory/compute, suited for HPC or cloud.
# 🖥️ Ollama | gpt-oss:20b (local): 
#    Open-source GPT-OSS 20B, runs locally via Ollama. Full control, no API costs.