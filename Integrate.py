import UserProfile_streamlit 
from Chat_UI import display_chat 
import streamlit as st

def app1():
    UserProfile_streamlit.User_info() 
    if st.button('Start Interview',key='StartInterviewButton'):
        st.session_state.app = app2
        st.experimental_rerun()

def app2():
    display_chat()

if 'app' not in st.session_state:
    st.session_state.app = app1

st.session_state.app()
