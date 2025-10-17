import streamlit as st
import pickle

model =pickle.load(open("C:\Users\shali\Downloads\sdemo\model_final.pkl","rb"))

st.header("Welcome to Iris predictor ")
sl = st.number_input("Sepal Length")
sw = st.number_input("sepal width")
pw = st.number_input("petal width")
pl = st.number_input("petal length")

if st.button("predict"):
    prediction = model.predict([[sl, sw, pl, pw]])
    st.success(f"predicted species:{prediction[0]}")

