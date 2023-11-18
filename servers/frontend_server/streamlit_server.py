import streamlit as st
import os

from frontend_src.main_page import main_page, sidebar


if __name__ == '__main__':
    st.set_page_config(
        layout='wide',
        initial_sidebar_state='auto',
        page_title='Titanic deploy',

    )

    st.session_state['MODEL_SERVER_URL'] = os.getenv(
        'MODEL_SERVER_URL',
        'http://127.0.0.1:8000'
    )
    st.session_state['successful_api_answer'] = False

    user_data = sidebar()
    main_page(user_data)
