import matplotlib.pyplot as plt
import seaborn as sns

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
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=historical_data, x='quiz_date', y='score')
    plt.title('Score Trend Over Last 5 Quizzes')
    plt.xlabel('Quiz Date')
    plt.ylabel('Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('quiz_analysis_project/src/static/images/score_trend.png')
    plt.show()