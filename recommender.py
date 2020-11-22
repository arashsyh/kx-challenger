import numpy as np


class Recommendation:

    def top_10(self, similarities):
        # Returns indices of top-10 similar employees in negative_attrition df
        top_10_similars = []
        for i in range(10):
            max_index = np.argmax(similarities)
            top_10_similars.append(max_index)
            "Remove the max element"
            del top_10_similars[max_index]
        return top_10_similars

    def cosine_similarity(self, employee):
        # Calculate Cosine similarity of employees to the requested employee
        similarities = []
        for index, row in negative_attrition.iterrows():
            cos_similarity = np.dot(employee, row) / (np.linalg.norm(employee) * np.linalg.norm(row))
            similarities.append(cos_similarity)
        top_10_similar_indices = top_10(similarities)
        return top_10_similar_indices

    def calculate_recommendation_values(self, employee, counterparts):
        recommendation_columns = ['JobInvolvement', 'MonthlyIncome', 'PercentSalaryHike', 'StockOptionLevel'
            , 'TrainingTimesLastYear', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']
        recommended_values = counterparts[recommendation_columns].mean()
        accepted_recommendation = dict()
        accepted_recommendation['JobInvolvement'] = round(recommendation_values['JobInvolvement'])
        accepted_recommendation['TrainingTimesLastYear'] = round(recommendation_values['TrainingTimesLastYear'])
        accepted_recommendation['YearsInCurrentRole'] = round(recommendation_values['YearsInCurrentRole'])
        accepted_recommendation['YearsWithCurrManager'] = round(recommendation_values['YearsWithCurrManager'])

        if employee['MonthlyIncome'] < recommended_values['MonthlyIncome']:
            accepted_recommendation['MonthlyIncome'] = recommended_values['MonthlyIncome']
        else:
            accepted_recommendation['MonthlyIncome'] = None

        if employee['PercentSalaryHike'] < recommended_values['PercentSalaryHike']:
            accepted_recommendation['PercentSalaryHike'] = recommended_values['PercentSalaryHike']
        else:
            accepted_recommendation['PercentSalaryHike'] = None

        if employee['StockOptionLevel'] < round(recommended_values['StockOptionLevel']):
            accepted_recommendation['StockOptionLevel'] = round(recommended_values['StockOptionLevel'])
        else:
            accepted_recommendation['StockOptionLevel'] = None

        if employee['YearsSinceLastPromotion'] > round(recommended_values['YearsSinceLastPromotion']):
            accepted_recommendation['YearsSinceLastPromotion'] = round(recommended_values['YearsSinceLastPromotion'])
        else:
            accepted_recommendation['YearsSinceLastPromotion'] = None
