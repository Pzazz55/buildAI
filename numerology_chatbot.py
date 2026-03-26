import streamlit as st
from datetime import datetime, date

# Function to calculate destiny number
def calculate_destiny_number(dob):
    total = dob.day + dob.month + dob.year
    while total > 9:
        total = sum(int(digit) for digit in str(total))
    return total

# Function to give career recommendations
def get_career_recommendation(destiny_number):
    rec = {
        1: "Leader, Entrepreneur, Innovator.",
        2: "Diplomat, Counselor, Supportive roles.",
        3: "Creative fields, Writing, Art, Entertainment.",
        4: "Organized, Engineer, Analyst, Researcher.",
        5: "Adventurer, Travel, Marketing, Sales.",
        6: "Careers in service, Teaching, Healing professions.",
        7: "Research, Spiritual work, Analyst, Scientist.",
        8: "Business, Management, Finance, Authority roles.",
        9: "Humanitarian, Social work, Art, Global causes."
    }
    return rec.get(destiny_number, "Unique path awaits you!")

# Streamlit App
st.set_page_config(page_title="Numerology Chatbot", layout="centered")
st.title("🔮 Numerology Chatbot")

st.write("Enter your Name and Date of Birth to get your Destiny Number and Career Recommendation!")

# Form with Name input + Date Picker restricted from 1/1/0001 to today
with st.form(key='dob_form'):
    name = st.text_input("Enter Your Name")
    dob = st.date_input(
        "Enter your Date of Birth",
        min_value=date(1, 1, 1),   # earliest selectable date
        max_value=date.today()      # latest selectable date
    )
    submit_button = st.form_submit_button(label='Get Destiny Number')

if submit_button:
    destiny_number = calculate_destiny_number(dob)
    st.success(f"Hello {name}, your Destiny Number is: {destiny_number}")
    st.info(f"Suggested Career Path: {get_career_recommendation(destiny_number)}")
