# 📧 Intelligent Email Assistant

An AI-powered customer support email assistant developed as part of **24CS2506 – Building Applications using GPT-4**.

The application analyzes customer emails, detects customer intent, retrieves similar historical conversations, generates context-aware professional replies, improves the tone of responses, summarizes customer issues, and saves generated replies for future reference.

## 🚀 Features

- 🎯 Customer Intent Detection
- 🔍 Similar Email Retrieval
- 🤖 AI-Powered Reply Generation
- 🎨 Tone Improvement
  - Friendly
  - Formal
  - Empathetic
- 📝 Conversation Summarization
- 💾 Automatic Reply Saving
- 📊 Interactive Streamlit Dashboard
- 📚 Historical Email Dataset Integration

## 🧠 How It Works

The application follows the workflow:

Customer Email  
→ Intent Detection  
→ Similar Email Retrieval  
→ AI Reply Generation  
→ Tone Improvement  
→ Conversation Summary  
→ Save Final Reply

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Large Language Models (LLMs)
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## 📁 Project Structure

```text
EmailAssistant/
│
├── data/
│   └── emails.csv
│
├── outputs/
│   └── generated_reply.txt
│
├── app.py
├── main.py
├── intent_module.py
├── retrieval_module.py
├── reply_module.py
├── tone_module.py
├── summary_module.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md