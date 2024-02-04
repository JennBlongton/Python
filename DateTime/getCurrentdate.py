from datetime import *
import pytz

tz_india = pytz.timezone('ASIA/Kolkata')
datetime_india = datetime.now(tz_india)
print(datetime)
print("India Time:", datetime_india.strftime("%H:%M:%S"))