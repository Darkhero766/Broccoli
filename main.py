import streamlit as st
import random

stage = "home"

if "stage" not in st.session_state:
    st.session_state.stage = "home"

def main():
    st.title("Master Quiz")
    st.header("Get your own random quiz here ")
    st.write(" ")
    st.write(" ")
    if st.button("Get Quiz Now"):
        st.session_state.stage = "random"

def random():
    quizzes = [
        "python",
        "Science",
        "History"
    ]

    random_quiz = random.choice(quizzes)
    st.session_state.stage = random_quiz

def python():
    st.header("Who is the inventor of Python Language")
    st.write(" ")
    st.write(" ")
    correct_answer = "Guido van Rossum"
    if st.button("1. Larry Wall"):
        if "Larry Wall" == correct_answer:
            st.success(" 🟢 Correct Answer")
        else: 
            st.error(" ❌ Wrong Answer")
    st.write(" ")
    if st.button("2. Harry Goshling"):
        if "Harry Goshling" == correct_answer:
            st.success("☑️ Correct Answer ")
        else:
            st.error("❌ Wrong Answer")
    st.write(" ")
    if st.button("Guido van Rossum"):
        if "Guido van Rossum" == correct_answer:
            st.success("☑️ Correct Answer Bravo!!!")
        else:
            st.error("❌Wrong answer blehhh")
    st.write(" ")

    if st.button("faizal "):
        if "faizal" == correct_answer:
            st.success("☑️Correct answer bravo")
        else:
            st.error("❌Wrong answer blehh")
    

def science():
    pass

def history():
    pass

main()