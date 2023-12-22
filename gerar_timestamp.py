from datetime import datetime

import pytz

def gerar_timestamp():
    """
    Function to generate a timestamp string.

    Returns:
    - A timestamp string in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    timezone = pytz.timezone('America/Fortaleza')
    utc_now = datetime.utcnow()
    utc_now = utc_now.replace(tzinfo=pytz.utc)
    local_now = utc_now.astimezone(timezone)
    timestamp = local_now.strftime('%Y-%m-%d %H:%M:%S')

    return timestamp
