import streamlit as st
import plotly.express as px
st.title("Mi segunda publicacón")
st.write("Introducción")
st.write("Esta es la primera que me sale algo")

fig=px.bar(x=["A","B","C"],y=["2","5","6"])
st.plotly_chart(fig)