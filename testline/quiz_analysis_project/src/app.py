from flask import Flask, render_template, jsonify
from data_analysis import load_data, analyze_performance, analyze_trends
from visualizations import plot_accuracy_by_topic, plot_score_trend
from recommendations import generate_recommendations
import pandas as pd
app = Flask(__name__)

def analyze_student_persona(quiz_data):
    # Clean and ensure accuracy is numeric
    quiz_data['accuracy'] = pd.to_numeric(quiz_data['accuracy'], errors='coerce')

    # Drop rows with NaN values in the 'accuracy' column
    quiz_data = quiz_data.dropna(subset=['accuracy'])
    accuracy_by_topic = quiz_data.groupby('quiz.topic')['accuracy'].mean()

    # Define strengths and weaknesses based on accuracy
    strong_areas = accuracy_by_topic[accuracy_by_topic >= 0.8]  # Strong areas (accuracy > 80%)
    weak_areas = accuracy_by_topic[accuracy_by_topic < 0.5]  # Weak areas (accuracy < 50%)

    # Persona based on strength in certain areas and struggles in others
    if len(strong_areas) > len(weak_areas):
        persona = "Strategic Learner"
        insights = [
            f"Your strength lies in subjects like {', '.join(strong_areas.index)}.",
            "Focus on your strong areas to maintain consistency."
        ]
    elif len(strong_areas) == len(weak_areas):
        persona = "Balanced Learner"
        insights = [
            "You have a good balance between strengths and areas to improve.",
            f"Consider focusing on improving in topics like {', '.join(weak_areas.index)}."
        ]
    else:
        persona = "Focused Learner"
        insights = [
            f"You excel in topics like {', '.join(strong_areas.index)}.",
            f"Consider spending more time in topics like {', '.join(weak_areas.index)} to improve overall performance."
        ]
    
    # Return persona and insights
    return persona, strong_areas, weak_areas, insights
def generate_student_persona(weak_areas):
    # Define strengths and weaknesses based on weak areas
    strengths = [topic for topic in weak_areas.index if weak_areas[topic] > 0.7]
    weaknesses = [topic for topic in weak_areas.index if weak_areas[topic] < 0.5]
    
    # Define the student persona
    student_persona = {
        "strengths": strengths,
        "weaknesses": weaknesses
    }
    
    # Generate personalized insights
    insights = []
    if strengths:
        insights.append(f"Focus on strengthening your strengths in {', '.join(strengths)}.")
    if weaknesses:
        insights.append(f"Spend more time improving on topics like {', '.join(weaknesses)}.")
    
    return student_persona, insights


@app.route('/')
def index():
    quiz_data, historical_data = load_data(
        'https://api.jsonserve.com/rJvd7g', 
        'https://api.jsonserve.com/XgAgFJ'
    )
    weak_areas = analyze_performance(quiz_data)
    trends = analyze_trends(historical_data)
    
    # Additional data analysis to define the student persona
    student_persona, personalized_insights = generate_student_persona(weak_areas)
    
    # Generate recommendations based on weak areas
    recommendations = generate_recommendations(weak_areas)
    
    quiz_data['accuracy'] = quiz_data['correct_answers'] / (quiz_data['correct_answers'] + quiz_data['incorrect_answers'])
    plot_accuracy_by_topic(quiz_data.groupby('quiz.topic')['accuracy'].mean())
    plot_score_trend(trends)
    
    return render_template(
        'index.html',
        recommendations=recommendations,
        insights=personalized_insights,
        student_persona=student_persona
    )




if __name__ == '__main__':
    app.run(debug=True)
