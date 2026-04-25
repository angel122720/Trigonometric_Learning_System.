import streamlit as st
import math
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Trigonometry Learning System", layout="wide")

# ---------------- SESSION STATE ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "quiz_q" not in st.session_state:
    st.session_state.quiz_q = None

# ---------------- UI ----------------
st.title("📐 Trigonometry Learning System")
st.caption("Interactive Learning Tool")

menu = st.sidebar.radio(
    "Menu",
    ["Home", "Trig Identities Explorer", "Derivatives", "Equation Solver", "Quiz"]
)

# ==================================================
# HOME
# ==================================================
if menu == "Home":
    st.header("Welcome 👋")
    st.write("Explore trigonometric identities, derivatives, equations, and quizzes interactively.")

# ==================================================
# IDENTITIES EXPLORER
# ==================================================
elif menu == "Identities Explorer":
    st.header("📘 Trigonometric Identities Explorer")

    expr = st.text_input("Enter trig function (sin, cos, tan, sec, csc, cot):")

    identities = {
        "sin": "sin²θ + cos²θ = 1 | tanθ = sinθ/cosθ",
        "cos": "cos²θ + sin²θ = 1 | secθ = 1/cosθ",
        "tan": "tanθ = sinθ/cosθ | 1 + tan²θ = sec²θ",
        "sec": "secθ = 1/cosθ | sec²θ = 1 + tan²θ",
        "csc": "cscθ = 1/sinθ | 1 + cot²θ = csc²θ",
        "cot": "cotθ = cosθ/sinθ | 1 + cot²θ = csc²θ"
    }

    if st.button("Show Identity"):
        key = expr.lower().strip()

        if key in identities:
            st.success("Identity Found:")
            st.write(identities[key])
        else:
            st.error("Invalid input. Try sin, cos, tan, sec, csc, cot.")

# ==================================================
# DERIVATIVES
# ==================================================
elif menu == "Derivatives":
    st.header("📈 Derivatives of Trigonometric Functions")

    func = st.selectbox("Choose function:", [
        "sin(x)", "cos(x)", "tan(x)", "sec(x)", "csc(x)", "cot(x)"
    ])

    derivatives = {
        "sin(x)": "cos(x)",
        "cos(x)": "-sin(x)",
        "tan(x)": "sec²(x)",
        "sec(x)": "sec(x)tan(x)",
        "csc(x)": "-csc(x)cot(x)",
        "cot(x)": "-csc²(x)"
    }

    st.success(f"d/dx {func} = {derivatives[func]}")

# ==================================================
# EQUATION SOLVER
# ==================================================
elif menu == "Equation Solver":
    st.header("🧩 Trigonometric Equation Solver")

    st.write("Format examples: sin(30), cos(60), tan(45)")

    eq = st.text_input("Enter expression:")

    if st.button("Solve"):
        try:
            eq = eq.lower().replace(" ", "")

            if "sin" in eq:
                val = float(eq.replace("sin(", "").replace(")", ""))
                result = math.sin(math.radians(val))

            elif "cos" in eq:
                val = float(eq.replace("cos(", "").replace(")", ""))
                result = math.cos(math.radians(val))

            elif "tan" in eq:
                val = float(eq.replace("tan(", "").replace(")", ""))
                result = math.tan(math.radians(val))

            else:
                st.error("Unsupported format. Use sin(30), cos(60), tan(45)")
                result = None

            if result is not None:
                st.success(f"Result = {round(result, 4)}")

        except:
            st.error("Invalid input format")

# ==================================================
# QUIZ SYSTEM (RANDOMIZED + GREEN BLINK)
# ==================================================
elif menu == "Quiz":
    st.header("🧠 Trigonometry Quiz (Randomized)")

    # ---------------- QUESTION BANK ----------------
    questions = [
        {
        "q": "What is the derivative of sin(x)?",
        "choices": ["cos(x)", "-sin(x)", "tan(x)", "-cos(x)"],
        "answer": "cos(x)"
        },
        {
        "q": "Derivative of cos(x)?",
        "choices": ["-sin(x)", "sin(x)", "cos(x)", "sec²(x)"],
        "answer": "-sin(x)"
        },
        {
        "q": "Derivative of tan(x)?",
        "choices": ["sec²(x)", "csc²(x)", "sec(x)", "tan(x)"],
        "answer": "sec²(x)" },
        {
        "q": "Derivative of sec(x)?",
        "choices": ["sec(x)tan(x)", "-sec(x)tan(x)", "csc(x)", "sec²(x)"],
        "answer": "sec(x)tan(x)"
        },
        {
        "q": "Derivative of csc(x)?",
        "choices": ["-csc(x)cot(x)", "csc(x)cot(x)", "sec(x)", "tan(x)"],
        "answer": "-csc(x)cot(x)"
        },
        {
        "q": "Derivative of cot(x)?",
        "choices": ["-csc²(x)", "csc²(x)", "-sec²(x)", "tan²(x)"],
        "answer": "-csc²(x)"
        },
        {
            "q": "What is the derivative of sin(x)?",
            "choices": ["cos(x)", "-sin(x)", "tan(x)"],
            "answer": "cos(x)"
        },
        {
            "q": "sin²θ + cos²θ = ?",
            "choices": ["0", "1", "2"],
            "answer": "1"
        },
        {
            "q": "Derivative of cos(x)?",
            "choices": ["-sin(x)", "cos(x)", "sec²(x)"],
            "answer": "-sin(x)"
        },
        {
            "q": "tan(x) equals?",
            "choices": ["sin(x)/cos(x)", "cos(x)/sin(x)", "1/sin(x)"],
            "answer": "sin(x)/cos(x)"
        },
        {
            "q": "1 + tan²(x) = ?",
            "choices": ["sec²(x)", "csc²(x)", "1"],
            "answer": "sec²(x)"
        }
         # ================= IDENTITIES =================
        {
        "q": "sin²θ + cos²θ = ?",
        "choices": ["1", "0", "2", "sinθ"],
        "answer": "1"
        },
        {
        "q": "1 + tan²θ = ?",
        "choices": ["sec²θ", "csc²θ", "1", "tan²θ"],
        "answer": "sec²θ"
        },
        {
        "q": "1 + cot²θ = ?",
        "choices": ["csc²θ", "sec²θ", "tan²θ", "1"],
        "answer": "csc²θ"
        },
        {
        "q": "secθ is equal to?",
        "choices": ["1/cosθ", "1/sinθ", "sinθ/cosθ", "cosθ/sinθ"],
        "answer": "1/cosθ"
        },
        {
        "q": "cscθ is equal to?",
        "choices": ["1/sinθ", "1/cosθ", "tanθ", "secθ"],
        "answer": "1/sinθ"
        },

    # ================= BASIC VALUES =================
        {
        "q": "sin(30°) = ?",
        "choices": ["1/2", "√3/2", "1", "0"],
        "answer": "1/2"
        },
        {
        "q": "cos(60°) = ?",
        "choices": ["1/2", "√3/2", "0", "1"],
        "answer": "1/2"
        },
        {
        "q": "tan(45°) = ?",
        "choices": ["1", "0", "√3", "1/2"],
        "answer": "1"
        },
        {
        "q": "sin(90°) = ?",
        "choices": ["1", "0", "-1", "1/2"],
        "answer": "1"
        },

    # ================= CONCEPTUAL =================
        {
        "q": "tan(x) is equal to?",
        "choices": ["sin(x)/cos(x)", "cos(x)/sin(x)", "1/sin(x)", "sin(x)cos(x)"],
        "answer": "sin(x)/cos(x)"
        },
        {
        "q": "cos²θ + sin²θ is always equal to?",
        "choices": ["1", "0", "2", "θ"],
        "answer": "1"
        }
        ]

    # ---------------- RANDOM QUESTION ----------------
    if st.session_state.quiz_q is None:
        st.session_state.quiz_q = random.choice(questions)

    q = st.session_state.quiz_q

    st.subheader(q["q"])

    answer = st.radio("Choose answer:", q["choices"])

    # ---------------- GREEN BLINK EFFECT ----------------
    def flash_green():
        box = st.empty()
        box.markdown(
            "<div style='background-color:green;height:200px'></div>",
            unsafe_allow_html=True
        )
        time.sleep(0.3)
        box.empty()

    # ---------------- SUBMIT ----------------
    if st.button("Submit Answer"):
        if answer == q["answer"]:
            st.session_state.score += 1
            st.success("Correct! 🎉")
            st.balloons()

            # new question
            st.session_state.quiz_q = random.choice(questions)

        else:
            st.error("Wrong Answer ❌")
            flash_green()

    st.write("🏆 Score:", st.session_state.score)

    if st.button("Next Question 🔄"):
        st.session_state.quiz_q = random.choice(questions)
