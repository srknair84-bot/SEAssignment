import streamlit as st


st.title("Welcome to the CAIE Course Program")

    # Add more functionality here as needed
user_input = st.number_input("Enter your Mark:", max_value=100, min_value=0)
if st.button("Submit"):
    mark = user_input
    if mark >= 90 and mark <= 100:
        st.write("You have achieved an A grade!")
    elif mark >= 80 and mark < 90:
        st.write("You have achieved a B grade!")
    elif mark >= 70 and mark < 80:
        st.write("You have achieved a C grade!")
    elif mark >= 60 and mark < 70:
        st.write("You have achieved a D grade!") 
    elif mark < 60:
        st.write("You have achieved an E grade!")
    elif mark > 100 or mark < 0:
        st.write("Invalid mark. Please enter a mark between 0 and 100.")