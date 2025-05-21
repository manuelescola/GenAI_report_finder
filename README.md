# GenAI_report_finder
This repo creates an AI that finds a Power BI report for you using a Retrieval-Augmented Generation (RAG) system with a very practical use case:
🧠 The user describes the information they need (e.g., “sales by region this quarter”), and the website returns the most relevant Power BI report from a set of existing reports.

Under the hood:
1. Descriptions of reports are embedded as vectors.
2. A user query is also embedded.
3. The closest vectors (i.e., most semantically similar reports) are retrieved.
4. The app shows the names and descriptions of those reports.

_This is RAG without the generation step — just the “R” (Retrieval) part of RAG._

The repo is structured as follows.

GenAI_report_finder/
│
├── .venv
│
├── app/
│   ├── main.py             # Streamlit app
│   └── retriever.py        # RAG logic to fetch best-matching report
│
├── data/                   
│   └── reports.xlsx        # Excel file with report descriptions
│
├── scripts/
│   └── build_vector_db.py  # Converts Excel → VectorDB
│
├── vectorstore/            # ChromaDB persisting folder with report descriptions in a vector db
│   ├── chroma.sqlite3
│   └── 4e7867b3-5258-4081-a123-1abde192b78b
│       ├── data_level0.bin
│       ├── header.bin
│       ├── length.bin
│       └── link_lists.bin
│
├── .dockerignore
│
├── .env
│
├── .gitignore
│
├── docker-compose.yml
│
├── Dockerfile
│
├── README.md
│
└── requirements.txt



