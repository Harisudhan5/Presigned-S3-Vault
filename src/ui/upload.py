import streamlit as st
import requests

from src.core.presign import generate_upload_url


def render(config):

    st.header("Upload Object")

    bucket = st.text_input("Bucket Name")
    key = st.text_input("Object Key")
    file = st.file_uploader("File")

    if st.button("Upload"):
        if not bucket or bucket.strip() == "":
            st.error("Bucket name is required")
            st.stop()

        if not key or key.strip() == "":
            st.error("Object key is required")
            st.stop()

        if not file:
            st.warning("File not selected")
            st.stop()

        url = generate_upload_url(config, bucket, key)

        resp = requests.put(url, data=file.getvalue())

        if resp.status_code == 200:
            st.success("Object uploaded successfully")
        else:
            st.error(f"Failed to upload object | Status code: {resp.status_code}")