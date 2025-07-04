def calculate_risk_score(features):
    score = 0
    score += features['harsh_brakes'] * 2
    score += features['rapid_acceleration'] * 3
    score += features['average_speed'] / 10
    return score
