import streamlit as st
import math
import numpy as np

st.set_page_config(page_title="Trig Learning App", layout="wide")

# ---------------- SESSION STATE ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------- TITLE ----------------
st.title("🎯 Trigonometry Interactive Learning App")
st.caption("Discovery Learning + ADDIE Model")

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "Menu",
    ["Home", "Calculator", "Identities", "Derivatives", "Quiz"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.header("Welcome 👋")
    st.write("Explore trigonometry in a simple and interactive way!")

# ---------------- CALCULATOR ----------------
elif menu == "Calculator":
    st.header("🧮 Calculator (Degrees)")

    angle = st.number_input("Enter angle in degrees:", value=30.0)
    rad = math.radians(angle)

    if st.button("Compute"):
        st.success(f"sin({angle}) = {round(math.sin(rad),4)}")
        st.success(f"cos({angle}) = {round(math.cos(rad),4)}")
        st.success(f"tan({angle}) = {round(math.tan(rad),4)}")

# ---------------- IDENTITIES ----------------
elif menu == "Identities":
    st.header("📘 Identity Checker")

    angle = st.slider("Select angle", 0, 360, 45)
    rad = math.radians(angle)

    result = math.sin(rad)**2 + math.cos(rad)**2

    st.write("sin²(x) + cos²(x) = ", round(result, 4))

    if abs(result - 1) < 0.001:
        st.success("✔ Identity is TRUE (≈ 1)")
    else:
        st.error("Try again")

# ---------------- DERIVATIVES ----------------
elif menu == "Derivatives":
    st.header("📈 Derivatives")

    func = st.selectbox("Choose function", ["sin(x)", "cos(x)", "tan(x)"])

    if func == "sin(x)":
        st.latex(r"\frac{d}{dx} \sin(x) = \cos(x)")
    elif func == "cos(x)":
        st.latex(r"\frac{d}{dx} \cos(x) = -\sin(x)")
    elif func == "tan(x)":
        st.latex(r"\frac{d}{dx} \tan(x) = \sec^2(x)")

# ---------------- QUIZ (WITH BALLOONS 🎈) ----------------
elif menu == "Quiz":
    st.header("🧠 Quick Quiz")

    st.write("What is the derivative of sin(x)?")

    answer = st.radio("", ["cos(x)", "-sin(x)", "tan(x)"])

    if st.button("Submit Answer"):
        if answer == "cos(x)":
            st.session_state.score += 1
            st.success("Correct! 🎉 Great job!")

            # 🎈 BALLOON EFFECT
            st.balloons()

        else:
            st.error("Wrong answer. Try again!")

    st.write("Score:", st.session_state.score)
