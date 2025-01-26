import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def plot_accuracy_by_topic(accuracy_by_topic):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=accuracy_by_topic.index, y=accuracy_by_topic.values)
    plt.title('Topic-wise Accuracy')
    plt.xlabel('Topic')
    plt.ylabel('Accuracy')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('quiz_analysis_project/src/static/images/accuracy_by_topic.png')
    plt.show()

def plot_score_trend(historical_data):
    # Ensure 'quiz_date' is in datetime format (if it's not already)
    if 'submitted_at' in historical_data.columns:
        # Convert 'submitted_at' to datetime
        historical_data['quiz_date'] = pd.to_datetime(historical_data['submitted_at'])

        # Normalize the score by total questions
        historical_data['normalized_score'] = historical_data['score'] / historical_data['total_questions']
        historical_data['quiz_date'] = pd.to_datetime(historical_data['quiz_date'], errors='coerce')
    
        # Drop rows with NaT (invalid dates)
        historical_data = historical_data.dropna(subset=['quiz_date'])
    
        # Plot the score trend over time
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=historical_data, x='quiz_date', y='score')
        plt.title('Score Trend Over Last 5 Quizzes')
        plt.xlabel('Quiz Date')
        plt.ylabel('Score')
        plt.xticks(rotation=45)
        plt.show()