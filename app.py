import random
import time
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="The Distance Jar 🫙✨", page_icon="🐒", layout="centered"
)

# --- Custom Styling & CSS ---
st.markdown(
    """
    <style>
    /* Warm, cozy background gradient */
    .stApp {
        background: linear-gradient(135deg, #fef6e4 0%, #f3d250 100%);
        background-attachment: fixed;
    }
    
    /* Header styling */
    .main-title {
        text-align: center;
        color: #1b263b;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }
    
    .subtitle {
        text-align: center;
        color: #415a77;
        font-size: 1.1em;
        margin-bottom: 30px;
    }

    /* Note Display Card */
    .note-card {
        background: #ffffff;
        color: #2b2d42;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        border-left: 8px solid #fb8500;
        margin-top: 25px;
        animation: fadeIn 0.5s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Custom styling for Streamlit buttons acting as jar icons */
    .stButton>button {
        width: 100%;
        border-radius: 16px;
        height: 4.5em;
        font-weight: bold;
        font-size: 1rem;
        background-color: #ffffff;
        color: #1b263b;
        border: 2px dashed #fb8500;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #fb8500;
        color: white;
        border: 2px solid #fb8500;
        transform: translateY(-3px);
        box-shadow: 0 6px 16px rgba(251,133,0,0.3);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- Personalized Notes Database ---
NOTES_DB = {
    "😄 Happy & Monkeying Around": [
        "Yay! Seeing you win makes your favorite Laddu's day 10x better. Remember our laughs from '25? Let's celebrate over video call tonight!",
        "Capture this exact feeling, Monkey! Bangalore is lucky to have your energy. Don't forget to treat yourself today!",
        "Look at you shining! Keep that smile on—I'm cheering for you all the way from here.",
    ],
    "🥺 Missing Your Laddu": [
        "Hey Monkey, remember that distance is just a number. We've got through so much together since 2024, and that bond isn't going anywhere.",
        "Close your eyes for 5 seconds and take a deep breath. Even if we're miles apart, your Laddu is just a phone call or text away anytime.",
        "Miss you too! Pull up our old photo gallery—instant mood lifter guaranteed. We'll reunite soon!",
    ],
    "🌪️ Stressed / Overwhelmed": [
        "Take a deep breath, Monkey. You are way stronger than whatever is stressing you out right now. Tackle it one step at a time.",
        "Step away from the screen for 5 minutes, grab a cup of chai, and stretch. Your Laddu believes in you completely!",
        "Remember when things felt chaotic back in 2025? You crushed it then, and you're going to crush this too.",
    ],
    "😂 Need a Good Laugh": [
        "Remember our absolute disaster of an outing? Honestly, looking back, we are total chaos together. Classic Monkey behavior. 😂",
        "If you're feeling bored in Bangalore right now, just imagine me narrating your day in a dramatic movie trailer voice.",
        "Fun fact: You are legally obligated to smile after reading this note. Those are the rules of our friendship contract!",
    ],
    "🕰️ Core Memories": [
        "Thinking about how close we got in 2025... best plot twist ever. So glad our paths crossed.",
        "Remember all those random late-night talks? Even with the new city and time zones, some things never change.",
        "Just a reminder that you're stuck with your Laddu for life, no matter how many pin codes change. Cheers to our 2024–forever journey! 🥂",
    ],
}

# --- App Header ---
st.markdown(
    "<h1 class='main-title'>🫙 The Distance Jar 🐒💛🥏</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='subtitle'>Pick a jar capsule below whenever you need a piece of home!</p>",
    unsafe_allow_html=True,
)

st.write("---")

# Initialize session state to track the active selected note
if "selected_note" not in st.session_state:
    st.session_state.selected_note = None
if "active_mood" not in st.session_state:
    st.session_state.active_mood = None

# --- Spread Out Icon Grid (2 rows) ---
st.markdown("### ✨ Tap a jar to open:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🐒\nHappy"):
        st.session_state.active_mood = "😄 Happy & Monkeying Around"
        st.session_state.selected_note = random.choice(
            NOTES_DB[st.session_state.active_mood]
        )

with col2:
    if st.button("🥺\nMiss You"):
        st.session_state.active_mood = "🥺 Missing Your Laddu"
        st.session_state.selected_note = random.choice(
            NOTES_DB[st.session_state.active_mood]
        )

with col3:
    if st.button("🌪️\nStressed"):
        st.session_state.active_mood = "🌪️ Stressed / Overwhelmed"
        st.session_state.selected_note = random.choice(
            NOTES_DB[st.session_state.active_mood]
        )

col4, col5 = st.columns(2)

with col4:
    if st.button("😂\nNeed a Laugh"):
        st.session_state.active_mood = "😂 Need a Good Laugh"
        st.session_state.selected_note = random.choice(
            NOTES_DB[st.session_state.active_mood]
        )

with col5:
    if st.button("🕰️\nMemories"):
        st.session_state.active_mood = "🕰️ Core Memories"
        st.session_state.selected_note = random.choice(
            NOTES_DB[st.session_state.active_mood]
        )

# --- Display Note if a Jar was Clicked ---
if st.session_state.selected_note:
    st.markdown(
        f"""
        <div class="note-card">
            <h4 style="color: #fb8500; margin-top: 0; margin-bottom: 12px;">💌 Note from your Laddu ({st.session_state.active_mood}):</h4>
            <p style="font-size: 1.15em; line-height: 1.6; margin: 0;">{st.session_state.selected_note}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.balloons()

# --- Footer ---
st.write("\n\n")
st.markdown(
    "<p style='text-align: center; color: #6c757d; font-size: 0.85em;'>Made with 💛 and endless support for my favorite Monkey in Bangalore.</p>",
    unsafe_allow_html=True,
)
