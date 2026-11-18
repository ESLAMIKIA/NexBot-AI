
import streamlit as st
import random
import re
import time
from datetime import datetime
from difflib import SequenceMatcher


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="NexBot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #101014;
    color: #F4F4F5;
}

[data-testid="stSidebar"] {
    background: #17171C;
    border-right: 1px solid #292930;
}

[data-testid="stSidebar"] > div {
    padding-top: 25px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    max-width: 950px;
    padding-top: 35px;
    padding-bottom: 120px;
}

.brand {
    font-size: 28px;
    font-weight: 800;
    letter-spacing: -1px;
    color: white;
}

.brand span {
    color: #9B8CFF;
}

.brand-sub {
    color: #85858F;
    font-size: 12px;
    margin-top: 3px;
}

.sidebar-title {
    font-size: 11px;
    font-weight: 700;
    color: #777783;
    letter-spacing: 1.5px;
    margin-top: 35px;
    margin-bottom: 12px;
}

.hero {
    text-align: center;
    padding-top: 65px;
    padding-bottom: 35px;
}

.hero-icon {
    font-size: 48px;
    margin-bottom: 15px;
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -2px;
    color: #FFFFFF;
    margin-bottom: 10px;
}

.hero p {
    color: #90909C;
    font-size: 15px;
}

.message-user {
    display: flex;
    justify-content: flex-end;
    margin: 22px 0;
}

.message-user-content {
    background: #292933;
    border: 1px solid #383842;
    color: #F4F4F5;
    padding: 15px 19px;
    border-radius: 20px 20px 5px 20px;
    max-width: 78%;
    line-height: 1.7;
    overflow-wrap: anywhere;
}

.message-bot {
    display: flex;
    justify-content: flex-start;
    gap: 13px;
    margin: 25px 0;
}

.bot-avatar {
    min-width: 35px;
    height: 35px;
    background: linear-gradient(135deg, #8B7CFF, #5042B8);
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 18px;
}

.message-bot-content {
    color: #E7E7EB;
    line-height: 1.9;
    max-width: 85%;
    padding-top: 2px;
    overflow-wrap: anywhere;
}

.bot-name {
    font-size: 12px;
    font-weight: 700;
    color: #A99AFF;
    margin-bottom: 7px;
}

.stButton > button {
    border-radius: 12px;
    border: 1px solid #34343E;
    background: #202027;
    color: #F2F2F5;
    transition: all .2s ease;
}

.stButton > button:hover {
    border-color: #8C7AFF;
    color: white;
    background: #292735;
}

button[kind="primary"] {
    background: #7765E8 !important;
    border: none !important;
    color: white !important;
}

.stTextInput input, .stTextArea textarea {
    background: #202027 !important;
    color: white !important;
    border: 1px solid #383842 !important;
    border-radius: 12px !important;
}

.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #8877FF !important;
    box-shadow: 0 0 0 1px #8877FF !important;
}

[data-testid="stChatInput"] {
    border: 1px solid #393943;
    border-radius: 18px;
    background: #202027;
}

[data-testid="stChatInput"] textarea {
    color: white !important;
}

hr {
    border-color: #303039;
}

.feature-card {
    background: #1C1C24;
    border: 1px solid #30303A;
    border-radius: 15px;
    padding: 18px;
    min-height: 105px;
    margin-bottom: 10px;
}

.feature-card strong {
    color: #E9E5FF;
    font-size: 14px;
}

.feature-card p {
    color: #898994;
    font-size: 12px;
    margin-top: 7px;
}

.status {
    display: inline-block;
    background: #18372C;
    color: #66DDA8;
    border: 1px solid #285B46;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 11px;
}

div[data-testid="stChatMessage"] {
    background: transparent;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# AI ENGINE
# ==========================================

class NexBot:

    def __init__(self):

        self.knowledge = {

            "greeting": {
                "examples": [
                    "hello", "hi", "hey",
                    "good morning", "good evening"
                ],
                "responses": [
                    "Hello! Welcome back. What would you like to talk about?",
                    "Hey! Great to see you. How can I help?",
                    "Hi there! What's on your mind today?"
                ]
            },

            "identity": {
                "examples": [
                    "who are you",
                    "what is your name",
                    "tell me about yourself"
                ],
                "responses": [
                    "I'm NexBot, your personal AI assistant, built entirely with Python!",
                    "My name is NexBot. I'm here to help you explore ideas and learn new things."
                ]
            },

            "ai": {
                "examples": [
                    "what is artificial intelligence",
                    "what is ai",
                    "explain machine learning"
                ],
                "responses": [
                    "Artificial Intelligence is a field of computer science focused on building systems that perform tasks associated with human intelligence.",
                    "AI allows computers to recognize patterns, process information, and make predictions."
                ]
            },

            "python": {
                "examples": [
                    "what is python",
                    "tell me about python",
                    "why learn python"
                ],
                "responses": [
                    "Python is a versatile programming language used in AI, automation, backend development, and data science.",
                    "Python is popular because of its readable syntax and powerful ecosystem."
                ]
            },

            "technology": {
                "examples": [
                    "tell me about technology",
                    "what is technology",
                    "latest technology"
                ],
                "responses": [
                    "Technology helps us solve problems and build better tools. AI, robotics, cloud computing, and cybersecurity are important fields."
                ]
            },

            "motivation": {
                "examples": [
                    "motivate me",
                    "give me motivation",
                    "i feel lazy",
                    "inspire me"
                ],
                "responses": [
                    "Great things are built one small step at a time. Keep going!",
                    "You don't need to be perfect. You just need to keep improving.",
                    "Your future self will thank you for the work you do today."
                ]
            },

            "thanks": {
                "examples": [
                    "thank you",
                    "thanks",
                    "appreciate it"
                ],
                "responses": [
                    "You're very welcome!",
                    "Happy to help!",
                    "Anytime! That's what I'm here for."
                ]
            },

            "goodbye": {
                "examples": [
                    "goodbye",
                    "bye",
                    "see you later"
                ],
                "responses": [
                    "Goodbye! Have an amazing day.",
                    "See you soon!",
                    "Take care!"
                ]
            }
        }

    def normalize(self, text):

        return re.sub(
            r"[^\w\s]",
            "",
            text.lower()
        ).strip()

    def similarity(self, first, second):

        first_words = set(self.normalize(first).split())
        second_words = set(self.normalize(second).split())

        if not first_words or not second_words:
            return 0

        overlap = len(first_words & second_words)
        total = len(first_words | second_words)

        jaccard = overlap / total

        sequence = SequenceMatcher(
            None,
            self.normalize(first),
            self.normalize(second)
        ).ratio()

        return 0.65 * jaccard + 0.35 * sequence

    def respond(self, message, memory, learned):

        normalized = self.normalize(message)

        # Personal memory
        name = re.search(
            r"\bmy name is\s+([a-zA-Z]+)",
            message,
            re.IGNORECASE
        )

        if name:
            memory["name"] = name.group(1).capitalize()
            return f"Nice to meet you, {memory['name']}! I'll remember your name."

        if "what is my name" in normalized:
            return (
                f"Your name is {memory['name']}."
                if "name" in memory
                else "You haven't told me your name yet."
            )

        remember = re.search(
            r"\bremember that\s+(.+)",
            message,
            re.IGNORECASE
        )

        if remember:
            fact = remember.group(1)
            memory.setdefault("facts", []).append(fact)
            return f"I'll remember that: {fact}"

        if "what do you remember" in normalized:
            facts = memory.get("facts", [])

            result = []

            if "name" in memory:
                result.append(f"Your name is {memory['name']}.")

            if facts:
                result.append("You asked me to remember: " + ", ".join(facts))

            return " ".join(result) if result else "I haven't stored anything yet."

        # Learned answers
        if normalized in learned:
            return learned[normalized]

        # Dynamic time and date
        if "time" in normalized and any(
            word in normalized for word in ["what", "tell", "current"]
        ):
            return "The current time is " + datetime.now().strftime("%H:%M:%S")

        if "date" in normalized and any(
            word in normalized for word in ["what", "tell", "today"]
        ):
            return "Today's date is " + datetime.now().strftime("%B %d, %Y")

        # Find matching intent
        best_score = 0
        best_intent = None

        for intent, data in self.knowledge.items():

            for example in data["examples"]:

                score = self.similarity(message, example)

                if score > best_score:
                    best_score = score
                    best_intent = intent

        if best_intent and best_score >= 0.48:

            return random.choice(
                self.knowledge[best_intent]["responses"]
            )

        return (
            "That's an interesting question! I don't have a good answer "
            "for it yet. You can teach me a response using the Learn feature."
        )


# ==========================================
# SESSION STATE
# ==========================================

if "bot" not in st.session_state:
    st.session_state.bot = NexBot()

if "chats" not in st.session_state:
    st.session_state.chats = {}

if "active_chat" not in st.session_state:
    st.session_state.active_chat = None

if "memory" not in st.session_state:
    st.session_state.memory = {}

if "learned" not in st.session_state:
    st.session_state.learned = {}

if "chat_counter" not in st.session_state:
    st.session_state.chat_counter = 0

if "show_learn" not in st.session_state:
    st.session_state.show_learn = False


# ==========================================
# CHAT MANAGEMENT
# ==========================================

def new_chat():

    st.session_state.chat_counter += 1

    chat_id = st.session_state.chat_counter

    st.session_state.chats[chat_id] = {
        "title": "New Conversation",
        "messages": []
    }

    st.session_state.active_chat = chat_id


def get_active_chat():

    chat_id = st.session_state.active_chat

    if chat_id is None:
        new_chat()
        chat_id = st.session_state.active_chat

    return st.session_state.chats[chat_id]


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("""
    <div class="brand">NEX<span>BOT</span> ✦</div>
    <div class="brand-sub">YOUR PERSONAL AI ASSISTANT</div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("＋  New Chat", use_container_width=True, type="primary"):
        new_chat()
        st.rerun()

    st.markdown(
        '<div class="sidebar-title">YOUR CONVERSATIONS</div>',
        unsafe_allow_html=True
    )

    if st.session_state.chats:

        for chat_id, chat in reversed(
            list(st.session_state.chats.items())
        ):

            title = chat["title"][:25]

            if st.button(
                "▤  " + title,
                key=f"chat_{chat_id}",
                use_container_width=True
            ):

                st.session_state.active_chat = chat_id
                st.rerun()

    else:

        st.caption("Your conversations will appear here.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    st.markdown(
        '<div class="sidebar-title">TOOLS</div>',
        unsafe_allow_html=True
    )

    if st.button("🧠  Teach NexBot", use_container_width=True):
        st.session_state.show_learn = not st.session_state.show_learn

    if st.button("🗑️  Clear Current Chat", use_container_width=True):

        if st.session_state.active_chat is not None:
            st.session_state.chats[
                st.session_state.active_chat
            ]["messages"] = []

            st.session_state.chats[
                st.session_state.active_chat
            ]["title"] = "New Conversation"

        st.rerun()

    st.divider()

    st.markdown("""
    <div style="padding:10px 0;">
        <div style="display:flex;align-items:center;gap:9px;">
            <div style="font-size:28px;">🤖</div>
            <div>
                <div style="font-weight:700;color:white;">NexBot AI</div>
                <div style="font-size:11px;color:#888;">Python Edition</div>
            </div>
        </div>
        <br>
        <span class="status">● Online</span>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# MAIN CONTENT
# ==========================================

chat = get_active_chat()

st.markdown("""
<div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
    border-bottom:1px solid #303039;
    padding-bottom:18px;
">
    <div style="font-size:15px;font-weight:700;">
        NexBot <span style="color:#999;font-weight:400;">/ AI Assistant</span>
    </div>
    <div style="font-size:12px;color:#85858F;">
        Python-powered
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# WELCOME SCREEN
# ==========================================

if not chat["messages"]:

    st.markdown("""
    <div class="hero">
        <div class="hero-icon">✦</div>
        <h1>How can I help you?</h1>
        <p>Ask me anything. Let's explore something interesting together.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    suggestions = [
        ("💡", "Explain Artificial Intelligence", "What is artificial intelligence?"),
        ("🐍", "Learn Python", "Tell me about Python"),
        ("🚀", "Get motivated", "Motivate me"),
        ("🤖", "Meet NexBot", "Who are you?")
    ]

    for index, (emoji, title, prompt) in enumerate(suggestions):

        with [col1, col2][index % 2]:

            if st.button(
                f"{emoji}  {title}  →",
                key=f"suggestion_{index}",
                use_container_width=True
            ):

                chat["messages"].append({
                    "role": "user",
                    "content": prompt
                })

                answer = st.session_state.bot.respond(
                    prompt,
                    st.session_state.memory,
                    st.session_state.learned
                )

                chat["messages"].append({
                    "role": "assistant",
                    "content": answer
                })

                if chat["title"] == "New Conversation":
                    chat["title"] = prompt[:25]

                st.rerun()


# ==========================================
# CHAT HISTORY DISPLAY
# ==========================================

for message in chat["messages"]:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="message-user">
                <div class="message-user-content">
                    {message["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="message-bot">
                <div class="bot-avatar">✦</div>
                <div class="message-bot-content">
                    <div class="bot-name">NEXBOT</div>
                    {message["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==========================================
# LEARNING PANEL
# ==========================================

if st.session_state.show_learn:

    st.divider()

    st.subheader("🧠 Teach NexBot")

    st.caption(
        "Create a question and teach NexBot its answer. "
        "It will remember it during this session."
    )

    with st.form("learning_form"):

        question = st.text_input(
            "Question",
            placeholder="What is Java?"
        )

        answer = st.text_area(
            "Answer",
            placeholder="Java is a programming language."
        )

        submitted = st.form_submit_button(
            "Save Knowledge",
            use_container_width=True
        )

        if submitted:

            if question.strip() and answer.strip():

                st.session_state.learned[
                    st.session_state.bot.normalize(question)
                ] = answer

                st.success("NexBot has learned something new!")

            else:

                st.warning("Please fill in both fields.")


# ==========================================
# CHAT INPUT
# ==========================================

user_message = st.chat_input(
    "Message NexBot..."
)

if user_message:

    chat["messages"].append({
        "role": "user",
        "content": user_message
    })

    if chat["title"] == "New Conversation":
        chat["title"] = user_message[:25]

    with st.spinner("NexBot is thinking..."):

        time.sleep(0.5)

        response = st.session_state.bot.respond(
            user_message,
            st.session_state.memory,
            st.session_state.learned
        )

    chat["messages"].append({
        "role": "assistant",
        "content": response
    })

    st.rerun()


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div style="
    text-align:center;
    color:#666672;
    font-size:11px;
    padding:30px 0 0 0;
">
    NexBot AI · Built with Python and Streamlit
    <br><br>
    AI can make mistakes. Always verify important information.
</div>
""", unsafe_allow_html=True)
