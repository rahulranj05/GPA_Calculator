import streamlit as st

# Streamlit app configuration
st.set_page_config(page_title="GPA Calculator", layout="centered")

# Title and Author
st.title("📊 GPA Calculator (SRM University)")
st.caption("**- by Rahul Ranjan ECE - DS - A**")

# Grade to Grade Point Map
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

# Subjects and their credits
subjects = {
    "Transforms and Boundary Value Problems": 4,
    "Computer Organization and Architecture": 4,
    "Solid State Devices": 3,
    "Digital Logic Design": 3,
    "Electromagnetic Theory and Interference": 3,
    "Design Thinking and Methodology": 3,
    "Devices and Digital IC Laboratory": 2
}

st.markdown("---")
st.subheader("Enter your Grades")

grades = {}
for subject, credits in subjects.items():
    grade = st.selectbox(
        f"{subject} ({credits} credits)",
        options=["O", "A+", "A", "B+", "B", "C"],
        key=subject
    )
    grades[subject] = grade

if st.button("Calculate GPA"):
    total_credits = 0
    total_weighted_points = 0

    for subject, grade in grades.items():
        credits = subjects[subject]
        grade_point = get_grade_point(grade)
        total_credits += credits
        total_weighted_points += grade_point * credits

    gpa = total_weighted_points / total_credits
    st.success(f"🎓 Your GPA is: **{gpa:.3f}**")

st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Made with ❤️ by Rahul Ranjan ECE - DS - A</div>", unsafe_allow_html=True)
