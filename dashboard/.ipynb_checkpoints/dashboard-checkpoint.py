import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'new_day_data.csv'
df = pd.read_csv(file_path)

# Drop the unnecessary index column
df.drop(columns=['Unnamed: 0'], inplace=True)

# Convert the date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Sidebar filters
st.sidebar.header("Filter Data")

year = st.sidebar.selectbox("Select Year", options=sorted(df['year'].unique()))
month = st.sidebar.selectbox("Select Month", options=sorted(df['month'].unique()))
weather = st.sidebar.multiselect("Select Weather Condition", options=df['weather'].unique(), default=df['weather'].unique())

# Filter data based on user selection
filtered_data = df[(df['year'] == year) & (df['month'] == month) & (df['weather'].isin(weather))]

# Main Dashboard
st.title("Bike Sharing Dashboard")

# Line chart of total users over time
st.subheader("Total Users Over Time")
fig, ax = plt.subplots()
ax.plot(filtered_data['date'], filtered_data['total'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Total Users")
st.pyplot(fig)

# Summary statistics for casual and registered users
st.subheader("Summary Statistics")
st.write(filtered_data[['casual', 'registered']].describe())

# Bar chart of casual vs registered users
st.subheader("Casual vs Registered Users")
fig, ax = plt.subplots()
ax.bar(filtered_data['date'], filtered_data['casual'], label="Casual Users", color='orange')
ax.bar(filtered_data['date'], filtered_data['registered'], label="Registered Users", bottom=filtered_data['casual'], color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Number of Users")
ax.legend()
st.pyplot(fig)