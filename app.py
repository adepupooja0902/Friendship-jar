import random
import time
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="The Distance Jar ✨", page_icon="🫙", layout="centered"
)

# --- Custom Styling & CSS ---
st.markdown(
    """
    <style>
    .main {
        background-color: #faf7f2;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        font-weight: bold;
        background-color: #ff6b6b;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff5252;
        transform: scale(1.02);
    }
    .note-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        border-left: 6px solid #ff6b6b;
        margin-top: 20px;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .jar-title {
        text-align: center;
        color: #2c3e50;
        font-family: 'Georgia', serif;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- Personalized Notes Database ---
# Feel free to add, edit, or swap these out with your own inside jokes and memories!
NOTES_DB = {
    "😄 When you're super happy": [
        "Yay! Seeing you win makes my day 10x better. Remember that dinner we had back in '25? Let's celebrate over a video call tonight!",
        "Capture this exact feeling! You deserve all the good things coming your way in Bangalore. Don't forget to treat yourself today!",
        "Look at you shining! Bangalore is lucky to have you. Keep that smile on—I'm cheering for you all the way from here.",
    ],
    "🥺 When you miss me / Feel lonely": [
        "Hey, remember that distance is just a number. We've got through so much together since 2024, and that bond isn't going anywhere.",
        "Close your eyes for 5 seconds and take a deep breath. Even if we're miles apart, I'm just a phone call or text away anytime, always.",
        "Miss you too, bestie. Pull up our old photo gallery—instant mood lifter guaranteed. We'll reunite soon!",
    ],
    "🌪️ When work/life gets overwhelming": [
        "Take a deep breath. You are way stronger than whatever is stressing you out right now. Tackle it one small step at a time.",
        "Step away from the screen for 5 minutes, grab a cup of chai/coffee, and stretch. You've survived 100% of your hardest days so far.",
        "Remember when things felt chaotic before? You crushed it then, and you're going to crush this too. I believe in you completely.",
    ],
    "😂 When you need a good laugh": [
        "Remember our absolute disaster of an outing? Honestly, looking back, we are total chaos together. 😂",
        "If you're feeling bored in Bangalore traffic right now, just imagine me narrating your day in a dramatic movie trailer voice.",
        "Fun fact: You are legally obligated to smile after reading this note. Those are the rules of our friendship contract.",
    ],
    "🕰️ Random Core Memories": [
        "Thinking about how close we got in 2025... best plot twist ever. So glad our paths crossed.",
        "Remember all those random late-night talks? Even with the new city and time zones, some things never change.",
        "Just a reminder that you're stuck with me for life, no matter how many pin codes change. Cheers to our 2024–forever journey! 🥂",
    ],
}

# --- App Header ---
st.markdown(
    "<h1 class='jar-title'>🫙 The Distance Jar</h1>", unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; color: #7f8c8d; font-size: 1.1em;'>A little piece of home and friendship, no matter how many miles apart we are.</p>",
    unsafe_allow_html=True,
)

st.write("---")

# --- Mood Selection ---
st.markdown(
    "### ✨ How are you feeling today? Pick a jar capsule to open:"
)

# Using columns for a cleaner layout of mood categories
mood_categories = list(NOTES_DB.keys())
selected_mood = st.selectbox(
    "Choose your current vibe:",
    mood_categories,
    label_visibility="collapsed",
)

st.write("")

# --- Interaction Logic ---
if st.button("🔮 Open a Note from the Jar"):
    # Fun interactive suspense loading simulation
    with st.spinner("Unfolding a folded paper note from the jar..."):
        time.sleep(1.2)  # slight dramatic pause

    # Pick a random note from the chosen category
    chosen_note = random.choice(NOTES_DB[selected_mood])

    # Display the note inside a styled card container
    st.markdown(
        f"""
        <div class="note-card">
            <h4 style="color: #ff6b6b; margin-top: 0;">💌 A note for you:</h4>
            <p style="font-size: 1.15em; color: #333333; line-height: 1.6;">{chosen_note}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Celebration effect
    st.balloons()

# --- Footer ---
st.write("\n\n")
st.markdown(
    "<p style='text-align: center; color: #bdc3c7; font-size: 0.85em;'>Made with ❤️ for my favorite person in Bangalore.</p>",
    unsafe_allow_html=True,
)
