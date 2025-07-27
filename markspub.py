import streamlit as st
import sys
import pandas as pd
import random
#from IPython.display import clear_output
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('MarksPub.csv')

df['Tally'] = 0

# Title
st.title("Welcome, Mark's Pub Friends!")
st.markdown("# ❓≈🕊🇮🇱")
# Puzzle prompt (always shown)
st.markdown(f"We've got {df.shape[0]} total different trivia questions.")

st.write("Select one or more options for the type of questions you want included:")

options = ["Discrete Facts", "Vocab Refreshers", "Summary Lists", 
           "Intersections", "Pavlovs", "Deep Cuts"]

# but only from the rows that we haven't seen yet
#filtereddf = df[df['Tally']== min(df['Tally'])]

selected = []
cols_per_row = 3

for i in range(0, len(options), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, option in enumerate(options[i:i+cols_per_row]):
        key = f"{option}_{i}_{j}"  # Make sure the key is unique
        if cols[j].checkbox(option, value=True, key=key):
            selected.append(option)

#try:
#    filtereddf = filtereddf[filtereddf['Type'].isin(selected)]    
#except NameError:
#    pass
        
# Sample word generator (replace with your own logic)
def generate_puzzle():
    # random choice 1
    # here's how we randomly select a noun/pronoun
    filtereddf = df[df['Type'].isin(selected)]  # First filter by category

    if filtereddf.empty:
    # fallback to full df or warn user
        st.warning("No rows match the selected categories.")
        st.stop()

    # Compute minimum Tally within the filtered set
    min_tally = filtereddf['Tally'].min()

    # Now filter again to just those with min Tally
    filtereddf = filtereddf[filtereddf['Tally'] == min_tally]

    if filtereddf.empty:
        st.warning("No rows with minimum Tally found in selected categories.")
        st.stop()

    # Choose one of those at random
    ourchoice = random.choice(filtereddf.index.tolist())

    # Update Tally in the original df
    df.at[ourchoice, 'Tally'] += 1

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
        "prompt": f"{pronoun} {beingverb} {df.iloc[ourchoice]['Question']}?",
        "answer": df.iloc[ourchoice]['Answer']
    }

# Initialize session state
if "puzzle" not in st.session_state:
    st.session_state.puzzle = generate_puzzle()
    st.session_state.show_answer = False

    
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
