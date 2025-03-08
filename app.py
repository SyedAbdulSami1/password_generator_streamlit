import streamlit as st
import random
import string

def pasword_generator(length, use_digit, use_special):
    charectors = string.ascii_letters
    if use_digit:
        charectors += string.digits
    if use_special:
        charectors += string.punctuation
    return ''.join(random.choice(charectors) for _ in range(length))
st.title("Password Generator")
length = st.slider("Select Password length", max_value=20, min_value=6, value=10)
use_digit = st.checkbox("Use digits")
use_special = st.checkbox("Use special charectors")

if st.button("Generate Password"):
    password = pasword_generator (length, use_digit, use_special)
    st.write(f"Generated password = {password}")

st.write("Created by: Syed Abdul Sami")