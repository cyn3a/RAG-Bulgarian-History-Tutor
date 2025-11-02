import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

loader = TextLoader("DIY History Textbook.txt", encoding = "utf-8")
docs = loader.load()

text_splitter = TokenTextSplitter(
    chunk_size = 500, chunk_overlap = 200
)

all_splits = text_splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")

embeddings_dim = len(embeddings.embed_query("hello world"))
index = faiss.IndexFlatIP(embeddings_dim)


vector_store = FAISS(
    embedding_function = embeddings,
    index = index,
    docstore = InMemoryDocstore(),
    index_to_docstore_id = {},    
)


ids = vector_store.add_documents(documents = all_splits)




from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="s_emanuilov/BgGPT-v1.0:2.6b")

template = """
Ти си ИИ асистент, който помага на ученици да учат по история. Учтив си и винаги искаш да помогнеш.
Отговори на въпроса като използваш само дадения контекст.
Дай кратък, конкретен отговор, като включваш само най-важните факти.
Ако контекстът не съдържа информация по въпроса кажи, че не знаеш.
След като си дадеш отговора, предложи помощ по близко свързана тема. Задай въпрос, за да насърчиш ученика да продължи разговора.


Контекст: {context}
Въпрос: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


print("Здравей! Как мога да помогна?")
while True: 
    query = input() 
    context = vector_store.similarity_search(query, k = 3)
    result = chain.invoke({"context": context, "question": query})
    print(result)
    print("\n\n")



