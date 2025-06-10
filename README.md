
# Cold Email Generator 

An AI-powered application that generates personalized cold emails by analyzing job postings and matching them with your company's portfolio. Built with **Streamlit** and powered by the **Groq LLM**.

---

## Features 

- **Job Analysis**: Automatically extracts key information from job posting URLs  
- **Portfolio Matching**: Aligns job requirements with relevant portfolio items  
- **Custom Filtering**: Filter job postings using user-defined keywords  
- **AI-Powered Emails**: Generates tailored cold emails using **Groq's LLaMA3** model  
- **Vector Search**: Efficient portfolio matching using **ChromaDB**

---

## Tech Stack 

- **Frontend**: Streamlit  
- **Language Model**: Groq (llama3-70b-8192)  
- **Vector Database**: ChromaDB  
- **Web Scraping**: LangChain WebBaseLoader  
- **Data Processing**: Pandas

---

## Setup 

1. **Clone the repository**  
   ```bash
   git clone https://github.com/i-am-batman-28/Cold-Email.git
   cd Cold-Email
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**  
   Create a `.env` file in the `app/` directory with the necessary API keys and configurations. Example:
   ```env
   GROQ_API_KEY=your_groq_api_key
   ```

4. **Run the application**  
   ```bash
   streamlit run app/main.py
   ```

---

## Usage 

1. Enter a **job or careers page URL** into the input field  
2. Optionally add **filter keywords** to refine results  
3. Click **"Generate Cold Emails"**  
4. View the extracted job details and the generated emails in the results section

---

## Project Structure 

```
Cold-Email/
├── app/
│   ├── main.py             # Main Streamlit application
│   ├── chains.py           # LLM chains for job extraction & email generation
│   ├── portfolio.py        # Portfolio management and vector matching
│   ├── utils.py            # Utility functions
│   └── resource/
│       └── my_portfolio.csv # Portfolio data file
├── vectorstore/            # ChromaDB vector data
├── requirements.txt
└── README.md
```

---

## Contributing 

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a Pull Request.

---

## License 

This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.

---

## Contact 

For questions, collaborations, or support, reach out to:  
**hello@craftchainlabs.com**
