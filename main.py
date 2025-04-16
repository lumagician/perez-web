import numpy as np
import pandas as pd

# Define location and time
latitude = 32.2
longitude = -111.0
times = pd.date_range('2023-06-21', periods=24, freq='H', tz='UTC')

# Simulate a simple solar zenith angle based on hour angle
def solar_zenith(hour):
    # Fake model: Zenith is minimum at solar noon (~12h), max at sunrise/sunset
    return abs(90 - (90 - abs(12 - hour) * 7))

zenith_angles = [solar_zenith(t.hour) for t in times]
data = pd.DataFrame({'time': times, 'zenith_angle': zenith_angles})
output = data.to_string(index=False)