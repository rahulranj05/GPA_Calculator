import streamlit as st

# Mapping from letter grades to grade points
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

# Subject names and their credits
subjects = {
    "Transforms and Boundary Value Problems": 4,
    "Computer Organization and Architecture": 4,
    "Solid State Devices": 3,
    "Digital Logic Design": 3,
    "Electromagnetic Theory and Interference": 3,
    "Design Thinking and Methodology": 3,
    "Devices and Digital IC Laboratory": 2
}

# Streamlit UI
st.set_page_config(page_title="SRM GPA Calculator", page_icon="🎓")

st.title("🎓 SRM GPA Calculator")
st.markdown("Enter your letter grades for the following **7 subjects** to calculate your GPA.")

grades = {}

# Collect grades using dropdowns
for subject, credits in subjects.items():
    grades[subject] = st.selectbox(
        f"{subject} ({credits} credits)",
        ['O', 'A+', 'A', 'B+', 'B', 'C'],
        key=subject
    )

# Calculate GPA on button click
if st.button("Calculate GPA"):
    total_credits = 0
    total_weighted_points = 0

    for subject, grade in grades.items():
        credits = subjects[subject]
        grade_point = get_grade_point(grade)
        total_credits += credits
        total_weighted_points += grade_point * credits

    gpa = total_weighted_points / total_credits

    st.success(f"✅ Your GPA is: **{gpa:.3f}**")
    st.balloons()
