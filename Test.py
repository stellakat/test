import streamlit as st
from PIL import Image

#### App Visuals
st.title("Are you a LinkedIn User?")

income = st.slider("Income (low=1 to high=9)", 1, 9)
education = st.slider("Level of Education (less than high school=1 to advanced degrees=8)", 1, 8)
parent = st.selectbox("Do you have children?", ('Yes', 'No'))
married = st.selectbox("Are you married?", ('Yes', 'No'))
female = st.selectbox("What gender do you identify as?", ('Male', 'Female'))
age = st.slider("How old are you?", 0, 130)
sm_li = st.selectbox("Do you use LinkedIn", ('Yes', 'No'))

#### LinkedIn
if sm_li == 'Yes':
    linked_label = "you are a LinkedIn User"
else:
    linked_label = "you are not a LinkedIn User"

#### Age
if age <= 16:
    age_label = "you are not a LinkedIn User"
elif age > 16 and age < 53:
    age_label = "you are a LinkedIn User"
else:
    age_label = "you are not a LinkedIn User"

#### Education
if education <= 3 and income <= 4:
    education_label = "you are not a LinkedIn User"
elif education >= 4 and income >= 5:
    education_label = "you are a LinkedIn User"
else:
    education_label = "you are a LinkedIn User"

st.write(f"According to the inputs above, we predict that {age_label}, your income and education level specifically indicate that {education_label}")
st.write(f"According to the inputs above {linked_label}")

