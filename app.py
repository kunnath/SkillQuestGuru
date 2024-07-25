import streamlit as st
import mysql.connector
from datetime import datetime, timedelta


# Establish MySQL connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="extracurricular_activities_db"
)
db_cursor = db_connection.cursor(dictionary=True)  # Use dictionary cursor

# Fetch activity types from database
db_cursor.execute("SELECT * FROM ActivityTypes")
activity_types = [row['name'] for row in db_cursor.fetchall()]


# Function to insert student data into MySQL
def insert_student_data(name, interests, talents, age):
    insert_query = "INSERT INTO students (name, interests, talents, age) VALUES (%s, %s, %s, %s)"
    student_data = (name, interests, talents, age)
    db_cursor.execute(insert_query, student_data)
    db_connection.commit()

# Streamlit application code with database integration
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
if page == 'Find Clubs':
    st.header('Find Clubs and Activities')

    # Fetch activity types from database
    db_cursor.execute("SELECT * FROM ActivityTypes")
    activity_types = [row['name'] for row in db_cursor.fetchall()]

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

# Talent Assessment page content
elif page == 'Talent Assessment':
    st.header('Talent Assessment')

    st.markdown("""
        Assess your child's talents and interests to find suitable clubs.
        Fill out the following details to get started:
    """)

    # Form to assess talents and interests
    with st.form('talent_assessment_form'):
        st.subheader('Child\'s Interests')
        interests_sports = st.checkbox('Sports')
        interests_arts = st.checkbox('Arts & Crafts')
        interests_music = st.checkbox('Music & Dance')
        interests_tech = st.checkbox('Technology & Coding')
        interests_other = st.text_input('Other Interests')

        st.subheader('Child\'s Talents')
        talents_leadership = st.checkbox('Leadership')
        talents_creativity = st.checkbox('Creativity')
        talents_problem_solving = st.checkbox('Problem-solving')
        talents_performing_arts = st.checkbox('Performing Arts')
        talents_academic_excellence = st.checkbox('Academic Excellence')
        talents_other = st.text_input('Other Talents')

        st.subheader('Family Situation')
        preferred_schedule = st.selectbox('Preferred Days and Times', ['Weekdays after school', 'Weekends', 'Specific weekday evenings', 'Flexible schedule'])

        st.subheader('Parental Preferences')
        outcomes = st.multiselect('Desired Outcomes', ['Skill development', 'Social interaction', 'Academic improvement', 'Physical fitness', 'Others'])

        if st.form_submit_button('Get Recommendations'):
            # Placeholder for recommendation logic based on assessment
            st.success('Recommendations will be shown here.')

# Parent Dashboard page content
elif page == 'Parent Dashboard':
    st.header('Parent Dashboard')

    # Manage child profiles
    with st.expander('Manage Child Profiles', expanded=True):
        child_name = st.text_input('Child\'s Name')
        child_age = st.number_input('Child\'s Age', min_value=1, max_value=18)
        child_interests = st.text_area('Child\'s Interests')
        
        if st.button('Add Child'):
            if child_name:
                st.session_state[child_name] = {'age': child_age, 'interests': child_interests}
                st.success(f'Added child: {child_name}')

        # Display current child profiles
        st.subheader('Current Child Profiles')
        for child, profile in st.session_state.items():
            if isinstance(profile, dict):
                st.write(f"**{child}** - Age: {profile['age']}, Interests: {profile['interests']}")

    # Communication with clubs
    with st.expander('Communication with Clubs', expanded=True):
        selected_club = st.selectbox('Select Club', ['Sports Academy', 'Art Studio', 'Music School'])
        message = st.text_area('Message to Club')

        communication_status = st.radio('Communication Status', ['Pending', 'Contacted', 'Meeting Scheduled', 'Follow-up Needed'])

        # Default value for next_communication_date
        default_date = datetime.today() + timedelta(days=7)
        next_communication_date = st.date_input('Next Communication Date', default_date)

        if st.button('Update Communication Status'):
            st.success(f'Communication status updated for {selected_club}.')

    # Track activity schedules
    with st.expander('Track Activity Schedules', expanded=False):
        st.write("""
            Here you can track your child's activity schedules and upcoming events.
            This feature will be available soon.
        """)

# Student Information Form page content
elif page == 'Student Information Form':
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