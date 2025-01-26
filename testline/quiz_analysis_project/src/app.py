from flask import Flask, render_template, jsonify
from data_analysis import load_data, analyze_performance, analyze_trends
from visualizations import plot_accuracy_by_topic, plot_score_trend
from recommendations import generate_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    quiz_data, historical_data = load_data(
        'https://api.jsonserve.com/rJvd7g', 
        'https://api.jsonserve.com/XgAgFJ'
    )
    weak_areas = analyze_performance(quiz_data)
    trends = analyze_trends(historical_data)
    quiz_data['accuracy'] = quiz_data['correct_answers'] / (quiz_data['correct_answers'] + quiz_data['incorrect_answers'])
    plot_accuracy_by_topic(quiz_data.groupby('quiz.topic')['accuracy'].mean())
    plot_score_trend(trends)

    recommendations = generate_recommendations(weak_areas)

    return render_template('index.html', recommendations=recommendations)


if __name__ == '__main__':
    app.run(debug=True)
