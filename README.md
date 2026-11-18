# 🤖 NexBot AI — Your Personal Python Chatbot

A modern, ChatGPT-inspired chatbot built entirely with Python and Streamlit.

**Simple. Interactive. Intelligent. Customizable.**

---

## ✨ Overview

NexBot AI is a lightweight, interactive chatbot application developed entirely in Python.

Inspired by modern AI conversational platforms such as ChatGPT, NexBot combines a beautiful dark-mode interface with a custom-built conversational engine.

Unlike traditional chatbot projects that require multiple frontend files, databases, or complicated configurations, NexBot keeps everything inside a single Python file.

It uses text similarity algorithms, predefined knowledge, session-based memory, and a custom learning mechanism to create an interactive chatbot experience.

## 🎨 Features

- **Modern UI:** Beautiful dark-themed interface inspired by ChatGPT.
- **Conversational AI:** Understands and responds to basic natural-language messages.
- **Smart Matching:** Uses Jaccard similarity and SequenceMatcher to identify user intentions.
- **Conversation History:** Create and switch between multiple conversations.
- **Session Memory:** Remembers your name and personal information during the session.
- **Custom Learning:** Teach NexBot new questions and answers.
- **Quick Suggestions:** Start conversations with predefined prompts.
- **Dynamic Responses:** Provides current date and time.
- **Single-File Architecture:** The entire application is implemented in one Python file.
- **Lightweight:** No external AI APIs, databases, or downloaded language models required.

## 🖥️ Interface

NexBot features a modern conversational interface with:

- Dark charcoal background.
- Purple accent colors.
- Sidebar navigation.
- Individual conversation history.
- Chat-style message bubbles.
- Interactive learning panel.
- Responsive browser-based layout.

## 📸 Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/73bddd54-6862-4151-ae09-fd630bc48af5" width="49%" alt="NexBot AI - Chat Interface" />
  <img src="https://github.com/user-attachments/assets/b7ae5318-9721-4102-b519-7a61be76ecc5" width="49%" alt="NexBot AI - Application Preview" />
</p>

<p align="center">
  <em>A closer look at NexBot AI's interface and features.</em>
</p>


## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Regular Expressions | Text processing |
| Difflib | Text similarity matching |
| Random | Response selection |
| Datetime | Date and time handling |

## 📂 Project Structure

```text
NexBot-AI/
│
├── nexbot.py       # Complete application
└── README.md       # Project documentation
```

Everything is handled inside `nexbot.py`.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/NexBot-AI.git
```

### 2. Navigate to the project directory

```bash
cd NexBot-AI
```

### 3. Install dependencies

```bash
pip install streamlit
```

### 4. Run NexBot

```bash
streamlit run nexbot.py
```

### 5. Open the application

Visit:

```text
http://localhost:8501
```

That's it! NexBot is ready to chat.

## 💬 How to Use

### Basic Conversation

Try asking:

```text
Hello!
Who are you?
What is Artificial Intelligence?
Tell me about Python.
Motivate me.
```

### Personal Memory

NexBot can remember information during your session.

```text
My name is Alex.
```

Then ask:

```text
What is my name?
```

You can also teach NexBot personal information:

```text
Remember that I love programming.
```

### Teach NexBot

Use the **Teach NexBot** feature in the sidebar.

For example:

**Question:**
```text
What is Java?
```

**Answer:**
```text
Java is a popular object-oriented programming language.
```

NexBot can now respond to that question using your custom answer.

## 🧠 How Does the AI Work?

NexBot uses a lightweight text-matching engine rather than a pretrained generative language model.

Its response engine combines two techniques:

**1. Jaccard Similarity**

Measures the overlap between the words in two sentences.

**2. SequenceMatcher**

Compares textual sequences to estimate how similar two messages are.

The combined similarity score helps NexBot identify the closest matching intent.

The chatbot also includes:

- Intent classification.
- Predefined knowledge categories.
- Session-based user memory.
- Runtime knowledge customization.
- Context-independent response generation.

## ⚙️ Current Limitations

NexBot is an experimental lightweight chatbot, not a full-scale generative AI model.

- Responses are selected from predefined knowledge.
- It cannot generate arbitrary answers like ChatGPT.
- Memory is temporary and resets when the application session ends.
- Custom knowledge is not permanently stored.
- Internet access is only needed for the optional Google Fonts styling.

These limitations make NexBot a useful starting point for exploring NLP, text similarity, and chatbot development.

## 🔮 Future Improvements

Planned ideas for future versions:

- [ ] Integration with a local Large Language Model (LLM).
- [ ] Persistent conversation storage.
- [ ] Improved natural-language understanding.
- [ ] Context-aware conversations.
- [ ] User authentication.
- [ ] Voice input and speech output.
- [ ] Multilingual support.
- [ ] Advanced machine-learning-based intent classification.
- [ ] Export and import conversations.

## 🎯 Project Goals

This project was created to explore:

- Python application development.
- Natural Language Processing (NLP).
- Text similarity algorithms.
- Conversational systems.
- Session management.
- Interactive UI development using Streamlit.

## 🤝 Contributing

Suggestions, improvements, and contributions are welcome!

Feel free to fork the repository, experiment with the chatbot engine, and submit pull requests.

## 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute it according to the license terms.

---

**Built with ❤️ and Python.**

**NexBot AI — Your conversation. Your knowledge. Your AI.**
