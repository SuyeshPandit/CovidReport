import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://www.worldometers.info/coronavirus/country/india"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

# Use the correct BeautifulSoup module name, bs4
cases = soup.select('#maincounter-wrap > div > span')[0].text.replace(',', '')
Total_cases = int(cases)

deaths = soup.select('#maincounter-wrap > div > span')[1].text.replace(',', '')
Total_deaths = int(deaths)

recovered = soup.select('#maincounter-wrap > div > span')[2].text.replace(',', '')
Total_recovered = int(recovered)

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
