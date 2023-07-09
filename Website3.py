import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Send a GET request to the website
url = "https://www.worldometers.info/coronavirus/country/india"
r = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(r.text, "html.parser")

# Extract the number of total cases
cases = soup.select('#maincounter-wrap > div > span')[0].text.replace(',', '')
Total_cases = int(cases)

# Extract the number of total deaths
deaths = soup.select('#maincounter-wrap > div > span')[1].text.replace(',', '')
Total_deaths = int(deaths)

# Extract the number of total recoveries
recovered = soup.select('#maincounter-wrap > div > span')[2].text.replace(',', '')
Total_recovered = int(recovered)

# Calculate the number of active cases
active = Total_cases - Total_deaths - Total_recovered

# Define the data for the bar graph
data = [active, Total_deaths, Total_recovered]
labels = ["Active", "Deaths", "Recovery"]
colors = ["red", "green", "blue"]

# Create a figure and an axes object
fig, ax = plt.subplots()

# Use the plt.bar() function to create the bar graph
plt.bar(labels, data, color=colors)

# Show the bar graph
plt.show()
