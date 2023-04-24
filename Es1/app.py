import streamlit as st
import pandas as pd

def main():
    st.title("Exercise Number One")





if __name__ == "__main__":
    main()

number = st.number_input('Insert Age')
st.write('The current Age is', number, 'years old')

select = st.radio(
    "And you are:",
    ('With Car license', 'Without Car license'))

boy = number
patente = False

if number >= 18 and select == 'With Car license':
    st.write("Daje vezz ce l'hai gia la patente")
elif number >= 18 and select == 'Without Car license':
    st.write("Daje oooh, sta patentina quando al prendiamo?")
else:
    st.write("Sus Bro, troppo cinno")