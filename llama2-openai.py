from openai import OpenAI

client = OpenAI(
    base_url='https://llm.local.naim.run/v1',
    api_key='ollama',  # required, but unused
)

response = client.chat.completions.create(
    model="llama2",
    messages=[
        # {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Introduce yourself."},
    ]
)

if __name__ == '__main__':
    # Make the request
    print(response.choices[0].message.content)
