import random
import time
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="The Distance Jar 🫙✨", page_icon="🐒", layout="centered"
)

# --- Custom Styling & CSS (Enhanced UI, Background, and Flip Cards) ---
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

    /* Flip Card Container */
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 220px;
        perspective: 1000px;
        margin-bottom: 20px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s;
        transform-style: preserve-3d;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
        border-radius: 20px;
    }

    /* Front of Card (The Jar / Mood Icon) */
    .flip-card-front {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        background: #ffffff;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 3px dashed #ffb703;
    }

    /* Back of Card (The Secret Note) */
    .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        background: #fff;
        color: #2b2d42;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 25px;
        transform: rotateY(180deg);
        border-left: 8px solid #fb8500;
        text-align: left;
    }
    
    /* Button overrides */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        font-weight: bold;
        background-color: #fb8500;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ffb703;
        color: #1b263b;
        transform: scale(1.02);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- Personalized Notes Database (Including "Monkey" & "Laddu" touches) ---
NOTES_DB = {
    "😄 When you're happy & monkeying around": [
        "Yay! Seeing you win makes your favorite Laddu's day 10x better. Remember our laughs from '25? Let's celebrate over video call tonight!",
        "Capture this exact feeling, Monkey! Bangalore is lucky to have your energy. Don't forget to treat yourself today!",
        "Look at you shining! Keep that smile on—I'm cheering for you all the way from here.",
    ],
    "🥺 When you miss your Laddu / Feel lonely": [
        "Hey Monkey, remember that distance is just a number. We've got through so much together since 2024, and that bond isn't going anywhere.",
        "Close your eyes for 5 seconds and take a deep breath. Even if we're miles apart, your Laddu is just a phone call or text away anytime.",
        "Miss you too! Pull up our old photo gallery—instant mood lifter guaranteed. We'll reunite soon!",
    ],
    "🌪️ When Bangalore traffic/work gets overwhelming": [
        "Take a deep breath, Monkey. You are way stronger than whatever is stressing you out right now. Tackle it one step at a time.",
        "Step away from the screen for 5 minutes, grab a cup of chai, and stretch. Your Laddu believes in you completely!",
        "Remember when things felt chaotic back in 2025? You crushed it then, and you're going to crush this too.",
    ],
    "😂 When you need a good laugh": [
        "Remember our absolute disaster of an outing? Honestly, looking back, we are total chaos together. Classic Monkey behavior. 😂",
        "If you're feeling bored in Bangalore right now, just imagine me narrating your day in a dramatic movie trailer voice.",
        "Fun fact: You are legally obligated to smile after reading this note. Those are the rules of our friendship contract!",
    ],
    "🕰️ Random Core Memories": [
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
    "<p class='subtitle'>A little piece of home, inside jokes, and Laddu-approved cheer, no matter how far Monkey goes.</p>",
    unsafe_allow_html=True,
)

st.write("---")

# --- Mood Selection with Icons ---
st.markdown("### ✨ Choose a jar capsule to open:")

# Emoji icons mapping for each mood category
mood_icons = {
    "😄 When you're happy & monkeying around": "🐒😄",
    "🥺 When you miss your Laddu / Feel lonely": "🥺🥏",
    "🌪️ When Bangalore traffic/work gets overwhelming": "🌪️💼",
    "😂 When you need a good laugh": "😂🍿",
    "🕰️ Random Core Memories": "🕰️✨",
}

selected_mood_display = st.selectbox(
    "How are you feeling?",
    list(mood_icons.keys()),
    format_func=lambda x: f"{mood_icons[x]}  {x}",
    label_visibility="collapsed",
)

st.write("")

# --- Interaction Logic (With Flip Effect Simulation) ---
if st.button("🔮 Open the Capsule"):
    with st.spinner("Unfolding a folded paper note from the jar..."):
        time.sleep(1.0)  # dramatic suspense pause

    # Pick a random note
    chosen_note = random.choice(NOTES_DB[selected_mood_display])

    # Render a simulated flip-card with CSS
    st.markdown(
        f"""
        <div class="flip-card">
            <div class="flip-card-inner" style="transform: rotateY(180deg);">
                <div class="flip-card-front">
                    <h3>Jar Open</h3>
                </div>
                <div class="flip-card-back">
                    <h4 style="color: #fb8500; margin-top: 0; margin-bottom: 10px;">💌 Note from your Laddu:</h4>
                    <p style="font-size: 1.1em; line-height: 1.5; margin: 0;">{chosen_note}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Celebration effect
    st.balloons()

# --- Footer ---
st.write("\n\n")
st.markdown(
    "<p style='text-align: center; color: #6c757d; font-size: 0.85em;'>Made with 💛 and endless support for my favorite Monkey in Bangalore.</p>",
    unsafe_allow_html=True,
)
