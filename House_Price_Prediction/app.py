import streamlit as st
import pandas as pd 
import joblib

st.set_page_config(page_icon="🏘️",page_title="HOUSEPRICEPREDICTION",layout="wide")
with open("RF_model.joblib","rb") as file:
    model=joblib.load(file)

df=pd.read_csv("Cleaned_df.csv")
    
st.title("HOUSE PRICE PREDICTION")
st.image("h1.jpg",width=300)


with st.sidebar:
    st.title("HOUSE PRICE PREDICTION")
    st.image("h1.jpg")
with st.container(border=True):
    col1,col2=st.columns(2)
    with col1:
        location=st.selectbox("LOCATION : ",options=df["location"].unique())
        sqft=st.number_input("SQ.FT : ",min_value=300)

    with col2:
        bath=st.selectbox("Number of Bathrooms : ",options=sorted(df["bath"].unique()))
        bhk=st.selectbox("Number of1 Bedrooms : ",options=sorted(df["bath"].unique()))
def get_encoded_Loc(location):
    for Loc,encoded in zip(df['location'],df['encoded_loc']):
        if location == Loc:
            return encoded
encode=get_encoded_Loc(location)

if st.button("PREDICT"):
    input_data=[[sqft,bath,bhk,encode]]
    prediction=model.predict(input_data)
    prediction=float(f'{prediction[0]:.2f}')
    st.title(f"Predicted Price: Rs. {prediction*100000}")
