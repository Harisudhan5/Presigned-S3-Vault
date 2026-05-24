import streamlit as st
import requests

from src.core.presign import generate_delete_url


def render(config):

    st.header("Delete Object")

    bucket = st.text_input("Bucket Name")
    key = st.text_input("Object Key")

    if st.button("Delete"):

        url = generate_delete_url(config, "delete_object", bucket, key)

        resp = requests.delete(url)

        if resp.status_code in [200, 204]:
            st.success("Object deleted successfully")
        else:
            st.error(f"Failed to delete object | Status code: {resp.status_code}")