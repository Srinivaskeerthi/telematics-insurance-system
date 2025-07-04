def generate_recommendations(features):
    recommendations = []
    if features['harsh_brakes'] > 5:
        recommendations.append("Reduce harsh braking to improve safety and premiums.")
    if features['rapid_acceleration'] > 5:
        recommendations.append("Avoid rapid acceleration to lower risk score.")
    return recommendations
