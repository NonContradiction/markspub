import streamlit as st
import sys
import pandas as pd
import random
#from IPython.display import clear_output
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('MarksPub.csv')
df['Tally'] = 0

vocabdf = df[df['Type'].isin(['Vocab'])]
factsdf = df[df['Type'].isin(['Fact'])]

# Sample word generator (replace with your own logic)
def generate_puzzle():
    # random choice 1
    # here's how we randomly select a noun/pronoun
    # but only from the rows that we haven't seen yet
    filtereddf = df[df['Tally']== min(df['Tally'])]
    ourchoice = random.choice(filtereddf.index.tolist())

    if df.iloc[ourchoice]['Number'] == 'Singular':
        beingverb = 'is'
    else: 
        beingverb = 'are'

    if df.iloc[ourchoice]['Personal'] == 'No':
        pronoun = 'What'
    else: 
        pronoun = 'Who'

    df.iloc[ourchoice]['Tally'] += 1
    
    return {
        # TROUBLESHOOTING
        #"troubleshooting": f"{df.iloc[ourchoice, 5]}?",
        "prompt": f"{pronoun} {beingverb} {df.iloc[ourchoice]['Question']}?",
        "answer": df.iloc[ourchoice]['Answer']
    }


# Initialize session state
if "puzzle" not in st.session_state:
    st.session_state.puzzle = generate_puzzle()
    st.session_state.show_answer = False

# Title
st.title("Welcome, Mark's Pub Friends!")

st.markdown("# ❓≈🕊🇮🇱")

# Puzzle prompt (always shown)
st.markdown(f"We've got {df.shape[0]} total different trivia questions.")

st.write("Select one or more options for the type of questions you want included:")

option_a = st.checkbox("Discrete Facts")
option_b = st.checkbox("Vocab Refreshers")
option_c = st.checkbox("Summary Lists")
option_d = st.checkbox("Intersections")
option_e = st.checkbox("Pavlovs")
option_f = st.checkbox("Deep Cuts")

selected = []
if option_a: selected.append("Option A")
if option_b: selected.append("Option B")
if option_c: selected.append("Option C")
if option_d: selected.append("Option D")
if option_e: selected.append("Option E")
if option_f: selected.append("Option F")

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
