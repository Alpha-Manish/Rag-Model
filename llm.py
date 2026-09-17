from langchain_ollama import ChatOllama


def get_llm():
    llm = ChatOllama(
           model="qwen3:0.6b",
           temperature=0.8,
           num_predict=512
    )

    return llm

# query = input("Enter your query: ")

# llm = get_llm()
# response = llm.invoke(query)

# print(response)