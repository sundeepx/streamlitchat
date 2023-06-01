import streamlit as st
from streamlit_chat import message

st.title('🎈 App Name')

st.write('Hello world!')

message("My message") 
message("Hello bot!", is_user=True)