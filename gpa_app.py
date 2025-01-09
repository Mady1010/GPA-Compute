import streamlit as st

# Setting up the Streamlit page
st.set_page_config(page_title="GPA Computing", page_icon="📘", layout="centered")
st.title("GPA COMPUTING")
st.write("Calculate your Semester and Overall GPA with ease.")

st.info("""
### Instructions:
1. Select the grade for each course from the dropdown menus provided.  
2. If Course 6 is not applicable, select "Null" from the dropdown menu.  
3. Enter your previous GPA (if available) to calculate the overall GPA.  
4. If you only wish to compute the Semester GPA, leave the "Old GPA" field empty.  
""")

# Define grades and their corresponding values
grades = {
    'A+': 4.0, 'A': 3.75, 'B+': 3.4, 'B': 3.0,
    'C+': 2.7, 'C': 2.3, 'C-': 2.0, 'D+': 1.7,
    'D': 1.3, 'D-': 1.0, 'F': 0.0, "Null": None
}


# GPA Calculation function
def calculate_gpa(course_grades, old_gpa, include_course_6=True):
    total_credits = 15 if not include_course_6 else 18
    course_points = sum(grades[grade] * 3 for grade in course_grades if grade != "Null")
    semester_gpa = round(course_points / total_credits, 3)
    overall_gpa = round((old_gpa + semester_gpa) / 2, 3) if old_gpa else semester_gpa
    return semester_gpa, overall_gpa

# User inputs
st.header("Enter Your Grades")
col1, col2 = st.columns(2)

with col1:
    course1 = st.selectbox("Course 1", options=list(grades.keys()), key="course1")
    course2 = st.selectbox("Course 2", options=list(grades.keys()), key="course2")
    course3 = st.selectbox("Course 3", options=list(grades.keys()), key="course3")

with col2:
    course4 = st.selectbox("Course 4", options=list(grades.keys()), key="course4")
    course5 = st.selectbox("Course 5", options=list(grades.keys()), key="course5")
    course6 = st.selectbox("Course 6", options=list(grades.keys()), key="course6")

old_gpa = st.number_input("Enter OLD GPA", min_value=0.0, max_value=4.0, step=0.10)

# Calculate GPA
if st.button("Calculate GPA"):
    include_course_6 = course6 != "Null"
    semester_gpa, overall_gpa = calculate_gpa(
        [course1, course2, course3, course4, course5, course6],
        old_gpa,
        include_course_6=include_course_6
    )
    st.success(f"Semester GPA: {semester_gpa}")
    st.info(f"Overall GPA: {overall_gpa}")

st.markdown(
    """
    <div style="bottom: 0; width: 100%; text-align: center; color: #dcdcdc; padding: 10px; font-size: 12px;">
        Created by <b>Mady</b> | © 2025 GPA Computing App
    </div>
    """,
    unsafe_allow_html=True
)