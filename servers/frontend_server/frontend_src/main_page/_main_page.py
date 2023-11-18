import pandas as pd
import streamlit as st


def get_prediction_text(model_prediction: dict):
    if model_prediction['binary_prediction']:
        survival_chance = model_prediction['survive_proba'] * 100
        message = (f'The person entered is lucky enough to survive with the '
                   f'{survival_chance:.2f}% chance.')
    else:
        death_chance = model_prediction['death_proba'] * 100
        message = (f'Unfortunately, the person entered would probably die with '
                   f'the {death_chance:.2f}% chance.')

    return message


def main_page(user_data):
    st.write('# Determine if the person would have died on the Titanic')

    if st.session_state['successful_api_answer']:

        st.write('You\'ve entered:')

        dataframe = pd.DataFrame(user_data, index=[0, ])
        st.write(dataframe)

        model_prediction = st.session_state['api_response']
        message = get_prediction_text(model_prediction)

        st.write(message)
