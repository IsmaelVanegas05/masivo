import streamlit as st
import plotly.express as px
st.title("Mi segunda publicacón")
st.write("Introducción")
st.write("Esta es la primera que me sale algo")

fig=px.bar(x=["A","B","C"],y=["2","5","6"])
st.plotly_chart(fig)

fig2=px.histogram(x=["A","B","C"],y=["2","5","6"])
st.plotly_chart(fig2)

fig3= px.pie(names=["1","2","3"],values=["7","6","3"],
            title="Distribuciones de Pesos en los Empleados")
st.plotly_chart(fig3)

fig4 = px.scatter(x=["1","2","3"],y=["7","6","3"], title="Correlacion de Peso y Edad")
st.plotly_chart(fig4)