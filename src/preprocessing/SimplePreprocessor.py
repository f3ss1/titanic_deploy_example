from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


class SimplePreprocesser:
    def __init__(self):
        self.column_transformer = ColumnTransformer(
            [
                ('ohe_encoder', OneHotEncoder(drop='first'), ['Pclass', 'Sex', 'Embarked'])
            ],
            sparse_threshold=0,
            remainder='passthrough'
        )

    def fit(self, data):
        data = self._process_siblings(data)
        self.column_transformer.fit(data)
        return self

    def transform(self, data):
        data = self._process_siblings(data)
        return self.column_transformer.transform(data)

    @staticmethod
    def _process_siblings(data):
        data['Siblings'] = data['SibSp'] + data['Parch']
        return data.drop(['SibSp', 'Parch'], axis=1)