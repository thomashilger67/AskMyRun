
def generate_summary(row):
    # Basic activity description
    summary = (
        f"Activity on {row['start_date']} called {row['name']}: You completed a {row['distance']}km {row['type']} "
        f"with an average pace of {row['pace']} min/km and an average speed of {row['average_speed']} km/h. "
        f"The route had {row['total_elevation_gain']}m of elevation gain. "
    )

    # Performance metrics with context
    summary += (
        f"Performance details: "
        f"Your max speed was {row['max_speed']} km/h, and your average heart rate was {row['average_heartrate']} bpm (max: {row['max_heartrate']} bpm). "
    )

    # Cadence and power (if applicable)
    if row['type'] in ['ride', 'cycling']:
        summary += (
            f"Your average cadence was {row['average_cadence']} rpm. "
            f"Power output: {row['average_watts']}W average, {row['max_watts']}W max, and {row['weighted_average_watts']}W weighted average. "
        )

    summary += (
        f"Metadata: "
        f"distance_km={row['distance']}, pace_min_per_km={row['pace']}, "
        f"elevation_gain_m={row['total_elevation_gain']}, type={row['type']}, "
        f"start_date={row['start_date']}, average_heartrate={row['average_heartrate']}, "
        f"max_speed_kmh={row['max_speed']}, average_speed_kmh={row['average_speed']}"
    )

    return summary