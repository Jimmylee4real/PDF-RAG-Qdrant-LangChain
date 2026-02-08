# PDF-RAG-Qdrant-LangChain

RAG using LangChain, Qdrant DB (Docker), and OpenAIEmbeddings

This repository demonstrates a minimal **Retrieval-Augmented Generation (RAG) (檢索增強生成)** workflow with two main phases:

1. **Indexing phase (`index.py`)**  
   Load a PDF, split it into chunks, create embeddings, and store vectors in a vector database.

2. **Retrieval phase (`chat.py`)**  
   Take a user question, retrieve the most relevant chunks from the vector database, then use an LLM to generate an answer grounded in the retrieved context (with page references).

---

## Why RAG?

Traditional LLMs can hallucinate or provide irrelevant answers when they rely only on their PAST training data.  
RAG improves reliability by combining the intelligence of an LLM with an external knowledge source (the HKMA Practical Insights Report in this project).

---

## Key Document Used (Public Link)

This project indexes a publicly available PDF from the HKMA website:

- **Practical Insights Report** — **Generative Artificial Intelligence (GenA.I.) Sandbox** (HKMA × Cyberport)  
  Public link: <https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20251031-6-EN/20251031-6-EN.pdf>

This report is a prime example of the HKMA Fintech 2030 initiative fostering **responsible AI innovation** in Hong Kong’s fintech ecosystem, jointly promoted by the **Hong Kong Monetary Authority (HKMA)** and the city’s digital tech hub and AI accelerator (**Cyberport**). It provides practical learnings from technical trials between participating banks and technology firms—covering topics such as **data preparation**, **model fine-tuning**, and **output evaluation**.

Because the report is long and can take significant time to digest end-to-end, **RAG helps you ask specific questions and quickly retrieve relevant sections**, producing responses that are relevant and grounded in the source document (with page references).

---

## Setup

### Prerequisites
- Python 3.10+ recommended
- Docker + Docker Compose
- OpenAI API key

### 1) Start Qdrant (Vector DB)
```bash
docker compose up -d
