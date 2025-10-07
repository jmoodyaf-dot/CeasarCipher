import string
import streamlit as st

alphabet = list(string.ascii_lowercase)
capital = list(string.ascii_uppercase)

def encode(word: str, shift: int):
    msg = ''
    for letter in word:
        if letter in alphabet:
            msg += alphabet[(alphabet.index(letter) + shift) % 26]
        elif letter in capital:
            msg += capital[(capital.index(letter) + shift) % 26]
        else:
            msg += letter
    return msg

def decode(word: str, shift: int):
    msg = ''
    for letter in word:
        if letter in alphabet:
            msg += alphabet[(alphabet.index(letter) - shift) % 26]
        elif letter in capital:
            msg += capital[(capital.index(letter) - shift) % 26]
        else:
            msg += letter
    return msg

st.title("🔐 Caesar Cipher Encoder/Decoder")

action = st.radio("Choose an action:", ["Encode", "Decode"])
word = st.text_input("Enter your message:")
shift = st.number_input("Enter shift number:", min_value=0, max_value=25, value=3)

if st.button("Run Cipher"):
    if action == "Encode":
        result = encode(word, shift)
    else:
        result = decode(word, shift)

    st.markdown(f"""
    ```
    +{'-' * (len(result) + 2)}+
    | {result} |
    +{'-' * (len(result) + 2)}+
    ```
    """)

st.caption("Built with ❤️ in Replit using Streamlit")
