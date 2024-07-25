import streamlit as st
import mysql.connector

# Establish MySQL connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="password",
    database="extracurricular_activities_db"
)
db_cursor = db_connection.cursor()

# Function to insert student data into MySQL
def insert_student_data(name, interests, talents, age):
    insert_query = "INSERT INTO students (name, interests, talents, age) VALUES (%s, %s, %s, %s)"
    student_data = (name, interests, talents, age)
    db_cursor.execute(insert_query, student_data)
    db_connection.commit()

# Streamlit application code with database integration
st.title('Student Information Form')

# Form to collect student information
with st.form('student_info_form'):
    st.subheader('Enter Student Information')
    name = st.text_input('Name')
    interests = st.text_input('Interests')
    talents = st.text_input('Talents')
    age = st.number_input('Age', min_value=1, max_value=18)
    
    if st.form_submit_button('Submit'):
        insert_student_data(name, interests, talents, age)
        st.success('Student information successfully submitted.')

# Close MySQL connection
db_cursor.close()
db_connection.close()