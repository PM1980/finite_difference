import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def cubic_function(t):
    return t**3

def exact_derivative(t):
    return 3 * t**2

def central_difference(t, delta):
    x3 = cubic_function(t + delta)
    x1 = cubic_function(t - delta)
    return (x3 - x1) / (2 * delta)

st.set_page_config(layout="wide")
st.title("Aproximação da 1a derivada de uma função cúbica")

col1, col2 = st.columns(2)

with col1:
    t = st.slider("Ponto de avaliação (t)", -5.0, 5.0, 2.0)
    delta = st.slider("Delta (distância entre pontos)", 0.001, 1.0, 0.1)

    exact = exact_derivative(t)
    approximate = central_difference(t, delta)

    st.markdown(f"<p style='color:green;font-size:32px;'>Valor exato da derivada: {exact:.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:red;font-size:32px;'>Valor aproximado da derivada: {approximate:.2f}</p>", unsafe_allow_html=True)

    # Display the cubic function equation
    st.subheader("Equação da função cúbica")
    st.markdown(r"<span style='font-size:24px;'>$x(t) = t^3$</span>", unsafe_allow_html=True)

with col2:
    t_values = np.linspace(-5, 5, 100)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(t_values, [exact_derivative(t) for t in t_values], 'k--', label="derivada exata")
    ax.plot(t_values, [central_difference(t, delta) for t in t_values], 'r-', label=f"numerico - delta = {delta:.2f}")
    ax.set_xlabel("t")
    ax.set_ylabel("Derivada")
    ax.set_title("Aproximação da derivada da função cúbica")
    ax.legend()
    st.pyplot(fig)
