# Bulgarian History Tutor
This Bulgarian History Tutor provides assistance for students learning about Bulgarians under the rule of the Ottomans during the 15th–17th century. 





## About

This project is an AI tutor specifically focused on the period of Bulgarian history under Ottoman rule (15th to 17th centuries). It uses a RAG (Retrieval-Augmented Generation) approach: the system retrieves 
information from our knowledge base (__DIY History Textbook.txt__) and uses it to answer questions in Bulgarian.

This project was developed as part of a research project for UCHIBAN.  
It is an experimental prototype and should not be treated as a polished educational tool.


## Features

- Ask questions in Bulgarian about the historical content in __DIY History Textbook.txt__ (e.g., facts, context, events, figures, culture).
- Generate study materials such as test questions or summaries based on __DIY History Textbook.txt__.
- RAG pipeline: combines retrieved passages with an LLM for more grounded answers.
- Built-in support for Ollama LLMs.
- Extensible: feel free to replace or expand __DIY History Textbook.txt__.


## How to run the code:
#### 1. Download the project files OR clone the repository
##### 1.1 Downloading the project files
- Either click Code → Download ZIP on GitHub and unzip it
- Or download just the needed files (main.py, requirements.txt, and DIY History Textbook.txt) into a folder
##### 1.2 Cloning the repository
```
git clone https://github.com/cyn3a/RAG-Bulgarian-History-Tutor.git
cd RAG-Bulgarian-History-Tutor
```

#### 2. Install dependencies
```
pip install -r requirements.txt
```
#### 3. Install Ollama

This project uses [Ollama](https://ollama.com) to run the local LLM.  
Download and install Ollama from the official site:

- **Linux / macOS:**  
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
- Windows:
Download the installer from https://ollama.com/download

Verify it’s installed by running ` ollama --version `.

#### 4. Pull the LLM model
```
ollama pull s_emanuilov/BgGPT-v1.0:2.6b
```

#### 5. Run the tutor
```
python main.py
```

Then ask a history question, e.g.:
> Каква е ролята на църквата през този период?


## Architecture & Design

**Retrieval module**  
A document store (_DIY History Textbook.txt_) is indexed with embeddings. On each user query, relevant passages are retrieved.

**Generation / LLM module**  
The retrieved passages are used to augment the user query, which is then fed into an LLM that grounds its answer in the retrieved content.

**Main orchestration**  
The main.py script handles user interaction (reading a question, calling the retrieval + generation parts, and returning an answer).

The repo currently contains:  

_requirements.txt_ - packages used in the project  
_main.py_ — entry point  
_DIY History Textbook.txt_ — knowledge base  
_questions.txt_ - example prompts  
