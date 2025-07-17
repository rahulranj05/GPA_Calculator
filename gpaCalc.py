import streamlit as st

# -------------------- Grade Mapping --------------------
def get_grade_point(letter_grade):
    grade_points_map = {
        'O': 10,
        'A+': 9,
        'A': 8,
        'B+': 7,
        'B': 6,
        'C': 5
    }
    return grade_points_map.get(letter_grade.upper(), 0)

# -------------------- Subject Data --------------------
subjects = {
    "Transforms and Boundary Value Problems": 4,
    "Computer Organization and Architecture": 4,
    "Solid State Devices": 3,
    "Digital Logic Design": 3,
    "Electromagnetic Theory and Interference": 3,
    "Design Thinking and Methodology": 3,
    "Devices and Digital IC Laboratory": 2
}

# -------------------- UI Layout --------------------
st.set_page_config(
    page_title="GPA Calculator - SRM",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

with st.container():
    st.markdown("<h2 style='text-align: center; color: white;'>SRM University - GPA Calculator</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #AAAAAA;'>Calculate your semester GPA based on your letter grades and subject credits.</p>", unsafe_allow_html=True)

st.divider()

# -------------------- Form --------------------
with st.form("gpa_form"):
    st.subheader("Enter Grades")
    grade_inputs = {}
    for subject, credits in subjects.items():
        grade_inputs[subject] = st.selectbox(
            f"{subject} ({credits} credits)",
            options=["O", "A+", "A", "B+", "B", "C"],
            key=subject
        )
    submit = st.form_submit_button("Calculate GPA")

# -------------------- GPA Calculation --------------------
if submit:
    total_credits = 0
    total_points = 0

    for subject, grade in grade_inputs.items():
        credits = subjects[subject]
        points = get_grade_point(grade)
        total_credits += credits
        total_points += points * credits

    gpa = total_points / total_credits

    st.divider()
    st.subheader("📈 GPA Result")
    st.markdown(f"<h3 style='color: #00FFAA;'>Your GPA: {gpa:.2f}</h3>", unsafe_allow_html=True)

    st.info("Note: GPA is calculated based on SRM standard 10-point grade scale.")

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>Developed by SRM student for fellow students</p>", unsafe_allow_html=True)
