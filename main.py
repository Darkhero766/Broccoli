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
    st.write(" ")
    st.write(" ")


    st.write(" ")

    if st.button("Next Question"):
        st.session_state.stage = "python1"

def python1():
    st.header("Q.2 : In which year python lanuguage was created ?")
    correct_answer = "1989"

    if st.button("1989"):
        if "1989" == correct_answer:
            st.success("👍Correct Answer")
        else:
            st.error("❌Wrong Answer")
    st.write(" ")
    st.write(" ")

    if st.button("1957"):
        if "1957" == correct_answer:
            st.success("👍 Correct Answer!!!")
        else :
            st.error("❌Wrong Answer ")
    st.write(" ")

    st.write(" ")

    if st.button("1999"):
        if "1999" == correct_answer:
            st.success("👍 Correct Answer")
        else:
            st.error("❌Wrong Answer")

    if st.button("1978"):
        if "1978" == correct_answer:
            st.success("👍 Correct Answer")
        else: 
            st.error("❌ Wrong Answer")

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("⏭️ Next Question "):
        st.session_state.stage = "python2"

def python2():
    st.header("Q.3 Which of the following data type is mutable in python ? ")
    
    correct_answer = "List"

    if st.button("Tupple"):
        if "Tupple" == correct_answer:
            st.success("✅Correct Answer....")

        else:
            st.error("❌Wrong Answer")

    st.write(" ")

    if st.button("2. Integer"):
        if "Integer" == correct_answer:
            st.success("✅ Correct Answer..")
        else:
            st.error("❌Wrong Answer ")
    
    st.write(" ")

    if st.button("3. Arrays"):
        if "Arrays" == correct_answer:
            st.success("✅ Correct Answer")
        else:
            st.error("❌Wrong Answer....")

    if st.button("4. List"):
        if "List" == correct_answer:
            st.success("✅ Correct Answer")
        else:
            st.error("❌ Wrong Answer")
    
    st.write(" ")
    st.write(" ")

    st.write(" ")

    if st.button(" You did it . Return to menu..........."):
        st.session_state.stage = "main"
        


def science():
    st.header("Select The Difficulty ")
    st.write(" ")

    st.write(" ")

    if st.button("Easy"):
        st.session_state.stage = "easy"
    st.write(" ")

    if st.button("Intermediate."):
        st.session_state.stage = "int"
    
    st.write(" ")

    if st.button("Hard"):
        st.session_state.stage = "hard":
        
    
def easy():
    st.header("Q.1 Why does Induction cooktop heat the pan but cool to touch Why ?")
    correct_answer = "Electromagnetism"

    st.write(" ")
    st.write(" ")
    
    

def history():
    pass

main()