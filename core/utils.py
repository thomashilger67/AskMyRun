
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_delta_timestamp( delta: int, unite="months") -> int:

    kwargs= {unite: delta}
    now = datetime.now()
    past_time = now - relativedelta(**kwargs)
    return int(past_time.timestamp())