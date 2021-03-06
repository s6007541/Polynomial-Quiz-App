import streamlit as st
from PIL import Image
import random

st.markdown("""
    # Polynomial Multiplication Quiz
    This app find remainder of the polynomial
    ***
         """)
st.sidebar.markdown("# Remainder Theorem 🤖")
st.sidebar.image(
            "https://cdn.dribbble.com/users/2933921/screenshots/6233848/dribbble_lebron_1.gif", # I prefer to load the GIFs using GIPHY
            width=300, # The actual size of most gifs on GIPHY are really small, and using the column-width parameter would make it weirdly big. So I would suggest adjusting the width manually!
        )


sign = ['+','-']




with st.form(key = 'next'):
    
    submitted2 = st.form_submit_button(label = "next")
    if(submitted2):
        st.session_state.a = str(random.randint(1,9))
        st.session_state.b = random.choice(sign) + str(random.randint(1,10))
        st.session_state.c = random.choice(sign) + str(random.randint(1,10))
        st.session_state.d = random.choice(sign) + str(random.randint(1,10))
        st.session_state.e = random.choice(sign) + str(random.randint(1,10))
        st.session_state.f = random.choice(sign) + str(random.randint(1,10))
        
        st.session_state.g = str(random.randint(1,2))
        st.session_state.h = random.choice(sign) + str(random.randint(1,6))

        st.session_state.x = -(int(st.session_state.h))/int(st.session_state.g)
        st.session_state.result = int(st.session_state.a) * (st.session_state.x ** 5) + int(st.session_state.b) * (st.session_state.x ** 4) + int(st.session_state.c) * (st.session_state.x ** 3) + int(st.session_state.d) * (st.session_state.x ** 2) + int(st.session_state.e) * (st.session_state.x) + int(st.session_state.f)
        
        
        if(st.session_state.e[-1] == '1'):
            st.session_state.p = st.session_state.a + "x^5" + st.session_state.b + "x^4" + st.session_state.c + "x^3" + st.session_state.d + "x^2" + st.session_state.e[0] + "x" + st.session_state.f
        else:
            st.session_state.p = st.session_state.a + "x^5" + st.session_state.b + "x^4" + st.session_state.c + "x^3" + st.session_state.d + "x^2" + st.session_state.e + "x" + st.session_state.f
        
        if(st.session_state.p[0] == '1'):
            st.session_state.p = st.session_state.p[1:]
            
        if(st.session_state.g == '1'):
            st.session_state.q = "x" + st.session_state.h
        else:
            st.session_state.q = st.session_state.g + "x" + st.session_state.h
        
        st.write("""
         ### Question
         """)
        st.latex("\dfrac{" + st.session_state.p + "}{" + st.session_state.q + "}")


        st.write("""
                ##### Remainder
                """)



    else:
        if('p' in st.session_state and 'q' in st.session_state):
            st.write("""
                ### Question
                """)
            st.latex("\dfrac{" + st.session_state.p + "}{" + st.session_state.q + "}")

            st.write("""
                ##### Remainder
                """)





with st.form(key = 'form1'):
    
    remainder = st.text_input(label="", placeholder='remainder', max_chars=None, key='remainder')
   
    submitted = st.form_submit_button(label = "Submit")
    if(submitted):
        print(remainder[0] == '-')
        if(remainder[0] == '-'):
            remainder = -int(float(remainder[1:])*100000)
        else:
            remainder = int(float(remainder)*100000)
        print(remainder)
        print(int(st.session_state.result * 100000))
        
        if(remainder != int(st.session_state.result * 100000)):
            
            st.write("""
                ##### Your Answer is incorrect!
                """)
            
        else:
            st.write("""
                ##### Your Answer is correct!
                """)
         
if("result" in st.session_state):
    if st.button('Solution',key = 'sol'):
        st.latex (st.session_state.result)









    
    
