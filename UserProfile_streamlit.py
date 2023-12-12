import streamlit as st

def User_info():
    st.title('Omdena Chat Bot for Interview')
    st.subheader('User Profile')
    name = st.text_input('Name')
    position = st.text_input('Position')


    experience_options = ['Select', 'Entry Level', 'Intermediate', 'Experienced']
    experience = st.selectbox('Experience', experience_options, index=0)


    col1, col2 = st.columns([1, 4])

    country_code_options = ['Select', '+1', '+44', '+52', '+91', '+86']  
    country_code = col1.selectbox('Country Code', country_code_options, index=0)
    mobile_number = col2.text_input('Mobile Number')

    email_id = st.text_input('Email ID')
    job_link = st.text_input('Job Link')

    

    if st.button('Start Interview'):
        button_pressed = "Yes"
        if name == '' or position == '' or experience == 'Select' or country_code == 'Select' or mobile_number == '' or email_id == '' or job_link == '':
            st.warning('Please fill out all fields.')
        else:
    
            st.write('Starting the interview...')
            return True
    return False