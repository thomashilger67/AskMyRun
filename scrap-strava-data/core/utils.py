
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_delta_timestamp( delta: int, unite="months") -> int:

    kwargs= {unite: delta}
    now = datetime.now()
    past_time = now - relativedelta(**kwargs)
    return int(past_time.timestamp())


def week_boundaries(date_str: str):
    """
    Returns the monday (start) and Sunday (end) of the week for the given date.
    Parameters:
    - date_str (str): Date in "YYYY/MM/DD" format.
    Returns:
    - tuple: (start_timestamp, end_timestamp)
    """
    date = datetime.strptime(date_str, "%Y/%m/%d")
    start = date - timedelta(days=date.weekday())
    end = start + timedelta(days=7)
    return int(start.timestamp()), int(end.timestamp())

def to_pace(speed):
    """
    Convert speed (km/h) to pace (minutes, seconds per km).
    Parameters:
    - speed (float): Speed in kilometers per hour.
    Returns:
    - tuple (int): (minutes, seconds) per kilometer.
    """
    pace = 60 / speed if speed else 0
    minutes = int(pace)
    seconds = int(round((pace - minutes) * 60))
    return (minutes,seconds)
