import streamlit as st

def get_config():
    st.sidebar.title("AWS Configuration")

    config = {
        "aws_access_key": st.sidebar.text_input("AWS Access Key ID"),
        "aws_secret_key": st.sidebar.text_input("AWS Secret Key", type="password"),
        "region": st.sidebar.text_input("Region"),
        "expiry": st.sidebar.number_input(
            "URL Expiry (Seconds)",
            min_value=60,
            value=300
        )
    }

    return config