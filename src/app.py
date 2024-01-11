import streamlit as st 

st.title('Suma tres numeros')

st.write("## Usando `st.number_input`")

n1= st.number_input("Primer numero: ", step=1)
n2= st.number_input("Segundo numero: ", step=1)
n3= st.number_input("Tercer numero: ", step=1)

st.write("La suma de los tres numero es ",n1 + n2 + n3)

st.write("## Usando `st.slider`")

p1= st.slider("Primer numero: ")
p2= st.slider("Segundo numero: ")
p3= st.slider("Tercer numero: ")

st.write("La suma de los tres numero es ",p1 + p2 + p3)