# 💼 AI Job Application Agent with Streamlit & CrewAI

An autonomous multi-agent career preparation system built with **CrewAI** and powered by **Google Gemini**. It automatically analyzes job postings and candidate profiles to generate complete, high-impact application packages.

---

## ✨ Features

- **Multi-Agent Architecture**:
  - **Job Requirements Analyst**: Dissects job descriptions, discovers culture values, required competencies, and key phrasing.
  - **Career Coach & Application Writer**: Generates tailored application materials matching the candidate to the role.
- **Complete Application Package**:
  - 📝 **Tailored Cover Letter** (Hook, Evidence, Close)
  - 🎯 **Top 5 Resume Highlights** aligned to the specific requirements
  - 💡 **10 High-Probability Interview Questions** (5 Behavioral + 5 Technical) with detailed STAR and conceptual answer frameworks
  - 💰 **Salary Negotiation Range** based on role leveling and company tiers
- **🖥️ Interactive Streamlit Web UI**: Full web dashboard with custom input fields, real-time generation, and one-click markdown export.
- **💻 CLI Mode**: Fast terminal workflow for batch automation.

---

## 🚀 Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/RohanExploit/job-application-agent.git
cd job-application-agent
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file in the root folder:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
CREWAI_TELEMETRY_OPT_OUT=true
OTEL_SDK_DISABLED=true
```

---

## 🖥️ Running the Streamlit Web UI

Launch the interactive dashboard:
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 💻 Running via CLI

Run with built-in sample data:
```bash
python agent.py
```

Run with custom job and candidate inputs:
```bash
python agent.py \
  --job-desc "Senior Python Engineer at Stripe..." \
  --candidate "Jane Doe - 7 years Python, FastAPI, Docker, Kubernetes..."
```

---

## 🛠️ Tech Stack
- **Multi-Agent Framework**: [CrewAI](https://github.com/crewAIInc/crewAI)
- **LLM**: Google Gemini (`gemini-3.5-flash-lite` / `gemini-3.8-flash`)
- **Web Interface**: [Streamlit](https://streamlit.io/)
- **Configuration**: `python-dotenv`
