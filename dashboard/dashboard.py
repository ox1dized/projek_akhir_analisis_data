import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'new_day_data.csv'
df = pd.read_csv(file_path)

df.drop(columns=['Unnamed: 0'], inplace=True)

df['date'] = pd.to_datetime(df['date'])

st.sidebar.header("Filter Data")

year = st.sidebar.selectbox("Select Year", options=sorted(df['year'].unique()))
month = st.sidebar.selectbox("Select Month", options=sorted(df['month'].unique()))
weather = st.sidebar.multiselect("Select Weather Condition", options=df['weather'].unique(), default=df['weather'].unique())
season = st.sidebar.multiselect("Select Weather Condition", options=df['season'].unique(), default=df['season'].unique())

filtered_data = df[(df['year'] == year) & (df['month'] == month) & (df['weather'].isin(weather)) & (df['season'].isin(weather))]

st.title("Bike Sharing Dashboard")

st.subheader("Total Users Over Time")
fig, ax = plt.subplots()
ax.plot(filtered_data['date'], filtered_data['total'], marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Total Users")
st.pyplot(fig)

st.subheader("Summary Statistics")
st.write(filtered_data[['casual', 'registered']].describe())

st.subheader("Casual vs Registered Users")
fig, ax = plt.subplots()
ax.bar(filtered_data['date'], filtered_data['casual'], label="Casual Users", color='orange')
ax.bar(filtered_data['date'], filtered_data['registered'], label="Registered Users", bottom=filtered_data['casual'], color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Number of Users")
ax.legend()
st.pyplot(fig)