import streamlit as st
import random

stage = "main"

if "stage" not in st.session_state:
    st.session_state.stage = "main"

def main():
    st.title("Master Quiz")
    st.header("Get your own random quiz here ")
    st.write(" ")
    st.write(" ")
    if st.button("Get Quiz Now"):
        st.session_state.stage = "random"

def random():
    st.header("Select the quiz to continue. ")
    quizzes = [
        "python",
        "Science",
        "History"
    ]

    st.write(" ")
    st.write(" ")

    if st.button("1. Python"):
        st.session_state.stage = "python"
    st.write(" ")

    if st.button("2. History"):
        st.session_state.stage = "history"

    st.write(" ")

    if st.button("3. Science"):
        st.session_state.stage = "science"

    



    

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

    if st.button("1957"):
        if "1957" == correct_answer:
            st.success("👍 Correct Answer!!!")
        else :
            st.error("❌Wrong Answer ")
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
    st.write(" ")

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
        st.session_state.stage = "hard"

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("Return to Mian Menu"):
        st.session_state.stage = "main"
        
    
def easy():
    st.header("Q.1 Why does Induction cooktop heat the pan but cool to touch Why ?")
    correct_answer = "Electromagnetism"

    st.write(" ")
    st.write(" ")

    if st.button("1. Induction "):
        if "Indcution" == correct_answer:
            st.success("✅ Correct Answer")

        else:
            st.error("❌Beeeep Wrong Answer")
        
    st.write(" ")

    if st.button("2. Electromagnetism"):
        if "Electromagnetism" == correct_answer:
            st.success("✅ Correct Answer...")
        
        else :
            st.error("❌Beeeep Wrong Answer")

    st.write(" ")

    if st.button("3. Infrared"):
        if "Infrared" == correct_answer:
            st.success("✅ Correct Answer")
        else: 
            st.error("❌ Microwave")

    st.write(" ")

    if st.button("4. Microwave"):
        if "Microwave" == correct_answer:
            st.success("✅ Correct Answer")
        
        else:
            st.error("❌ Wrong answer ")
            
    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("⏭️ Next Question......"):
        st.session_state.stage = "easy1"

    

def easy1():
    st.header("Q.2 What is the active ingredient in household bleach to kills bacteria?")
    correct_answer = "Hypochlorite"

    st.write(" ")
    st.write(" ")

    if st.button("1. Hypochlorite "):
        if "Hypochlorite" == correct_answer:
            st.success("✅ Correct Answer")
        else:
            st.error("❌Beeep Wrong One.......")

    st.write(" ")

    if st.button("2. Chloride"):
        if "Chloride" == correct_answer:
            st.success("✅ Correct Answer")

        else:
            st.error("❌ Wrong One beeeeeep")

    st.write(" ")

    if st.button("3. Bicarbonate"):
        if "Bicarbonate" == correct_answer:
            st.success("✅ Correct Answer")

        else:
            st.error("❌Beeeep Wrong One")

    st.write(" ")

    if st.button("4. Acetate "):
        if "Acetate" == correct_answer:
            st.success("✅ Correct Answer")

        else:
            st.error("❌Wrong One")

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("⏭️ Next Question "):
        st.session_state.stage = "easy2"

    

def easy2():
    st.header("Q.3 Why LED bulbs use lesser Energy than old Incandescent bulbs?")

    correct_answer = "Electroluminescence"

    st.write(" ")
    st.write(" ")

    if st.button("1. Incandescence"):
        if "Incandescence" == correct_answer:
            st.success("✅ Correct Answer")
        
        else:
            st.error("❌ Wrong Answer")
    st.write(" ")

    if st.button("2. Electroluminescence"):
        if "Electroluminescence" == correct_answer:
            st.success("✅ Correct Answer...")
        else:
            st.error("❌ Wrong Answer")

    st.write(" ")

    if st.button("3. Combustion"):
        if "Combustion" == correct_answer:
            st.success("✅ Correct Answer")
        
        else:
            st.error("❌ Wrong Answer")

    st.write(" ")

    if st.button("4. Phosphorescence"):
        if "Phosphorescence" == correct_answer:
            st.success("✅ Correct Answer")

        
        else:
            st.error("❌ Wrong Answer")

    st.write(" ")

    st.write(" ")
    st.write(" ")

    if st.button("Return to Menu"):
        st.session_state.stage = "science"

def intermediate ():
    st.header("Q.1 What Cosmic force must Spacecraft escape velocity mist overcome to come oit of earth?")
    correct_answer = "Gravity"
    st.write(" ")
    st.write(" ")

    if st.button("1. Inertia"):
        if "Ineetia" == correct_answer:
            st.success("✅ Correct Answer ")

        else:
            st.error("❌Wrong One Beeep")

    st.write(" ")

    if st.button("2. Friction"):
        if "Friction" == correct_answer:
            st.success("✅ Correct Answer")
        else:
            st.error("❌Wrong Answer")
    
    st.write(" ")

    if st.button("3. Gravity"):
        if "Gravity" == correct_answer:
            st.success("✅ Correct Answer")
        else:
            st.error("❌Beeeeep Wrong Ansswer")

    st.write(" ")

    if st.button("4. Magnetism"):
        if "Mangnetism" == correct_answer:
            st.success("✅ Correct ")

        else: 
            st.error(" ❌Beeeo Wrong One ")

    st.write(" ")
    st.write(" ")

    st.write(" ")

    if st.button(" ⏭️ Next Question "):
        st.session_state.stage = "int1"


def intermediate1():
    st.header("Q.2  What happeens to the satellite signals passing through the ionosphere ?")
    correct_answer = "Refraction"
    st.write(" ")

    st.write(" ")

    if st.button("1. Refraction "):
        if "Refraction" == correct_answer:
            st.success("✅Correct Answeerrr babe")
        else:
            st.error("❌Beeeeep Wrong One")

    st.write(" ")

    if st.button("2. Amplification "):
        if "Amplification" == correct_answer:
            st.success("✅ Correct Answer")

        else:
            st.error("❌Beeeeep Wr9ng Answer")

    st.write(" ")

    if st.button("3. Freezing"):
        if "Freezing" == correct_answer:
            st.success("✅ Correct Answer")
        else:
            st.error("❌Wrong One Babe")

    st.write(" ")

    if st.button("4. Combustions "):
        if "Combustion" == correct_answer:
            st.success("✅ Correct Answer")
        else:
            st.error("❌Beeeeeeeeep Wrong Oneee")

    st.write(" ")
    st.write(" ")

    st.write(" ")

    if st.button("⏭️ Next Question "):
        st.session_state.stage = "int2"


def intermediate2():
    st.header("Q.3 What type of Radiation dies cosmic microwave backround data reveals?")

    correct_answer = "Microwave"
    st.write(" ")
    st.write(" ")

    st.write(" ")

    if st.button("1. Ultraviolet"):
        if "Ultraviolet" == correct_answer:
            st.success("✅Correct Answer")

        else:
            st.error("❌ Beeeep Wrong One")

    st.write(" ")

    if st.button("2. Infrared "):
        if "Infrared" == correct_answer:
            st.success("✅ Correct Answer ")

        else:
            st.error("❌ Weong Answer")

    st.write(" ")

    if st.button("2. X-ray "):
        if "X-ray" == correct_answer:
            st.success("✅ Correct Answer ")
        else:
            st.error("❌ Beeeeeep Wrong one")

    st.write(" ")

    if st.button("4. Microwave"):
        if "Microwave" == correct_answer:
            st.success("✅ Correct Answer")

        else:
            st.error("❌ Wrong Answer Beeeeeeep")

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("Return to Menu"):
        st.session_state.stage= "science"


def hard():
    st.header("Q 1 What Mathematical tool used filter noisy sensor data for realtime spacecraft trajectory system ?? ")
    
    correct_answer = "Kalman"

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("1. Fourier "):
        if "Fourier" == correct_answer:
            st.success("✅ Correct Answer")
        else: 
            st.error("❌ Wrong Answer")

    st.write(" ")

    if st.button("2. Kalman"):
        if "Kalman" == correct_answer:
            st.success("✅ Correct Answer")

        else: 
            st.error("❌ Wrong Answer")

    st.write(" ")

    if st.button("3. Laplace"):
        if "Laplace" == correct_answer:
            st.success("✅ Correct Answer ")

        else: 
            st.error("❌ Wrong Answer")

    st.write(" ")

    if st.button("4. Newton"):
        if "Newton" == correct_answer:
            st.success("✅ Correct Answer ")

        else:
            st.error("❌ Wrong Asnwer")

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("⏭️ Next Question...."):
        st.session_state.stage = "hard1"
        

def hard1():
    st.header("Q.2 What chemical element acts as primary propellant in modern ion thruster propulsion ?")

    correct_answer = "Xenon"
    st.write(" ")

    st.write(" ")
    st.write(" ")

    if st.button("1. Argon "):
        if "Argon" == correct_answer:
            st.success("Correct Answer 😝😝")
        else:
            st.error("❌ Wrong Answer")

    st.write(" ")

    if st.button("2. Xenon"):
        if "Xenon" == correct_answer:
            st.success(" Correcr Answer !!!!!!")

        else:
            st.error("❌ Beeeeep Wromg One")

    st.write(" ")

    if st.button("3. Hydrogen"):
        if "Hydrogen" == correct_answer:
            st.success(" Cirrect Answwer")

        else:
            st.error("❌Wrong onee")

    st.write(" ")

    if st.button("4. Helium"):
        if "Helium" == correct_answer:
            st.success(" Correct Answer")

        else:
            st.error("❌ Wrong Answer Beeeeeeep")

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("⏭️ Next Question "):
        st.session_state.stage = "hard2"


def hard2():
    st.header("Q.3 What crystalline material foucused hard X-ray in advanced Space telescope Optics ??")
    correct_answer = "Germanium"

    st.write(" ")

    st.write(" ")
    st.write(" ")

    if st.button("1. Silicon"):
        if "Silicon" == correct_answer:
            st.success(" Correct Answer !!!")

        else:
            st.error("❌ Wrong Answer !!!")

    st.write(" ")

    if st.button("2. Quartz "):
        if "Quartz" == correct_answer:
            st.success("Correct Answer ")

        else: 
            st.error("❌ Wrong Answe")

    st.write(" ")

    if st.button("3. Diamond"):
        if "Diamond" == correct_answer:
            st.success("Correct Answer")
        else:
            st.error(" ❌Wrong One Beeeeep")

    st.write(" ")

    if st.button("4. Germanium "):
        if "Germanium" == correct_answer:
            st.success("Correct Answer")
        else:
            st.error("❌ Wrong Answer beeeep")

    st.write(" ")
    st.write(" ")

    st.write(" ")

    if st.button("Return to Menu"):
        st.session_state.stage = "main"


def history():
    st.header("Q.1 Which Macedonian king conquered the persian Land before the age of 30 ?")
    st.write(" ")
    st.write(" ")

    st.write(" ")

    correct_answer = "Alexander"

    if st.button("1. Alexander"):
        if "Alexander" == correct_answer:
            st.success("Correct Answer")

        else:
            st.error("❌Beeeeep Wrong One")

    st.write(" ")

    if st.button("2. Marcus Aurelius"):
        if "Marcus Aurelius" == correct_answer:
            st.success("Correct Answer")

        else: 
            st.error("❌ Wrong One Beep")

    st.write(" ")

    if st.button("3. Caesar"):
        if "Caesar" == correct_answer:
            st.success("Correctooooooo")
        else:
            st.error("❌ Wrong One ")

    st.write(" ")

    if st.button("4. Cyrus"):
        if "Cyrus" == correct_answer:
            st.success("Correct Answer")
        
        else:
            st.button("❌ Beep One beeep")

    st.write(" ")
    st.write(" ")

    st.write(" ")

    if st.button("⏭️Next One"):
        st.session_state.stage = "history1"

def history1():
    st.header("Q.2 Which french military leader crowned himself as emperor in 1804 ???")
    correct_answer = "Napoleon"

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("1. Louis"):
        if "Louis" == correct_answer:
            st.success("Correct Answer")
        else: 
            st.error("❌Beeeep Wrong One")

    st.write(" ")

    if st.button("2. Napoleon "):
        if "Napoleon" == correct_answer:
            st.success("Correct Answerrrr!!!!!")

        else:
            st.error("❌ Beeeeeep Wrong One")

    st.write(" ")

    if st.button("3. Charlemagne"):
        if "Charlemagne" == correct_answer:
            st.success(" Correct Answer")

        else:
            st.echo("❌ Wrong One")

    st.write(" ")

    if st.button("4. Lafayette "):
        if "Lafayette" == correct_answer:
            st.success("Correct Answer")
        else:
            st.error("❌Bleeeh Wrong One")

    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button(" ⏭️ Next Question "):
        st.session_state.stage = "history2"

def history2():
    st.header("Q.3 Which famous Stone blocked allowed historian to finally decode egyptian hieroglyphs??")
    correct_answer = "Rosetta"
    st.write(" ")
    st.write(" ")

    st.write(" ")

    if st.button("1. Rosetta"):
        if "Rosetta" == correct_answer:
            st.success("Correct Answer")

        else:
            st.error("❌Wrong One ")

    st.write(" ")

    if st.button("2. Blarney"):
        if "Blarney" == correct_answer:
            st.success("Correct Answer ")
        
        else:
            st.error("❌ Wrong One")

    st.write(" ")

    if st.button("3. Giza"):
        if "Giza" == correct_answer:
            st.success(" Correct Answer")

        else:
            st.error("❌ Bleeeeeh Wrong Answer")

    st.write(" ")

    if st.button("4. Pyson"):
        if "Pyson" == correct_answer:
            st.success("Correct Answer")
            
        else:
            st.error("❌Wrong Answer")


    st.write(" ")
    st.write(" ")
    
    st.write(" ")

    if st.button("Return To menu"):
        st.session_state.stage = "main"


if st.session_state.stage == "main":
    main()

elif st.session_state.stage == "random":
    random()

elif st.session_state.stage == "python":
    python()

elif st.session_state.stage == "python1":
    python1()

elif st.session_state.stage == "python2":
    python2()

elif st.session_state.stage == "science":
    science()

elif st.session_state.stage == "easy":
    easy()

elif st.session_state.stage == "easy1":
    easy1()

elif st.session_state.stage == "easy2":
    easy2()

elif st.session_state.stage == "int":
    intermediate()
elif st.session_state.stage == "int1":
    intermediate1()

elif st.session_state.stage == "int2":
    intermediate2()

elif st.session_state.stage == "hard":
    hard()

elif st.session_state.stage == "hard1":
    hard1()
elif st.session_state.stage == "hard2":
    hard2()

elif st.session_state.stage == "history":
    history()

elif st.session_state.stage == "history1":
    history1()
elif st.session_state.stage == "history2":
    history2()

