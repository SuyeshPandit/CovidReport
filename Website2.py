import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Read the HTML table from the website
data = pd.read_html('https://prsindia.org/covid-19/cases')
Corona_cases = data[0]

# Save the data to a CSV file
Corona_cases.to_csv("corona_case_statewise.csv", index=False)

# Read the CSV file into a DataFrame
Corona_cases = pd.read_csv("corona_case_statewise.csv")

# Display the first and last few rows of the DataFrame
Corona_cases.head()
Corona_cases.tail()

# Display information about the DataFrame
Corona_cases.info()

# Remove unnecessary columns
Corona_cases = Corona_cases.drop(["Unnamed: 0", "#"], axis=1)

# Drop the row with index 36
Corona_cases = Corona_cases.drop(36, inplace=False)

# Display the first few rows of the cleaned DataFrame
Corona_cases.head()

# Get the top 5 states with the highest number of deaths
top_5_deaths = Corona_cases.sort_values("Death", ascending=False).head(5)

# Plot a bar chart for the top 5 states with the highest number of deaths
sns.barplot(x="State/UT", y="Death", data=top_5_deaths)
plt.xlabel("States")
plt.ylabel("Number of Deaths")
plt.title("Top 5 States with the Highest Number of Deaths")
plt.show()

# Get the top 5 states with the highest number of active cases
top_5_active_cases = Corona_cases.sort_values("Active Cases", ascending=False).head(5)

# Plot a bar chart for the top 5 states with the highest number of active cases
sns.barplot(x="State/UT", y="Active Cases", data=top_5_active_cases)
plt.xlabel("States")
plt.ylabel("Number of Active Cases")
plt.title("Top 5 States with the Highest Number of Active Cases")
plt.show()

# Rename the columns for better readability
Corona_cases.columns = ['State/UT', 'Confirmed Cases', 'Active Cases', 'Cured/Discharged', 'Deaths']

# Plot a bar chart for confirmed cases by state using Plotly
fig = px.bar(Corona_cases, x='State/UT', y='Confirmed Cases', width=800, height=800)
fig.show()

# Plot a scatter chart for confirmed cases vs. cured/discharged cases using Plotly
fig = px.scatter(Corona_cases, x="Confirmed Cases", y="Cured/Discharged", width=800, height=400)
fig.show()
