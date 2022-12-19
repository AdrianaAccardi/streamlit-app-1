#-------------------#
# SETUP
import streamlit as st
import pandas as pd
import altair as alt

#-------------------#
# IMPORT DATA

df = pd.read_csv("https://raw.githubusercontent.com/eo026/homework-1/main/data/external/data.csv")


###-------------------###
# START OF OUR APP

#-------------------#
# HEADER

# Title of our app
st.title("Dashboard")

# Add image
st.image('hdm-logo.jpg')

# Add header
st.header("Unsere Auswertung")

#-------------------#
# SIDEBAR

# Header
st.sidebar.header("Sidebar")

# Make a slider
satisfaction = st.sidebar.slider('Candidate', 0, 10, 1)

# Show output of slider selection
st.sidebar.write("XXXXX ", satisfaction, 'numbers')

#-------------------#
# BODY

st.write("Schauen wir uns die Daten genauer an")
# Show static DataFrame
st.dataframe(df)

st.write("Die Auswertung hat ergeben")
# Make a chart with altair




# Show plot
st.altair_chart(c, use_container_width=True)



###-------------------###
# END OF APP