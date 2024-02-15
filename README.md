## Quick Ollama installation
- Spin up Ollama container
    ```bash
    docker compose up -d
    ```
- Run Llama2 model inside the container
    ```bash
    docker exec -it ollama ollama run llama2
    ```
- Run llava (Vision Assistant) model inside the container
    ```bash
    docker exec -it ollama ollama run llava
    ```
- Run odellama model inside the container
    ```bash
    docker exec -it ollama ollama run codellama
    ```

## Test LLM models
- Install required packages
    ```bash
    pip install -r requirements.txt
    ```

- llama2
    ```bash
    py llama2.py
    ```
- codellama
    ```bash
    py codellama.py
    ```

- llava (Vision Assistant)
    ```bash
    py vision.py
    ```