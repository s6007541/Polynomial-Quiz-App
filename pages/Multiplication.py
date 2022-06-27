import streamlit as st
from PIL import Image
import random

st.markdown("""
    # Polynomial Multiplication Quiz
    This app multiplies two Polynomial with degree less than 3
    ***
         """)
st.sidebar.markdown("# Main page 🎈")



sign = ['+','-']




with st.form(key = 'next'):
    
    submitted2 = st.form_submit_button(label = "next")
    if(submitted2):
        st.session_state.a1 = str(random.randint(1,10))
        st.session_state.b1 = random.choice(sign) + str(random.randint(1,10))
        st.session_state.c1 = random.choice(sign) + str(random.randint(1,10))
        st.session_state.a2 = str(random.randint(1,10))
        st.session_state.b2 = random.choice(sign) + str(random.randint(1,10))
        st.session_state.c2 = random.choice(sign) + str(random.randint(1,10))
        
        
        
        st.session_state.p1 = st.session_state.a1 + "x^2" + st.session_state.b1 + "x" + st.session_state.c1
        st.session_state.p2 = st.session_state.a2 + "x^2" + st.session_state.b2 + "x" + st.session_state.c2
        st.write("""
         ### Question
         """)
        st.latex("(" + st.session_state.p1 + ")(" + st.session_state.p2 + ")")


        st.write("""
                ##### Your Answer in the form below
                """)
        st.latex ("Ax^4 + Bx^3 + Cx^2 + Dx + E")

        st.session_state.Ar = str(int(st.session_state.a1)*int(st.session_state.a2))
        st.session_state.Br = str(int(st.session_state.a1)*int(st.session_state.b2) + int(st.session_state.a2)*int(st.session_state.b1))
        st.session_state.Cr = str(int(st.session_state.a1)*int(st.session_state.c2) + int(st.session_state.a2)*int(st.session_state.c1) + int(st.session_state.b1)*int(st.session_state.b2))
        st.session_state.Dr = str(int(st.session_state.b1)*int(st.session_state.c2) + int(st.session_state.b2)*int(st.session_state.c1))
        st.session_state.Er = str(int(st.session_state.c1)*int(st.session_state.c2))
        
        print("__________")
        print(st.session_state.Ar)
        print(st.session_state.Br)
        print(st.session_state.Cr)
        print(st.session_state.Dr)
        print(st.session_state.Er)
        print("__________")
    else:
        if('p1' in st.session_state and 'p2' in st.session_state):
            st.write("""
                ### Question
                """)
            st.latex("(" + st.session_state.p1 + ")(" + st.session_state.p2 + ")")

            st.write("""
                ##### Your Answer in the form below
                """)
            st.latex ("Ax^4 + Bx^3 + Cx^2 + Dx + E")





with st.form(key = 'form1'):
    
    A = st.text_input(label="", placeholder='A', max_chars=None, key='A')
    B = st.text_input(label="", placeholder='B', max_chars=None, key='B')
    C = st.text_input(label="", placeholder='C', max_chars=None, key='C')
    D = st.text_input(label="", placeholder='D', max_chars=None, key='D')
    E = st.text_input(label="", placeholder='E', max_chars=None, key='E')
    
    submitted = st.form_submit_button(label = "Submit")
    if(submitted):
        
        
        if(A != st.session_state.Ar or B != st.session_state.Br or C != st.session_state.Cr or D != st.session_state.Dr or E != st.session_state.Er):
            
            st.write("""
                ##### Your Answer is incorrect!
                """)
            
            
        else:
            st.write("""
                ##### Your Answer is correct!
                """)
            







    
    
