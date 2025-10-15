
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_delta_timestamp( delta: int, unite="months") -> int:

    kwargs= {unite: delta}
    now = datetime.now()
    past_time = now - relativedelta(**kwargs)
    return int(past_time.timestamp())


def week_boundaries(date_str: str):
    """
    Retuns the monday (start) and Sunday (end) of the week for the given date.
    """
    date = datetime.strptime(date_str, "%Y/%m/%d")
    start = date - timedelta(days=date.weekday())
    end = start + timedelta(days=7)
    return int(start.timestamp()), int(end.timestamp())

def to_pace(speed):
    pace = 60 / speed if speed else 0
    minutes = int(pace)
    seconds = int(round((pace - minutes) * 60))
    return (minutes,seconds)


def generate_summary(row):
    # Basic activity description
    summary = (
        f"Activity on {row['date']} called {row['name']}: You completed a {row['distance_km']}km {row['type']} "
        f"with an average pace of {row['pace']} min/km and an average speed of {row['average_speed']} km/h. "
        f"The route had {row['elevation_gain_m']}m of elevation gain. "
    )

    # Performance metrics with context
    summary += (
        f"Performance details: "
        f"Your max speed was {row['max_speed_kmh']} km/h, and your average heart rate was {row['average_heartrate']} bpm (max: {row['max_heartrate']} bpm). "
        f"You burned approximately {row['calories_kcal']} kcal. "
    )

    # Cadence and power (if applicable)
    if row['type'] in ['ride', 'cycling']:
        summary += (
            f"Your average cadence was {row['avg_cadence_rpm']} rpm. "
            f"Power output: {row['average_watts']}W average, {row['max_watts']}W max, and {row['weighted_average_watts']}W weighted average. "
        )

        # Interpretive insights (optional but powerful for LLM)
    summary += (
        f"Insights: "
        f"This activity was {'your fastest' if row['pace'] < 5.0 else 'a moderate-paced'} {row['type']} this month. "
        f"Your heart rate suggests {'high intensity' if row['average_heartrate'] > 160 else 'moderate effort'}. "
        f"Consider {'rest' if row['average_heartrate'] > 170 else 'pushing harder next time'} based on your metrics."
    )
    return summary

