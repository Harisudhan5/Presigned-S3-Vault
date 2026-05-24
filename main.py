import streamlit as st

from src.ui.config_panel import get_config
from src.ui.view import render as view
from src.ui.upload import render as upload
from src.ui.delete import render as delete


st.title("Presigned S3 Vault")

config = get_config()

operation = st.radio(
    "Operations Allowed",
    ["Download", "Upload", "Delete"],
    horizontal=True
)

if operation == "Download":
    view(config)

elif operation == "Upload":
    upload(config)

elif operation == "Delete":
    delete(config)