import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

LLAMA_ENDPOINT = 'http://localhost:11434/api/generate'
OPENAI_ENDPOINT = 'https://api.openai.com/v1/chat/completions'
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Carrega a chave do arquivo .env


def process_task(task, use_llama=True):
    agent_details = task['agent_details']
    enriched_prompt = (
        "Por favor, responda em português.\n"
        f"Função: {agent_details['role']}\n"
        f"Objetivo: {agent_details['goal']}\n"
        f"Histórico: {agent_details['backstory']}\n"
        f"Descrição da Tarefa: {task['description']}"
    )

    if use_llama:
        logging.info(f"Usando Llama API para a tarefa: {task['description']}")
        payload = {
            "model": "llama3:8b",
            "prompt": enriched_prompt,
            "stream": False
        }
        try:
            response = requests.post(LLAMA_ENDPOINT, json=payload)  # Removido o timeout
            response.raise_for_status()  
            return {
                "task": task['description'],
                "result": response.json().get('response')
            }
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro na API Llama: {str(e)}")
            return {
                "task": task['description'],
                "result": "Llama API request failed",
                "debug": str(e)
            }

    else:
        logging.info(f"Usando OpenAI API para a tarefa: {task['description']}")
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "Você é um assistente útil que responde em português."},
                {"role": "user", "content": enriched_prompt}
            ],
            "max_tokens": 1000
        }
        try:
            response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
            response.raise_for_status()  # Lança exceções para qualquer erro HTTP
            return {
                "task": task['description'],
                "result": response.json().get('choices', [{}])[0].get('message', {}).get('content', 'No response')
            }
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro na API OpenAI: {str(e)}")
            return {
                "task": task['description'],
                "result": "OpenAI API request failed",
                "debug": str(e)
            }

@app.route('/execute-tasks', methods=['POST'])
def execute_tasks():
    data = request.json
    tasks_data = data.get('tasks', [])

    if not tasks_data:
        return jsonify({"error": "No tasks provided"}), 400

    use_llama = data.get('use_llama', True)  # Defina para True se quiser usar a Llama, False para usar a OpenAI
    total_tasks = len(tasks_data)
    logging.info(f"Processando {total_tasks} tarefas com {'Llama' if use_llama else 'OpenAI'}.")

    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_task = {executor.submit(process_task, task, use_llama): task for task in tasks_data}

        results = []
        for i, future in enumerate(as_completed(future_to_task), start=1):
            try:
                result = future.result()
                results.append(result)
                remaining_tasks = total_tasks - i
                logging.info(f"Interação {i}/{total_tasks} concluída. Faltam {remaining_tasks} tarefas.")
            except Exception as e:
                logging.error(f"Erro durante o processamento da tarefa: {str(e)}")
                results.append({"error": str(e)})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
