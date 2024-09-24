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
st.title("Cubic Function Derivative Approximation")

col1, col2 = st.columns(2)

with col1:
    t = st.slider("Evaluation point (t)", -5.0, 5.0, 2.0)
    delta = st.slider("Delta (spacing between points)", 0.001, 5.0, 0.1)

    exact = exact_derivative(t)
    approximate = central_difference(t, delta)

    st.markdown(f"<p style='color:green;font-size:32px;'>Exact derivative: {exact:.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:red;font-size:32px;'>Approximate derivative: {approximate:.2f}</p>", unsafe_allow_html=True)

with col2:
    t_values = np.linspace(-5, 5, 100)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(t_values, [exact_derivative(t) for t in t_values], 'k--', label="Exact derivative")
    ax.plot(t_values, [central_difference(t, delta) for t in t_values], 'r-', label=f"Delta = {delta:.2f}")
    ax.set_xlabel("t")
    ax.set_ylabel("Derivative")
    ax.set_title("Cubic Function Derivative Approximation")
    ax.legend()
    st.pyplot(fig)
