from sentence_transformers import SentenceTransformer
from datetime import datetime
import logging
def generate_summary(row):

    date = row.get('start_date', 'an unknown date')
    date_pretty =datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y at %H:%M")
    name = row.get('name', 'Unnamed activity')
    sport_type = row.get('type', 'activity').lower()
    distance = row.get('distance', 0)
    pace = row.get('pace', None)
    avg_speed = row.get('average_speed', None)
    elevation = row.get('total_elevation_gain', 0)

    summary = (
        f"On {date_pretty}, you completed a {distance:.2f} kilometer {sport_type} titled '{name}'. "
        f"You maintained an average pace of {pace} minutes per kilometer "
        f"and an average speed of {avg_speed} kilometers per hour. "
        f"The route included a total elevation gain of {elevation} meters. "
    )

    if 'average_heartrate' in row and row['average_heartrate']:
        summary += (
            f"Your average heart rate was {row['average_heartrate']} bpm, "
            f"with a maximum of {row.get('max_heartrate', 'unknown')} bpm. "
        )

    if 'max_speed' in row:
        summary += f"Your maximum speed reached {row['max_speed']} km/h. "

    # Add sport-specific details
    if sport_type in ['ride', 'cycling']:
        summary += (
            f"Your average cadence was {row.get('average_cadence', 'N/A')} rpm. "
            f"Power output averaged {row.get('average_watts', 'N/A')} watts "
            f"(max {row.get('max_watts', 'N/A')}W, weighted average {row.get('weighted_average_watts', 'N/A')}W). "
        )
    return summary


def embed_summary(summary):
    """
    Generate an embedding for the given summary using a open-source model.

    Parameters:
        summary (str): The summary text to be embedded.

    Returns:
        list: The embedding vector for the summary.
    """
    try:
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L12-v2")
        embedding = model.encode(summary)
        logging.info("Successfully generated embedding.")
    except Exception as e:
        logging.error(f"Error generating embedding: {e}")

    return embedding
