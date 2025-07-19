import streamlit as st
import sys
import pandas as pd
import random
#from IPython.display import clear_output
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('MarksPub.csv')

vocabdf = df[df['Type'].isin(['Vocab'])]
factsdf = df[df['Type'].isin(['Fact'])]

# Sample word generator (replace with your own logic)
def generate_puzzle():
    # random choice 1
    # here's how we randomly select a noun/pronoun
    ourchoice = random.choice(range(df.shape[0]))

    if df.iloc[ourchoice, 4] == 'Singular':
        beingverb = 'is'
    else: 
        beingverb = 'are'
    
    return {
        "prompt": f"What {beingverb} {df.iloc[ourchoice, 2]}?",
        "answer": df.iloc[ourchoice, 3]
    }


# Initialize session state
if "puzzle" not in st.session_state:
    st.session_state.puzzle = generate_puzzle()
    st.session_state.show_answer = False

# Title
st.title("Welcome, Mark's Pub Friends!")

st.markdown("# ❓≈🕊️")

# Puzzle prompt (always shown)
st.markdown(f"🔍 **Question:** {st.session_state.puzzle['prompt']}")

# Answer area
answer_placeholder = st.empty()

if st.session_state.show_answer:
    answer_placeholder.markdown(f"✅ **Answer:** {st.session_state.puzzle['answer']}")
else:
    # Reserve space for layout consistency
    answer_placeholder.markdown("<div style='height: 42px'></div>", unsafe_allow_html=True)

# Button logic — single click toggles state correctly
button_clicked = st.button("Next trivium please")

if button_clicked:
    if st.session_state.show_answer:
        # Go to next puzzle
        st.session_state.puzzle = generate_puzzle()
        st.session_state.show_answer = False
    else:
        # Reveal the answer
        st.session_state.show_answer = True

st.markdown("---")  # Optional horizontal rule

st.markdown("ℹ️ You may need to double-click the button the first time. If you're on a computer, you should be able to use the enter/return key instead of the GUI (after clicking on it once).")
st.markdown("𓂀𓋹𓁈𓃠𓆃☥𓆣")
