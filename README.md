# genai-chat-interface
Interface Gradio para interagir com a API da Google Generative AI

# GenAI Chat Interface

Este projeto é uma interface gráfica simples, construída com [Gradio](https://gradio.app/), para interagir com a API da Google Generative AI. A interface permite que os usuários façam perguntas e obtenham respostas geradas por modelos de linguagem generativa.

## Funcionalidades

- **Seleção de modelo:** A interface lista os modelos disponíveis na API da Google Generative AI e permite que o usuário escolha qual usar.
- **Entrada de perguntas:** O usuário pode digitar uma pergunta na caixa de texto.
- **Geração de respostas:** A resposta gerada pelo modelo selecionado é exibida, juntamente com um histórico de interações anteriores.
- **Limpar histórico:** O usuário pode limpar o histórico de perguntas e respostas.

## Demonstração em Vídeo

Veja o vídeo da demonstração prática do código [aqui](example.mp4).

## Pré-requisitos

Antes de executar o projeto, você precisará:

- Python 3.8 ou superior
- Uma conta no Google Cloud com acesso à [Google Generative AI API](https://cloud.google.com/generative-ai)
- Um arquivo `api_key.txt` contendo sua chave da API

### Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/gustavochotti/genai-chat-interface.git
    cd genai-chat-interface
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    .\venv\Scripts\activate    # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Coloque sua chave da API no arquivo `api_key.txt`:
    - Crie um arquivo `api_key.txt` no diretório raiz do projeto.
    - Cole sua chave de API no arquivo.

### Uso

1. Execute o script:
    ```bash
    python nome-do-script.py
    ```

2. Acesse a interface no navegador, que será aberta automaticamente, ou siga o link que será exibido no terminal.

3. Digite sua pergunta e selecione o modelo que deseja usar para gerar a resposta.

### Estrutura do Projeto
- api_key.txt # Arquivo que contém a chave da API
- main.py # Script principal que executa o Gradio e a integração com a API
- requirements.txt # Arquivo com as dependências do projeto
- README.md # Este arquivo


### Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. As principais são:

- [Gradio](https://gradio.app/) - para criar a interface gráfica.
- [Google Generative AI Python Client](https://pypi.org/project/google-generativeai/) - para interagir com a API da Google Generative AI.

### Notas Importantes

- **API Key**: Certifique-se de manter sua chave da API em segurança e não compartilhá-la publicamente.
- **Limitações**: Certifique-se de que a sua chave da API possui permissões adequadas e de que você está ciente de qualquer limitação de uso imposta pela Google.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
