import streamlit as st

from frontend_src.api_requests import prediction_request


def _get_sidebar_features():
    json = {
        'Sex': st.sidebar.selectbox('Sex', ('male', 'female'), key='sex_widget'),
        'Pclass': st.sidebar.selectbox('Class', (1, 2, 3)),
        'Age': st.sidebar.number_input('Age', step=1),
        'SibSp': st.sidebar.number_input('Number of siblings and spouses on board', step=1),
        'Parch': st.sidebar.number_input('Number of parents and children on board', step=1),
        'Fare': st.sidebar.number_input('Price of the ticket you bought'),
        'Embarked': st.sidebar.selectbox(
            'Embarked',
            ('Cherbourg', 'Queenstown', 'Southampton')
        )[0]
    }
    return json


def sidebar():
    st.sidebar.header('Parameters')
    user_data = _get_sidebar_features()

    if st.sidebar.button('Spin the wheel'):
        api_response = prediction_request(
            user_data,
            server_url=st.session_state['MODEL_SERVER_URL']
        )
        st.session_state['api_response'] = api_response

    return user_data