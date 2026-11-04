import os
import sys
import streamlit as st
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

load_dotenv()
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"
os.environ["OTEL_SDK_DISABLED"] = "true"

from agent import SAMPLE_JOB, SAMPLE_CANDIDATE, run_job_application_crew

st.set_page_config(
    page_title="AI Job Application Agent",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #64748B;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
        border: none;
        transition: background-color 0.2s;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
    }
    .result-card {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.2rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">💼 AI Job Application Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">CrewAI Multi-Agent System powered by Google Gemini 3.8 Flash • Generates tailored cover letter, resume highlights, interview questions, and salary negotiation guide.</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Configuration")
    gemini_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if gemini_key:
        st.success("✅ Gemini API Key Loaded")
    else:
        st.warning("⚠️ No API Key found in .env")
        custom_key = st.text_input("Enter Gemini API Key:", type="password")
        if custom_key:
            os.environ["GOOGLE_API_KEY"] = custom_key
            os.environ["GEMINI_API_KEY"] = custom_key
            st.success("Key applied!")

    st.markdown("---")
    st.subheader("👥 CrewAI Multi-Agent Architecture")
    st.markdown("""
    1. **Job Requirements Analyst**: Decodes JD, finds keywords, signals & culture values.
    2. **Career Coach & Application Writer**: Crafts high-impact tailored application materials.
    """)

    if st.button("🔄 Reset to Default Samples"):
        st.session_state["job_desc"] = SAMPLE_JOB
        st.session_state["candidate_profile"] = SAMPLE_CANDIDATE
        st.rerun()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 1. Job Description")
    job_desc = st.text_area(
        "Paste the Target Job Posting:",
        value=st.session_state.get("job_desc", SAMPLE_JOB),
        height=320,
        help="Paste the full job description or requirements here."
    )

with col2:
    st.subheader("👤 2. Candidate Profile")
    candidate_profile = st.text_area(
        "Paste Your Resume / Experience Summary:",
        value=st.session_state.get("candidate_profile", SAMPLE_CANDIDATE),
        height=320,
        help="Paste your candidate bio, skills, education, and notable achievements."
    )

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 Generate Application Package"):
    if not job_desc.strip():
        st.error("Please enter a job description.")
    elif not candidate_profile.strip():
        st.error("Please enter candidate profile details.")
    else:
        with st.spinner("🤖 Multi-Agent Crew is analyzing requirements and crafting your tailored application package..."):
            try:
                result = run_job_application_crew(job_desc, candidate_profile)
                st.session_state["result"] = result
                st.success("✨ Application package generated successfully!")
            except Exception as e:
                st.error(f"Error during agent execution: {str(e)}")

if "result" in st.session_state:
    result_text = st.session_state["result"]
    st.markdown("---")
    st.subheader("📦 Generated Job Application Package")
    
    st.markdown(result_text)
    
    st.download_button(
        label="📥 Download Application Package (.md)",
        data=result_text,
        file_name="job_application_package.md",
        mime="text/markdown"
    )
