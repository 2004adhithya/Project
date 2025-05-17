import streamlit as st
st.title("Titanic Survivor")
st.header("Data Analysis")

pclass=st.number_input("Enter your class:")
sex=st.selectbox("Select sex :",["female","male"])
age=st.number_input("Enter your age:")
sibsp=st.number_input("Enter your sibsp:")
parch=st.number_input("Enter your parch:")
Fare=st.number_input("Enter your fare:")
Embarked=st.selectbox("Select Embarked:",["C","S"])

import joblib

classi=joblib.load(r'C:\Users\adhit\Titanic.pkl')
label1=joblib.load(r'C:\Users\adhit\lb.pkl')
label2=joblib.load(r'C:\Users\adhit\lb1.pkl')
stand=joblib.load(r'C:\Users\adhit\st.pkl')

sex=label1.transform([sex])[0]
Embarked=label2.transform([Embarked])[0]

if st.button("Predict"):
    result=classi.predict(stand.transform([[pclass,sex,age,sibsp,parch,Fare,Embarked]]))[0]
    st.success("The output is {}".format(result))
    if result==0:
       st.success("Dead".format(result))
    else:
       st.success("Alive".formst(result))
    