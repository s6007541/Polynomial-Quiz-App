import streamlit as st
from PIL import Image
import random

st.markdown("""
    # Polynomial Factorization Quiz
    This app factorizes two Polynomial with degree 2
    ***
         """)
st.sidebar.markdown("# Main page 🎈")


sign = ['+','-']




with st.form(key = 'next'):
    
    submitted2 = st.form_submit_button(label = "next")
    if(submitted2):
        st.session_state.a1 = random.randint(1,5)
        st.session_state.b1 = int(random.choice(sign) + str(random.randint(1,10)))
        st.session_state.a2 = random.randint(1,5)
        st.session_state.b2 = int(random.choice(sign) + str(random.randint(1,10)))
        
        print((st.session_state.a1, st.session_state.b1 ,st.session_state.a2, st.session_state.b2))
        
        st.session_state.A = int(st.session_state.a1)* int(st.session_state.a2)
        st.session_state.B = int(st.session_state.a1)* int(st.session_state.b2) + int(st.session_state.b1)* int(st.session_state.a2)
        st.session_state.C = int(st.session_state.b1)* int(st.session_state.b2)

        st.session_state.A = str(st.session_state.A)
        if(st.session_state.B > 0):
            st.session_state.B = "+" + str(st.session_state.B)
        else:
            st.session_state.B = str(st.session_state.B)
        
        if(st.session_state.C > 0):
            st.session_state.C = "+" + str(st.session_state.C)
        else:
            st.session_state.C = str(st.session_state.C)
            
            
        st.session_state.p = st.session_state.A + "x^2" + st.session_state.B + "x" + st.session_state.C
        st.write("""
         ### Question
         """)
        st.latex(st.session_state.p)


        st.write("""
                ##### Your Answer in the form below
                """)
        st.latex ("(Ax + B)(Cx + D)")
        
    else:
        if('p' in st.session_state):
            st.write("""
                ### Question
                """)
            st.latex(st.session_state.p)
            
            st.write("""
                ##### Your Answer in the form below
                """)
            st.latex ("(Ax + B)(Cx + D)")





with st.form(key = 'form1'):
    
    A = st.text_input(label="", placeholder='A', max_chars=None, key='1')
    B = st.text_input(label="", placeholder='B', max_chars=None, key='2')
    C = st.text_input(label="", placeholder='C', max_chars=None, key='3')
    D = st.text_input(label="", placeholder='D', max_chars=None, key='4')
    
    submitted = st.form_submit_button(label = "Submit")
    if(submitted):
        
        print((st.session_state.a1, st.session_state.b1 ,st.session_state.a2, st.session_state.b2))
        print((A,B,C,D))

        if(int(A) != st.session_state.a1 or int(B) != st.session_state.b1 or int(C) != st.session_state.a2 or int(D) != st.session_state.b2):
            
            st.write("""
                ##### Your Answer is incorrect!
                """)
            
            
        else:
            st.write("""
                ##### Your Answer is correct!
                """)
            







    
    
