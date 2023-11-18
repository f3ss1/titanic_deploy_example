import pandas as pd
import pickle

from catboost import CatBoostClassifier

from src.preprocessing import DataCleaner, SimplePreprocesser

data = pd.read_csv('data/train.csv')

cleaner = DataCleaner()
data = cleaner.transform(data)

train_data = data.drop('Survived', axis=1)
train_labels = data[['Survived']]

processor = SimplePreprocesser()
processor.fit(train_data)
train_data = processor.transform(train_data)

model = CatBoostClassifier()
model.fit(train_data, train_labels)

with open('models/cleaner.pkl', 'wb') as f:
    pickle.dump(cleaner, f)

with open('models/processor.pkl', 'wb') as f:
    pickle.dump(processor, f)

with open('models/catboost.pkl', 'wb') as f:
    pickle.dump(model, f)
