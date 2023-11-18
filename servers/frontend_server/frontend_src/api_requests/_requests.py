import requests
import streamlit as st


def prediction_request(
        user_data: dict,
        server_url: str = 'http://127.0.0.1:8000/predict'
):

    response = requests.post(server_url + '/predict', json=user_data)

    if response.status_code == 200:
        st.session_state['successful_api_answer'] = True

    else:
        st.session_state['successful_api_answer'] = False

    return response.json()
