import streamlit as st
from datetime import datetime, timedelta
# Define URLs for video and image
your_video_url = '/Users/kunnath/Projects/Talentfinder/sports.mov'
your_image_url_or_path = '/Users/kunnath/Projects/Talentfinder/Screenshot1.png'

# Title and sidebar navigation
st.set_page_config(page_title="Extracurricular Activities Platform", layout="wide")

# Define sidebar navigation and main page content
sidebar_options = ['Home', 'Find Clubs', 'Talent Assessment', 'Parent Dashboard']
page = st.sidebar.radio('Navigation', sidebar_options)

# Main page header with image
st.title('Extracurricular Activities Platform')
st.image(your_image_url_or_path, width=300)  # Adjust width as per your layout needs

# Home page content
if page == 'Home':
    st.markdown("""
        ## Welcome to the Extracurricular Activities Platform!
        This platform helps parents find and manage activities for their kids.
        Choose a section from the sidebar to get started.
    """)
    st.video(your_video_url)  # Replace with your video URL

# Find Clubs page content
elif page == 'Find Clubs':
    st.header('Find Clubs and Activities')

    # Filters for searching clubs
    with st.expander("Search Filters", expanded=True):
        activity_type = st.selectbox('Activity Type', ['Any', 'Sports', 'Arts', 'Music', 'Dance'])
        location = st.text_input('Location', 'Berlin')

    # Display clubs based on filters (placeholder)
    st.subheader('Clubs in Berlin')
    clubs_data = [
        {'name': 'Sports Academy', 'activity_type': 'Sports', 'location': 'Berlin'},
        {'name': 'Art Studio', 'activity_type': 'Arts', 'location': 'Berlin'},
        {'name': 'Music School', 'activity_type': 'Music', 'location': 'Berlin'},
    ]

    for club in clubs_data:
        if activity_type == 'Any' or activity_type == club['activity_type']:
            st.write(f"**{club['name']}** - {club['activity_type']} - Location: {club['location']}")

    # Student statistics in Berlin
    st.subheader('Student Statistics in Berlin')
    st.bar_chart({'Sports': 50, 'Arts': 30, 'Music': 40})  # Example data, replace with actual statistics

# Talent Assessment page content
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
            
             # Questions to assess talents and interests
    st.subheader('Child\'s Interests')
    interests = st.multiselect('Select Interests', ['Sports', 'Arts & Crafts', 'Music & Dance', 'Technology & Coding'])

    st.subheader('Child\'s Talents')
    talents = st.multiselect('Select Talents', ['Leadership', 'Creativity', 'Problem-solving', 'Performing Arts', 'Academic Excellence'])

    # Simulated database of kids with talents and interests
    kids_data = [
        {'name': 'Emma', 'interests': ['Sports', 'Arts & Crafts'], 'talents': ['Creativity', 'Leadership']},
        {'name': 'Liam', 'interests': ['Music & Dance'], 'talents': ['Performing Arts', 'Creativity']},
        {'name': 'Olivia', 'interests': ['Sports', 'Technology & Coding'], 'talents': ['Problem-solving', 'Leadership']}
    ]

    # Placeholder logic to find similar kids
    similar_kids = []
    for kid in kids_data:
        if set(interests).issubset(kid['interests']) and set(talents).issubset(kid['talents']):
            similar_kids.append(kid['name'])

    # Display recommendations
    st.subheader('Recommendations')
    if similar_kids:
        st.success(f"We found similar kids: {', '.join(similar_kids)}")
    else:
        st.warning('No similar kids found.')


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

# Footer
st.sidebar.text('© 2024 Extracurricular Activities Platform')