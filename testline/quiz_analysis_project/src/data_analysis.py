import pandas as pd
import numpy as np
import requests
def load_data(quiz_url, historical_url):
    quiz_response = requests.get(quiz_url)
    historical_response = requests.get(historical_url)

    # Check if the requests were successful
    if quiz_response.status_code == 200 and historical_response.status_code == 200:
        # Parse the JSON data into DataFrames
        quiz_data = pd.json_normalize(quiz_response.json())
        historical_data = pd.json_normalize(historical_response.json())
    return quiz_data, historical_data

def analyze_performance(quiz_data):
    if 'quiz.topic' in quiz_data.columns and 'correct_answers' in quiz_data.columns and 'incorrect_answers' in quiz_data.columns:
        # Calculate accuracy as the ratio of correct answers to total questions
        quiz_data['accuracy'] = quiz_data['correct_answers'] / (quiz_data['correct_answers'] + quiz_data['incorrect_answers'])

        # Group by topic and calculate the mean accuracy
        accuracy_by_topic = quiz_data.groupby('quiz.topic')['accuracy'].mean()

        print("\nAccuracy by Topic:")
        print(accuracy_by_topic)

        # Optional: Save the accuracy results to a CSV file
        accuracy_by_topic.to_csv('accuracy_by_topic.csv', index=True)
    else:
        print("\nRequired columns ('quiz.topic', 'correct_answers', 'incorrect_answers') are missing from quiz_data")
    weak_areas = accuracy_by_topic[accuracy_by_topic < 0.5]
    return weak_areas

def analyze_trends(historical_data):
    if 'submitted_at' in historical_data.columns:
        # Convert 'submitted_at' to datetime
        historical_data['quiz_date'] = pd.to_datetime(historical_data['submitted_at'])

        # Normalize the score by total questions
        historical_data['normalized_score'] = historical_data['score'] / historical_data['total_questions']

        # Sort by quiz_date and take the last 5 quizzes
        last_5_quizzes = historical_data.sort_values('quiz_date', ascending=False).head(5)

        # Display performance for the last 5 quizzes
        print("\nPerformance Over the Last 5 Quizzes:")
        print(last_5_quizzes[['quiz_date', 'normalized_score']])

    else:
        print("The column 'submitted_at' is not present in the dataset.")

    return historical_data[['quiz_date', 'score']]
