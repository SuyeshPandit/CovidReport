import requests
import matplotlib.pyplot as plt

# Send a GET request to the website
url = "https://api.covid19india.org/data.json"
response = requests.get(url)

# Extract the JSON data from the response
data = response.json()

# Fetch the latest COVID-19 statistics for India
latest_data = data["statewise"][0]

# Extract the required information
Total_cases = int(latest_data["confirmed"])
Total_deaths = int(latest_data["deaths"])
Total_recovered = int(latest_data["recovered"])

# Calculate the number of active cases
active = Total_cases - Total_deaths - Total_recovered

# Define the data for the bar graph
data = [active, Total_deaths, Total_recovered]
labels = ["Active", "Deaths", "Recovered"]
colors = ["red", "green", "blue"]

# Create a figure and an axes object
fig, ax = plt.subplots()

# Use the plt.bar() function to create the bar graph
plt.bar(labels, data, color=colors)

# Add labels to the bars
for i, v in enumerate(data):
    ax.text(i, v + 10000, str(v), ha="center")

# Show the bar graph
plt.title("COVID-19 Cases in India")
plt.xlabel("Category")
plt.ylabel("Number of Cases")
plt.show()
