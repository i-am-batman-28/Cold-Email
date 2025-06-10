import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

# Custom CSS for colorful theme
st.markdown("""
    <style>
        .title {
            font-size: 2.5em;
            color: #FF4B4B;
            font-weight: bold;
        }
        .subtitle {
            font-size: 1.2em;
            color: #6C63FF;
        }
        .job-header {
            font-size: 1.1em;
            font-weight: bold;
            color: #009688;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            height: 3em;
            font-size: 1em;
        }
        .stTextInput > div > input {
            background-color: #f0f2f6;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Info
with st.sidebar:
    st.image("app/2.jpg", width=150)
    st.markdown("### 🤖 <span style='color:#6C63FF'>CraftChain Labs</span>", unsafe_allow_html=True)
    st.markdown("Crafting custom cold emails using AI + job data.")
    st.markdown("---")
    st.markdown("🔗 [GitHub](https://github.com/your-repo)  \n📧 Contact: hello@craftchainlabs.com")

# Main Title
st.markdown("<div class='title'>📧 Cold Email Generator</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Paste a job/careers page URL to generate a tailored AI-crafted cold email</div>", unsafe_allow_html=True)

# Input Section
st.markdown("### 🔍 Job Details")
url_input = st.text_input("🔗 Enter job or careers page URL", value="https://careers.nike.com/lead-data-scientist/job/R-62512")
custom_filter = st.text_input("🧠 Optional filters (comma-separated keywords)", placeholder="e.g., data scientist, senior, backend")
submit_button = st.button("🚀 Generate Cold Emails")

# Instantiate chain and portfolio only once
chain = Chain()
portfolio = Portfolio()

# On submit
if submit_button and url_input:
    try:
        with st.spinner("🔄 Scraping and analyzing the careers page..."):
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = chain.extract_jobs(data)

        if not jobs:
            st.warning("⚠️ No jobs found on this page. Try another URL.")
        else:
            filters = [f.strip().lower() for f in custom_filter.split(",") if f.strip()]
            for i, job in enumerate(jobs):
                role = job.get("role", "Unknown Role")
                skills = job.get("skills", [])
                experience = job.get("experience", "")
                description = job.get("description", "")

                if filters and not any(f in role.lower() or f in description.lower() for f in filters):
                    continue

                with st.expander(f"📌 Job #{i+1}: {role}", expanded=False):
                    st.markdown(f"<div class='job-header'>🧑‍💼 Experience:</div> {experience}", unsafe_allow_html=True)
                    st.markdown(f"<div class='job-header'>💼 Skills:</div> {', '.join(skills)}", unsafe_allow_html=True)
                    st.markdown(f"<div class='job-header'>📝 Description:</div> {description[:300]}...", unsafe_allow_html=True)

                    with st.spinner("✍️ Generating cold email..."):
                        links = portfolio.query_links(skills)
                        email = chain.write_mail(job, links)

                    st.markdown("#### 📧 Generated Email:")
                    st.code(email, language='markdown')

    except Exception as e:
        st.error(f"❌ An unexpected error occurred:\n\n`{e}`")
