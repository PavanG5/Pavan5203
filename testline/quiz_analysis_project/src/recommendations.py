def generate_recommendations(weak_areas):
    recommendations = []
    for topic in weak_areas.index:
        recommendations.append(f"Revise {topic} to improve accuracy.")
    return recommendations
