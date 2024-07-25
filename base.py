import streamlit as st
import mysql.connector
from datetime import datetime, timedelta

# Function to establish database connection
def get_database_connection():
    return mysql.connector.connect(
        host="your-rds-endpoint.amazonaws.com",  # Replace with your AWS RDS endpoint
        user="your-db-username",                 # Replace with your database username
        passwd="your-db-password",               # Replace with your database password
        database="extracurricular_activities_db"
    )

# Function to fetch activity types from database
def fetch_activity_types(cursor):
    cursor.execute("SELECT * FROM ActivityTypes")
    return [row['name'] for row in cursor.fetchall()]

# Function to insert student data into MySQL
def insert_student_data(cursor, name, interests, talents, age):
    insert_query = "INSERT INTO students (name, interests, talents, age) VALUES (%s, %s, %s, %s)"
    student_data = (name, interests, talents, age)
    cursor.execute(insert_query, student_data)

# Establish MySQL connection and cursor
with get_database_connection() as db_connection:
    db_cursor = db_connection.cursor(dictionary=True)  # Use dictionary cursor

    # Streamlit application code
    st.title('Extracurricular Activities Platform')
    st.image('./Screenshot1.png', width=300)  # Replace with your image path

    # Define sidebar navigation and main page content
    sidebar_options = ['Home', 'Find Clubs', 'Talent Assessment', 'Parent Dashboard', 'Student Information Form']
    page = st.sidebar.radio('Navigation', sidebar_options)

    # Home page content
    if page == 'Home':
        st.markdown("""
            ## Welcome to the Extracurricular Activities Platform!
            This platform helps parents find and manage activities for their kids.
            Choose a section from the sidebar to get started.
        """)
        st.video('./1.mov')  # Replace with your video URL

    # Find Clubs page content
    elif page == 'Find Clubs':
        st.header('Find Clubs and Activities')

        # Fetch activity types from database
        activity_types = fetch_activity_types(db_cursor)

        # Filters for searching clubs
        with st.expander("Search Filters", expanded=True):
            activity_type = st.selectbox('Activity Type', ['Any'] + activity_types)
            location = st.text_input('Location', 'Berlin')

        # Display clubs based on filters
        st.subheader(f'Clubs in {location}')
        if activity_type == 'Any':
            db_cursor.execute("SELECT * FROM Clubs WHERE location = %s", (location,))
        else:
            db_cursor.execute("SELECT * FROM Clubs c JOIN ActivityTypes a ON c.activity_type_id = a.id WHERE a.name = %s AND c.location = %s", (activity_type, location))

        clubs_data = db_cursor.fetchall()
        for club in clubs_data:
            st.write(f"**{club['name']}** - {activity_type} - Location: {club['location']}")

        # Student statistics in Berlin
        st.subheader('Student Statistics in Berlin')
        st.bar_chart({'Sports': 50, 'Arts': 30, 'Music': 40})  # Example data, replace with actual statistics

    # Talent Assessment page content (similar structure for other pages)
    elif page == 'Talent Assessment':
        st.header('Talent Assessment')

        # Form to assess talents and interests
        with st.form('talent_assessment_form'):
            # Form elements as before

            if st.form_submit_button('Get Recommendations'):
                # Placeholder for recommendation logic based on assessment
                st.success('Recommendations will be shown here.')

    # Student Information Form page content
    elif page == 'Student Information Form':
        st.title('Student Information Form')

        # Form to collect student information
        with st.form('student_info_form'):
            # Form elements as before

            if st.form_submit_button('Submit'):
                insert_student_data(db_cursor, name, interests, talents, age)
                db_connection.commit()
                st.success('Student information successfully submitted.')

# End of Streamlit application code

# No need to explicitly close cursor and connection due to context manager usage