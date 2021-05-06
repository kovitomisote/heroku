import streamlit as st 
import pandas as pd
import plotly.express as px

data = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv')

def convert(x):
    year, week = x.split('-')
    year = (int(year) - 2020) * 54 
    return year + int(week)

data['week'] = data.year_week.apply(lambda x: convert(x))

countries = data['country'].unique()
country_choice = st.sidebar.selectbox('Select the country:', countries)

selected = data[data.country == country_choice]

fig = px.line(data_frame = selected, x = 'week', y = 'cumulative_count', color = 'indicator', )

st.title("My COVID app")
st.write(f'The selected country is {country_choice}')

st.plotly_chart(fig)

if st.checkbox("Show original dataset"):
    st.dataframe(data=selected)