import pandas as pd

def extract_features(driving_data):
    """
    driving_data: list of dicts, each with speed, acceleration, braking events
    Returns: dict of extracted features like harsh_brakes_count
    """
    df = pd.DataFrame(driving_data)
    features = {
        "average_speed": df['speed'].mean(),
        "harsh_brakes": sum(df['brake'] > 3),  # Example threshold
        "rapid_acceleration": sum(df['acceleration'] > 3),
    }
    return features
