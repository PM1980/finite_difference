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

st.title("Cubic Function Derivative Approximation")

t = st.slider("Evaluation point (t)", -5.0, 5.0, 2.0)
delta = st.slider("Delta (spacing between points)", 0.001, 1.0, 0.1)

exact = exact_derivative(t)
approximate = central_difference(t, delta)

st.write(f"Exact derivative at t = {t}: {exact:.2f}")
st.write(f"Approximate derivative at t = {t} (delta = {delta:.2f}): {approximate:.2f}")

t_values = np.linspace(-5, 5, 100)
delta_values = np.logspace(-3, 0, 10)

fig, ax = plt.subplots(figsize=(8, 6))
for delta in delta_values:
    approximations = [central_difference(t, delta) for t in t_values]
    ax.plot(t_values, approximations, label=f"delta = {delta:.2f}")

ax.plot(t_values, [exact_derivative(t) for t in t_values], 'k--', label="Exact derivative")
ax.set_xlabel("t")
ax.set_ylabel("Derivative")
ax.set_title("Cubic Function Derivative Approximation")
ax.legend()
st.pyplot(fig)
