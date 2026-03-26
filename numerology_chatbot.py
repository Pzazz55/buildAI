import streamlit as st
from datetime import date

# -----------------------------
# Chaldean Numerology Mapping
# -----------------------------
chaldean_map = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 8, 'G': 3, 'H': 5, 'I': 1,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 7, 'P': 8, 'Q': 1, 'R': 2,
    'S': 3, 'T': 4, 'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1, 'Z': 7
}

# -----------------------------
# Calculate Name Number
# -----------------------------
def calculate_name_number(name):
    name = name.upper()
    total = sum(chaldean_map.get(char, 0) for char in name)
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

# -----------------------------
# Calculate Destiny Number
# -----------------------------
def calculate_destiny_number(dob):
    total = dob.day + dob.month + dob.year
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

# -----------------------------
# Calculate Birth Number (from day)
# -----------------------------
def calculate_birth_number(day):
    birth_num = day % 9
    return 9 if birth_num == 0 else birth_num

# -----------------------------
# Career Recommendations
# -----------------------------
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

# -----------------------------
# Name Evaluation Rules
# -----------------------------
excellent_rules = {
    1: [1], 2: [1,6,7], 3: [1,3], 4: [1,5,6,9], 5: [9,5,4],
    6: [6,4,9], 7: [7,1,5], 8: [1,5], 9: [6,4]
}
verygood_rules = excellent_rules.copy()
average_rules = excellent_rules.copy()

def evaluate_name(destiny_number, birth_number, name_number):
    if destiny_number in excellent_rules and birth_number == destiny_number and name_number in excellent_rules[destiny_number]:
        return "Excellent"
    elif destiny_number in verygood_rules and name_number in verygood_rules[destiny_number]:
        return "Very-Good"
    elif birth_number in average_rules and name_number in average_rules[birth_number]:
        return "Average"
    else:
        return "Not Good"

# -----------------------------
# Color mapping
# -----------------------------
color_map = {
    "Excellent": "green",
    "Very-Good": "blue",
    "Average": "orange",
    "Not Good": "red"
}

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="Numerology Chatbot", layout="centered")
st.title("🔮 Numerology Chatbot")
st.write("Enter your Name and Date of Birth to get your Birth, Destiny, and Name Numbers, along with career guidance!")

with st.form(key='dob_form'):
    name = st.text_input("Enter Your Name")
    dob = st.date_input(
        "Enter your Date of Birth",
        min_value=date(1,1,1),
        max_value=date.today()
    )
    submit_button = st.form_submit_button(label="Get Numerology")

if submit_button:
    if not name:
        st.error("Please enter your name!")
    else:
        birth_number = calculate_birth_number(dob.day)
        destiny_number = calculate_destiny_number(dob)
        name_number = calculate_name_number(name)
        
        st.success(f"Hello {name}!")
        st.write(f"**Birth Number (Day of Birth):** {birth_number}")
        st.write(f"**Destiny Number:** {destiny_number}")
        st.write(f"**Name Number:** {name_number}")
        st.info(f"Suggested Career Path: {get_career_recommendation(destiny_number)}")

        # Evaluate Name
        evaluation = evaluate_name(destiny_number, birth_number, name_number)
        color = color_map[evaluation]
        
        if evaluation == "Not Good":
            st.markdown(f"<h3 style='color:{color}'>❌ Your Name needs evaluation. Consider consulting a professional Astrologer for Name Correction.</h3>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='color:{color}'>✅ Your Name Evaluation: {evaluation}</h3>", unsafe_allow_html=True)
