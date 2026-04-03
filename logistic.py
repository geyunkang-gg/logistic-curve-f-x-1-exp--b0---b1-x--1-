import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Logistic Curve Explorer", page_icon="📈")
st.title("📈 Logistic Curve Explorer")
st.latex(r"f(x) = \frac{1}{1 + e^{-b_0 - b_1 x}}")

b0 = st.slider("b0 (intercept — shifts the curve left/right)", -6.0, 6.0, 0.0, 0.1)
b1 = st.slider("b1 (slope — controls steepness and direction)", -6.0, 6.0, 1.0, 0.1)

x = np.linspace(-8, 8, 500)
f = 1 / (1 + np.exp(-b0 - b1 * x))

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, f, color="#2563eb", lw=2.5, label=f"b0={b0:.1f}, b1={b1:.1f}")
ax.axhline(0.5, color="gray", ls="--", alpha=0.5, label="f(x) = 0.5")

if b1 != 0:
    x_star = -b0 / b1
    if -8 <= x_star <= 8:
        ax.axvline(x_star, color="tomato", ls=":", alpha=0.8,
                   label=f"Inflection point x* = {x_star:.2f}")
        ax.plot(x_star, 0.5, "o", color="tomato", ms=8)

ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("f(x)", fontsize=12)
ax.set_title(f"Logistic Curve (b0={b0:.1f}, b1={b1:.1f})", fontsize=13)
ax.set_ylim(-0.05, 1.05)
ax.legend()
ax.grid(alpha=0.3)
st.pyplot(fig)

st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("b0", f"{b0:.2f}")
col2.metric("b1", f"{b1:.2f}")
if b1 != 0:
    col3.metric("Inflection point x*", f"{-b0/b1:.2f}")
else:
    col3.metric("Inflection point x*", "undefined (b1=0)")
