import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Trig Learning Lab", layout="wide")

# ------------------ MODERN UI ------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1e1e2f, #2b5876);
    color: white;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SESSION STATE ------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# ------------------ TITLE ------------------
st.title("🎯 Trigonometry Learning Lab")
st.caption("Interactive • Discovery-Based • ADDIE Model")

# ------------------ ANALYSIS ------------------
st.sidebar.header("📊 Analysis Phase")
level = st.sidebar.selectbox("Select your level:", ["Beginner", "Intermediate", "Advanced"])

menu = st.sidebar.radio(
    "📌 Menu",
    ["🏠 Home", "📐 Explore", "📘 Identities", "📈 Derivatives", "🧮 Calculator", "🧩 Equation Solver", "🧠 Quiz", "📊 Progress"]
)

# ------------------ HOME ------------------
if menu == "🏠 Home":
    st.header("Welcome!")
    st.write(f"Level: {level}")
    st.info("Explore, compute, and learn trigonometry interactively!")

# ------------------ EXPLORE ------------------
elif menu == "📐 Explore":
    angle = st.slider("Angle (degrees)", 0, 360, 30)
    rad = math.radians(angle)

    st.metric("sin(x)", round(math.sin(rad), 4))
    st.metric("cos(x)", round(math.cos(rad), 4))
    st.metric("tan(x)", round(math.tan(rad), 4))

    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)

# ------------------ IDENTITIES ------------------
elif menu == "📘 Identities":
    angle = st.slider("Angle", 0, 360, 45)
    rad = math.radians(angle)

    result = math.sin(rad)**2 + math.cos(rad)**2

    st.latex(r"\sin^2(x) + \cos^2(x)")
    st.write("Result:", round(result, 4))

    if abs(result - 1) < 0.001:
        st.success("Verified!")
    else:
        st.error("Try again")

# ------------------ DERIVATIVES ------------------
elif menu == "📈 Derivatives":
    func = st.selectbox("Function", ["sin(x)", "cos(x)", "tan(x)"])

    derivatives = {
        "sin(x)": r"\cos(x)",
        "cos(x)": r"-\sin(x)",
        "tan(x)": r"\sec^2(x)"
    }

    st.latex(r"\frac{d}{dx} " + func + " = " + derivatives[func])

# ------------------ CALCULATOR ------------------
elif menu == "🧮 Calculator":
    mode = st.selectbox("Mode", ["Evaluate", "Simplify", "Derivative"])

    x = sp.symbols('x')

    expr = st.text_input("Enter expression:")

    if st.button("Run"):
        try:
            if mode == "Evaluate":
                expr_eval = expr.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
                result = eval(expr_eval.replace("(", "(math.radians("))
                st.success(result)

            elif mode == "Simplify":
                st.success(sp.simplify(expr))

            elif mode == "Derivative":
                st.success(sp.diff(expr, x))
        except:
            st.error("Invalid input")

# ------------------ EQUATION SOLVER ------------------
elif menu == "🧩 Equation Solver":
    st.header("Solve Trig Equation")

    eq = st.text_input("Example: sin(x) - 0.5")

    if st.button("Solve"):
        try:
            x = sp.symbols('x')
            solution = sp.solve(eq, x)
            st.success(f"Solutions: {solution}")
        except:
            st.error("Invalid equation")

# ------------------ QUIZ ------------------
elif menu == "🧠 Quiz":
    st.session_state.attempts += 1

    ans = st.radio("Derivative of sin(x)?", ["cos(x)", "-sin(x)", "sec^2(x)"])

    if st.button("Submit"):
        if ans == "cos(x)":
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error("Wrong!")

# ------------------ PROGRESS ------------------
elif menu == "📊 Progress":
    st.header("Your Progress")

    st.write("Score:", st.session_state.score)
    st.write("Attempts:", st.session_state.attempts)

    if st.session_state.attempts > 0:
        percent = (st.session_state.score / st.session_state.attempts) * 100
        st.progress(percent / 100)
        st.write(f"Accuracy: {round(percent,2)}%")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("ADDIE Model Integrated Learning System")