import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def quadratic_function(t, a, b, c):
    return a * t**2 + b * t + c

def cubic_function(t, a, b, c, d):
    return a * t**3 + b * t**2 + c * t + d

def exact_derivative_quadratic(t, a, b):
    return 2 * a * t + b

def exact_derivative_cubic(t, a, b, c):
    return 3 * a * t**2 + 2 * b * t + c

def central_difference(t, delta, func, *params):
    x3 = func(t + delta, *params)
    x1 = func(t - delta, *params)
    return (x3 - x1) / (2 * delta)

st.set_page_config(layout="wide")
st.title("Function Derivative Approximation")

col1, col2 = st.columns(2)

with col1:
    function_type = st.radio("Select function type", ("Quadratic", "Cubic"))

    if function_type == "Quadratic":
        a = st.number_input("a", value=1.0)
        b = st.number_input("b", value=2.0)
        c = st.number_input("c", value=1.0)
        t = st.slider("Evaluation point (t)", -5.0, 5.0, 2.0)
        delta = st.slider("Delta (spacing between points)", 0.001, 1.0, 0.1)

        displacement = quadratic_function(t, a, b, c)
        velocity = exact_derivative_quadratic(t, a, b)
        approximate_velocity = central_difference(t, delta, quadratic_function, a, b, c)

        st.markdown(f"<p style='color:green;font-size:32px;'>Displacement: {displacement:.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:green;font-size:32px;'>Exact velocity: {velocity:.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:red;font-size:32px;'>Approximate velocity: {approximate_velocity:.2f}</p>", unsafe_allow_html=True)

        displacement_equation = f"x(t) = {a:.2f}t^2 + {b:.2f}t + {c:.2f}"
        velocity_equation = f"v(t) = {2*a:.2f}t + {b:.2f}"
        st.write(f"Displacement equation: {displacement_equation}")
        st.write(f"Velocity equation: {velocity_equation}")

    elif function_type == "Cubic":
        a = st.number_input("a", value=1.0)
        b = st.number_input("b", value=2.0)
        c = st.number_input("c", value=1.0)
        d = st.number_input("d", value=0.0)
        t = st.slider("Evaluation point (t)", -5.0, 5.0, 2.0)
        delta = st.slider("Delta (spacing between points)", 0.001, 1.0, 0.1)

        displacement = cubic_function(t, a, b, c, d)
        velocity = exact_derivative_cubic(t, a, b, c)
        approximate_velocity = central_difference(t, delta, cubic_function, a, b, c, d)

        st.markdown(f"<p style='color:green;font-size:32px;'>Displacement: {displacement:.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:green;font-size:32px;'>Exact velocity: {velocity:.2f}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:red;font-size:32px;'>Approximate velocity: {approximate_velocity:.2f}</p>", unsafe_allow_html=True)

        displacement_equation = f"x(t) = {a:.2f}t^3 + {b:.2f}t^2 + {c:.2f}t + {d:.2f}"
        velocity_equation = f"v(t) = {3*a:.2f}t^2 + {2*b:.2f}t + {c:.2f}"
        st.write(f"Displacement equation: {displacement_equation}")
        st.write(f"Velocity equation: {velocity_equation}")

with col2:
    t_values = np.linspace(-5, 5, 100)

    fig, ax = plt.subplots(figsize=(8, 6))
    if function_type == "Quadratic":
        ax.plot(t_values, [exact_derivative_quadratic(t, a, b) for t in t_values], 'k--', label="Exact velocity")
        ax.plot(t_values, [central_difference(t, delta, quadratic_function, a, b, c) for t in t_values], 'r-', label=f"Delta = {delta:.2f}")
        ax.set_title("Quadratic Function Derivative Approximation")
    else:
        ax.plot(t_values, [exact_derivative_cubic(t, a, b, c) for t in t_values], 'k--', label="Exact velocity")
        ax.plot(t_values, [central_difference(t, delta, cubic_function, a, b, c, d) for t in t_values], 'r-', label=f"Delta = {delta:.2f}")
        ax.set_title("Cubic Function Derivative Approximation")

ax.set_xlabel("t")
ax.set_ylabel("Velocity")
ax.legend()
st.pyplot(fig)
