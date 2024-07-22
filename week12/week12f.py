# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2016, 1, 1)
end = datetime(2018, 8, 3)

# Create Point for Vancouver, BC
location = Point(40.12728, -76.13772)

# Get daily data for 2018
data = Daily(location, start, end)
data = data.fetch()

print(data)
# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg'])
plt.show()
