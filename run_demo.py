import json
from behavior_analysis.behavior import extract_features
from risk_scoring.risk import calculate_risk_score
from pricing_adjustment.pricing import adjust_premium
from feedback.feedback import generate_recommendations

# Sample data simulating telematics input
sample_data = [
    {"speed": 50, "acceleration": 2, "brake": 1},
    {"speed": 60, "acceleration": 4, "brake": 4},
    {"speed": 55, "acceleration": 5, "brake": 0},
    {"speed": 40, "acceleration": 1, "brake": 6},
]

features = extract_features(sample_data)
risk_score = calculate_risk_score(features)
premium = adjust_premium(100, risk_score)
recommendations = generate_recommendations(features)

print("Features:", features)
print("Risk Score:", risk_score)
print("Adjusted Premium:", premium)
print("Recommendations:", recommendations)
