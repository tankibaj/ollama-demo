from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = Ollama(base_url='https://llm.local.naim.run',
             model="llama2",
             callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

if __name__ == '__main__':
    while True:
        query = input("\nQuery: ")
        if query == "exit":
            break
        if query.strip() == "":
            continue
        llm(query)
