import gradio as gr
import google.generativeai as genai
from datetime import datetime


# Função para obter a chave da API de um arquivo
def get_api_key():
    with open('api_key.txt', 'r') as f:
        return f.read().strip()


# Função para configurar a API
def configure_api():
    api_key = get_api_key()
    if not api_key:
        raise ValueError("API key is missing or invalid.")
    genai.configure(api_key=api_key)


# Chamada para configurar a API
configure_api()

# Obter modelos suportados
models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
default_model = models[0] if models else None

# Variável global para manter o histórico
history = []


# Função para gerar resposta
def generate_response(question, model_name):
    model = genai.GenerativeModel(model_name)
    try:
        response = model.generate_content(question)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history.append((timestamp, question, response.text, model_name))
        return response.text, '\n\n'.join([f"{t}\nUser: {q}\n{m}: {a}" for t, q, a, m in history])
    except Exception as e:
        return str(e), ""


# Função para limpar o histórico
def clear_history():
    global history
    history = []
    return "", ""


# Interface do Gradio
with gr.Blocks() as interface:
    gr.Markdown("# Generative AI Interface")
    with gr.Row():
        with gr.Column():
            question_input = gr.Textbox(lines=2, placeholder="Type your question here...", label="Question")
            model_select = gr.Dropdown(choices=models, value=default_model, label="Select Model")
            generate_button = gr.Button("Generate")
        with gr.Column():
            output_textbox = gr.Textbox(label="Response", interactive=False)
            history_textbox = gr.Textbox(label="History", interactive=False, lines=15)
            clear_button = gr.Button("Clear History")

    generate_button.click(
        generate_response,
        inputs=[question_input, model_select],
        outputs=[output_textbox, history_textbox]
    )
    clear_button.click(
        clear_history,
        outputs=[output_textbox, history_textbox]
    )

if __name__ == "__main__":
    interface.launch(share=True)
  
