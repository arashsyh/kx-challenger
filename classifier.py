import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


class Model:

    def __init__(self, train_data, test_size=0.10, trees_number=50):
    #     self.train_data = pd.read_csv('./data/train_data.csv')
        self.train_data = train_data
        self.test_size = test_size
        self.dataset_x = None
        self.dataset_y = None
        self.train_x = None
        self.train_y = None
        self.test_x = None
        self.test_y = None
        self.model = RandomForestClassifier(n_estimators=trees_number)

    def pre_process(self):
        # train_data = self.train_data.drop(['Unnamed: 0', 'Name'], axis=1)
        train_data = self.train_data.drop(['EmployeeID', 'Name'], axis=1)
        self.dataset_y = train_data['Attrition']
        self.dataset_x = train_data.drop(['Attrition'], axis=1)
        self.__cat_to_num()
        self.train_x, self.test_x, self.train_y, self.test_y = \
            train_test_split(self.dataset_x, self.dataset_y, test_size=self.test_size, random_state=42)
        return

    def __cat_to_num(self):
        # Convert categorical values to numerical, using title encoding method.
        categorical_columns = self.dataset_x.loc[:, self.dataset_x.dtypes == 'object']
        for column_name in categorical_columns.columns.values:
            categorical_columns[column_name] = categorical_columns[column_name].astype('category')
            categorical_columns[column_name] = categorical_columns[column_name].cat.codes
        self.dataset_x = self.dataset_x.drop(list(categorical_columns.columns.values), axis=1)
        self.dataset_x = pd.concat([self.dataset_x, categorical_columns], axis=1)
        self.dataset_y = self.dataset_y.astype('category')
        self.dataset_y = self.dataset_y.cat.codes

    def fit(self):
        self.model.fit(self.train_x, self.train_y)
        return self.model.score(self.test_x, self.test_y)

    def predict(self, test_x):
        predict_y = self.model.predict(test_x)
        return predict_y
