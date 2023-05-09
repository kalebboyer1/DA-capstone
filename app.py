import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from PIL import Image



df = pd.read_csv("data.csv")
df1 = pd.read_csv("playerstats-salaries.csv")



st.title('Kaleb Boyer')
st.title(':red[DA Capstone]')
st.write("---")
st.subheader('Project Overview')
st.write(
    """
    For my capstone I decided to dive into a sport I love which is basketball and try to determine 
    which NBA players were overpaid and underpaid from the previous NBA season based on their personal stats.
    Not really knowing what conclusion I might find I started researching for good datasets that I could use. 
    It was challenging at first to find correct data to then start the cleaning process but once I was able to
    I quickly started piecing it all together. Taking stats from two different datasets and combining them was
    tricky but well worth the outcome.
    """
)
st.write("---")
st.subheader("Dataset Description")
st.write(
    """
    The NBA is all about statistics and money. Having a wide variety of stats I chose to take individual 
    season stats for each player and their salaries to determine whether or not they were overpaid or
    underpaid according to their performance.
    """
)

st.write("---")
st.subheader("Player Stats and Salary")
st.dataframe(df1)


st.write("---")

st.subheader("Player Salary difference")
st.dataframe(df)
st.write(
    """
    The dif column represents how much each player was either overpaid or underpaid. 
    Having a negative value signifies that the player was overpaid that amount. 
    A positive value means the player was underpaid by that amount.
    """
    )

    
st.write("---")

st.subheader('Coefficients')
image1 = Image.open(r"C:\Users\k__bo\OneDrive\Pictures\Screenshots\coefficient-titles.jpg")
st.image(image1)

image2 = Image.open(r"C:\Users\k__bo\OneDrive\Pictures\Screenshots\coefficients.jpg")
st.image(image2, caption="""For each title we have a corresponding value or coefficient. 
    Each coefficient displayed represents how each stat impacts the salary of a NBA player. 
    The more positive the value the more impact it has and the more negative the less impact 
    it has towards calculating salary.
    """)
st.subheader("OLS Summary")
image5 = Image.open(r"C:\Users\k__bo\OneDrive\Pictures\Screenshots\newOLS-data.jpg")
st.image(image5)
st.write(
    """
    In the summary we found all P-values to be under 0.05 which means they are all significant in deciding a 
    players salary. The R-squared is very close to 1.0 so we know that the variance in the dependent variable 
    can be explained by the independent variables shown here.

    """
)


st.write("---")
st.subheader("Top 10 Players who were overpaid")
st.table(df.head(10))
image3 = Image.open(r"C:\Users\k__bo\OneDrive\Pictures\Screenshots\top10players_overpaid.jpg")
st.image(image3)

st.subheader("Top 10 Players who were underpaid")
st.table(df.tail(10))
image4 = Image.open(r"C:\Users\k__bo\OneDrive\Pictures\Screenshots\top10players_underpaid.jpg")
st.image(image4)
st.write("---")

image6 = Image.open(r"C:\Users\k__bo\OneDrive\Pictures\Screenshots\top10scatterplot-cap.jpg")
st.image(image6, caption="Top 10 overpaid")
image7 = Image.open(r"C:\Users\k__bo\OneDrive\Pictures\Screenshots\randomscatter-cap.jpg")
st.image(image7, caption="30 Randomly selected Players")