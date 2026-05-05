# Edubot 🎓

Edubot is an intelligent, Retrieval-Augmented Generation (RAG) based educational chatbot designed to help students find the best college fit. By analyzing historical college admission records (such as predicted opening and closing ranks), Edubot provides personalized, data-driven college recommendations through an interactive conversational interface.

## ✨ Features

- **Intelligent RAG Pipeline:** Leverages LangChain and a locally hosted Llama-2 (7B) model to understand dynamic user constraints and deliver accurate recommendations.
- **Large-Scale Semantic Search:** Ingests and processes over 40,000 historical admission records using HuggingFace Sentence Transformers for dense embeddings and FAISS for ultra-fast, high-dimensional similarity retrieval.
- **Interactive UI:** Features a responsive, asynchronous web interface built with Chainlit for a seamless user experience.

## 🛠️ Technologies Used

- **Language:** Python
- **LLM Framework:** LangChain
- **Large Language Model:** Llama-2 7B (via CTransformers)
- **Vector Database:** FAISS (Facebook AI Similarity Search)
- **Embeddings:** HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`)
- **Frontend / UI:** Chainlit

## 🚀 Getting Started

Follow these steps to set up and run Edubot on your local machine.

### Prerequisites

Ensure you have Python 3.8+ installed. It is highly recommended to use a virtual environment.

### 1. Clone the repository

```bash
git clone https://github.com/aashna03/Edubot.git
cd Edubot
```

### 2. Install Dependencies

Install the required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Generate the Vector Database

Before running the bot, you need to process the CSV data and generate the vector database. Run the data ingestion script:

```bash
python ingest.py
```
*Note: This will create a `vectorstore/` folder containing the FAISS database.*

### 4. Run the Chatbot

Start the Chainlit server to launch the chatbot interface:

```bash
chainlit run model.py -w
```
Your browser should automatically open the interface at `http://localhost:8000`. If not, you can navigate there manually.

## 📂 Project Structure

- `model.py` - Core logic for the LLM, LangChain retrieval QA chain, and the Chainlit frontend application.
- `ingest.py` - Data pipeline script to load CSV data, chunk text, generate embeddings, and create the FAISS vector database.
- `data/` - Contains the dataset (`final_all_with_loc.csv`) with the college admission records.
- `requirements.txt` - Project dependencies.

---
*Developed by [Aashna](https://github.com/aashna03)*
