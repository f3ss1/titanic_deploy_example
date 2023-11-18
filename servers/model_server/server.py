from typing import Union
import pickle

from pydantic import BaseModel, Field
from fastapi import FastAPI

import pandas as pd


class OriginalPreprocessRequest(BaseModel):
    passenger_id: int = Field(..., alias='PassengerId')
    p_class: int = Field(..., alias='Pclass')
    name: str = Field(..., alias='Name')
    sex: str = Field(..., alias='Sex')
    age: int = Field(..., alias='Age')
    sib_sp: int = Field(..., alias='SibSp')
    par_ch: int = Field(..., alias='Parch')
    ticket: str = Field(..., alias='Ticket')
    fare: float = Field(..., alias='Fare')
    cabin: str = Field(..., alias='Cabin')
    embarked: str = Field(..., alias='Embarked')


class CleanPreprocessRequest(BaseModel):
    sex: str = Field(..., alias='Sex')
    p_class: int = Field(..., alias='Pclass')
    age: int = Field(..., alias='Age')
    sib_sp: int = Field(..., alias='SibSp')
    par_ch: int = Field(..., alias='Parch')
    fare: float = Field(..., alias='Fare')
    embarked: str = Field(..., alias='Embarked')


class ModelOutput(BaseModel):
    death_proba: float
    survive_proba: float
    binary_prediction: int


with open('models/cleaner.pkl', 'rb') as f:
    cleaner = pickle.load(f)

with open('models/processor.pkl', 'rb') as f:
    processor = pickle.load(f)

with open('models/catboost.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()


@app.get('/')
async def root():
    return None


@app.post('/predict')
async def predict(
        data_entry: Union[OriginalPreprocessRequest, CleanPreprocessRequest]
) -> ModelOutput:
    dataline = pd.DataFrame(
        data_entry.model_dump(by_alias=True),
        index=[0, ]
    )

    if isinstance(data_entry, OriginalPreprocessRequest):
        dataline = cleaner.transform(dataline, save_target=False)

    model_data = processor.transform(dataline)
    model_prediction = model.predict_proba(model_data)
    output = ModelOutput(
        death_proba=model_prediction[0, 0],
        survive_proba=model_prediction[0, 1],
        binary_prediction=(model_prediction[0, 1] > model_prediction[0, 0])
    )

    return output
