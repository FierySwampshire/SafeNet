import streamlit as st
import leafmap.foliumap as leafmap
import numpy.random as random
import pandas as pd
import plotly.express as px
from numba import calculate_percentile
import requests
from pylocation import parse_dump

st.set_page_config(layout="wide")
df = st.cache(pd.read_csv)("final_df.csv")

st.image("logo_2.png", use_column_width=True)

st.title("DashBoard")

col1, col2 = st.columns(2)

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Patch_of_the_New_York_City_Police_Department.svg/1200px-Patch_of_the_New_York_City_Police_Department.svg.png", width=400)

with col2:
    st.title("City: New York")
    st.title("ID: 700151")
    st.markdown("<br>", unsafe_allow_html=True)
    st.metric(label="Crime Index", value=df.get("crime_index")[-1], delta=df.get('crime_index')[0]-df.get("crime_index")[-1])

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    grades_cols = [cols for cols in df.columns if "historic_crime_rate" in cols]
    st.line_chart(list(df[historic_crime_rate].values[0][:-2]))

    # histogram using plotly bar:
    st.plotly_chart(px.histogram(calculate_percentile(grades_cols[current_crime_index]), nbins=10, title="Data"), use_container_width=True)

with col4:
    def get_crime_locations():
        locations = requests.get("https://safenet.hop.sh/get_locations")
        return locations
    m = leafmap.Map()
    m.add_marker(parse_dump(get_crime_locations()))
    m.to_streamlit(height=750)

col9, col10, col12 = st.columns((1, 1, 2))


with col9:
    st.metric(label="Name", value=df.get("city_name")[-1])
    st.metric(label="ID", value=df.get("city_id")[-1])
    st.metric(label="CrimeIndex", value=df.get("crime_index")[-1], delta=df.get('crime_index')[0]-df.get("crime_index")[-1])
    st.metric(label="Stat", value=round(df["risk"].values[0], 2))
with col10:
    st.metric(label="Stat", value=df.get("crime_moore_score")[-1])"))
    st.metric(label="Stat", value=df.get("percentile_preset")[-1])"))
    st.metric(label="Stat", value=df.get("p")[-1])"))
with col12:
    rand_data = random.normal(50, 50 / 3, 1000)
    # remove points below 0 and above 100:
    rand_data = [x for x in rand_data if x > 0 and x < 100]

    # change the color of the second bar to red:
    st.plotly_chart(px.histogram(rand_data, title="Data"), use_container_width=True)