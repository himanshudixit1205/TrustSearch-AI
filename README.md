## 🧠 TrustSearch AI - Reliable Web Search Agent (RAG + LLM)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![LLM](https://img.shields.io/badge/LLM-Llama--3.1-orange)
![RAG](https://img.shields.io/badge/Architecture-RAG-blueviolet)
![Search](https://img.shields.io/badge/Search-Tavily-green)
![Domain](https://img.shields.io/badge/Domain-AI%20Agents-red)
![License](https://img.shields.io/badge/License-MIT-success)

An end-to-end AI-powered web search agent that retrieves real-time information and generates reliable, source-backed answers using a Retrieval-Augmented Generation (RAG) pipeline.

This project demonstrates a complete AI system workflow — including web search integration, data filtering, context building, LLM-based answer generation, and hallucination control.

------------------------------------------------------------------------

## ✨ Key Features

- Real-time web search using Tavily API
- LLM-based answer generation using Groq (Llama 3.1)
- Retrieval-Augmented Generation (RAG) pipeline
- Filtering of unreliable sources (social media, low-quality domains)
- Removal of blocked / CAPTCHA-protected content
- Context cleaning, deduplication, and validation
- Structured answers with source attribution
- Modular and maintainable code design

------------------------------------------------------------------------

## ⚙️ System Workflow

1. User inputs a natural language query  
2. Tavily API retrieves relevant web results  
3. Results are filtered:
   - Removes unreliable domains (e.g., Reddit, Facebook)  
   - Skips blocked / CAPTCHA pages  
   - Eliminates duplicate and low-quality content  
4. Cleaned data is converted into structured context  
5. LLM generates a factual answer using only this context  
6. Final response includes answer and sources  

------------------------------------------------------------------------

## 📦 Example

### Input

    Compare Samsung Galaxy S24 and iPhone 15 specifications

### Output

    Answer:
    Samsung Galaxy S24 offers higher brightness and a more flexible camera system, 
    while iPhone 15 focuses on color accuracy and ecosystem integration.

    Sources:
    https://example.com/article1
    https://example.com/article2

------------------------------------------------------------------------

## 📜 Project Structure

    .
    ├── main.py        # Entry point and agent orchestration
    ├── search.py      # Web search and filtering logic
    ├── llm.py         # LLM prompt and response generation
    ├── utils.py       # Context building and cleaning
    ├── requirements.txt
    └── .env           # API keys (not included)

------------------------------------------------------------------------

## 🛠️ Tech Stack

- Python
- Tavily API (Web Search)
- Groq API (LLM - Llama 3.1)
- Requests
- BeautifulSoup
- python-dotenv

------------------------------------------------------------------------

## 🚀 Installation

    git clone <your-repo-url>
    cd <your-folder>
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

------------------------------------------------------------------------

## 🔑 Environment Setup

Create a `.env` file in the root directory:

    GROQ_API_KEY=your_groq_api_key
    TAVILY_API_KEY=your_tavily_api_key

------------------------------------------------------------------------

## ▶️ Usage

    python main.py

Enter your query when prompted.

------------------------------------------------------------------------

## 📊 Key Design Highlights

- Context-first answering to reduce hallucinations  
- Source filtering before LLM processing  
- Separation of concerns across modules  
- Basic validation layer to detect unreliable responses  

------------------------------------------------------------------------

## ⚠️ Limitations

- Output quality depends on retrieved data  
- No advanced ranking or scoring of sources  
- Limited context window may omit details  

------------------------------------------------------------------------

## 🔮 Future Improvements

- Source ranking and relevance scoring  
- Query-aware filtering (e.g., product variants)  
- Confidence scoring for answers  
- Caching for repeated queries  
- Improved validation and consistency checks  

------------------------------------------------------------------------

## 👤 Author

Himanshu Dixit

------------------------------------------------------------------------

## ⭐ If You Found This Useful

Feel free to star the repository or connect with me.