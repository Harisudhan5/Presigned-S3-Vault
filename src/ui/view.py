import streamlit as st
import requests
from src.core.presign import generate_download_url

def render(config):

    st.header("Download Object")

    bucket = st.text_input("Bucket Name")
    key = st.text_input("Object Key")

    if st.button("Get Object"):

        url = generate_download_url(config, "get_object", bucket, key)

        st.session_state["url"] = url

        resp = requests.get(url)

        if resp.status_code == 200:

            st.success("Object ready for download")

            if key.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                st.image(resp.content)

            elif key.lower().endswith((".txt", ".json", ".csv", ".md", ".py")):
                st.code(resp.content.decode("utf-8"))

            else:
                st.warning("Preview not supported")

            st.download_button(
                "Download",
                resp.content,
                file_name=key.split("/")[-1]
            )

        else:
            st.error(f"Failed: {resp.status_code}")