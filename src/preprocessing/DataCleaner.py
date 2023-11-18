class DataCleaner:
    def __init__(self):
        self.columns_to_drop = ['Ticket', 'Cabin', 'Name', 'PassengerId']

    def transform(
            self,
            data,
            save_target: bool = True
    ):
        data = data.drop(self.columns_to_drop, axis=1, errors='ignore')
        if not save_target:
            data = data.drop('Survived', axis=1, errors='ignore')
        data = data.dropna()
        return data

    def fit(self):
        return self
