# GenAI_report_finder

This project creates an AI assistant that helps users find the most relevant Power BI report, based on a natural language query.

🧠 The user describes the information they need (e.g., “sales by region this quarter”), and the app returns the best-matching report using a **Retrieval-Augmented Generation (RAG)** approach — but without the "generation" part.

![image](https://github.com/user-attachments/assets/6da09ab0-4b9d-493b-969c-70cd648b3161)



---

## 🔍 How It Works

1. Descriptions of reports are embedded as vectors using OpenAI.
2. A user query is also embedded in the same vector space.
3. The system retrieves the closest matching report vectors using ChromaDB.
4. The app displays the name and description of the top matches.

---

## 📁 Project Structure

```
GenAI_report_finder/
├── app/
│   ├── main.py              # Streamlit UI
│   └── retriever.py         # Vector search logic
│
├── data/
│   └── reports.xlsx         # Excel file with report descriptions (not committed)
│
├── scripts/
│   └── build_vector_db.py   # Loads Excel and builds the vector database
│
├── vectorstore/             # ChromaDB vector DB (generated, not committed)
│
├── .env.sample              # Template for environment variables
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/GenAI_report_finder.git
cd GenAI_report_finder
```

### 2. Set Up Environment

Create a `.env` file from the template:

```bash
cp .env.sample .env
```

Update it with your OpenAI API key.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Build the Vector Database

```bash
python scripts/build_vector_db.py
```

### 5. Run the App

#### Option A: Local (Dev Mode)

```bash
streamlit run app/main.py
```

#### Option B: Docker (Production Ready)

```bash
docker build -t genai_report_finder .
docker run --env-file .env -p 8501:8501 genai_report_finder
```

---

## ✅ Requirements

- Python 3.10+
- [OpenAI API Key](https://platform.openai.com/)
- [Docker (optional)](https://www.docker.com/products/docker-desktop/)

---

## 🛡️ Security

Do **not** commit your `.env` file or actual report data. Use `.env.sample` to share expected environment variables safely.

---

## 📬 Contact

Questions or feedback? Open an issue or contact [yourusername](https://github.com/manuelescola).
