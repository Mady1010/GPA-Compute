import streamlit as st


st.set_page_config(page_title="GPA Computing", page_icon="📘", layout="centered")
st.title("GPA COMPUTING")
st.write("Calculate your Semester and Overall GPA with ease.")

st.info("""
### Instructions:
1. If Course 6 is not applicable, select "Null" from the dropdown menu.
2. Enter your previous GPA (if available) to calculate the overall GPA.  
3. Enter your previous Credit Hours (num of Previous Courses * 3) to calculate the overall GPA.  
4. If you only wish to compute the Semester GPA, leave the "Old GPA" and "Previous Credit Hours" fields empty.  
""")


grades = {
    'A+': 4.0, 'A': 3.75, 'B+': 3.4, 'B': 3.0,
    'C+': 2.7, 'C': 2.3, 'C-': 2.0, 'D+': 1.7,
    'D': 1.3, 'D-': 1.0, 'F': 0.0, "Null": None
}



def calculate_gpa(course_grades, old_gpa, old_credit_hours, include_course_6=True):
    
    current_credits = 15 if not include_course_6 else 18

   
    course_points = sum(grades[grade] * 3 for grade in course_grades if grade != "Null")

   
    semester_gpa = round(course_points / current_credits, 3)

  
    if old_gpa and old_credit_hours:
        total_credits = old_credit_hours + current_credits
        weighted_gpa = ((old_gpa * old_credit_hours) + (semester_gpa * current_credits)) / total_credits
        overall_gpa = round(weighted_gpa, 3)
    else:
        overall_gpa = semester_gpa  

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
old_credit_hours = st.number_input("Enter Previous Credit Hours", min_value=0, step=1)

if st.button("Calculate GPA"):
    include_course_6 = course6 != "Null"
    semester_gpa, overall_gpa = calculate_gpa(
        [course1, course2, course3, course4, course5, course6],
        old_gpa,
        old_credit_hours,
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
