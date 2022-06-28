import streamlit as st
from PIL import Image
import random

st.markdown("""
    # Polynomial Factorization Quiz
    This app factorizes two Polynomial with degree 2
    ***
         """)
st.sidebar.markdown("# Factorization 🎈")
st.sidebar.image(
            "https://cdn.dribbble.com/users/2933921/screenshots/7088453/media/d30b00694c69bde54f1d1b7d2471463b.gif", # I prefer to load the GIFs using GIPHY
            width=300, # The actual size of most gifs on GIPHY are really small, and using the column-width parameter would make it weirdly big. So I would suggest adjusting the width manually!
        )

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

        if (int(A) == st.session_state.a1 and int(B) == st.session_state.b1 and int(C) == st.session_state.a2 and int(D) == st.session_state.b2)   or   (int(A) == st.session_state.a2 and int(B) == st.session_state.b2 and int(C) == st.session_state.a1 and int(D) == st.session_state.b1):
            
            
            st.write("""
                ##### Your Answer is correct!
                """)
            
            
        else:
            st.write("""
                ##### Your Answer is incorrect!
                """)
if('a1' in st.session_state):
    if st.button('Solution',key = 'sol'):
        st.latex ("(" + str(st.session_state.a1) + "x + " + str(st.session_state.b1) + ")(" + str(st.session_state.a2) + "x + " + str(st.session_state.b2) + ")")

            







    
    
