import streamlit as st
from datetime import date

# -----------------------------
# Helper: Reduce to single digit
# -----------------------------
def reduce_to_single_digit(num):
    while num > 9:
        num = sum(int(d) for d in str(num))
    return num

# -----------------------------
# Chaldean Numerology Mapping
# -----------------------------
chaldean_map = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 8, 'G': 3, 'H': 5, 'I': 1,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 7, 'P': 8, 'Q': 1, 'R': 2,
    'S': 3, 'T': 4, 'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1, 'Z': 7
}

# -----------------------------
# Name Number
# -----------------------------
def calculate_name_number(name):
    name = name.upper()
    total = sum(chaldean_map.get(c, 0) for c in name if c.isalpha())
    return reduce_to_single_digit(total)

# -----------------------------
# Destiny Number (FIXED)
# -----------------------------
def calculate_destiny_number(dob):
    total = dob.day + dob.month + dob.year
    return reduce_to_single_digit(total)

# -----------------------------
# Birth Number (FIXED)
# -----------------------------
def calculate_birth_number(day):
    return reduce_to_single_digit(day)

# -----------------------------
# Career Recommendation
# -----------------------------
def get_career_recommendation(num):
    careers = {
        1: "Leadership, Entrepreneurship, Management",
        2: "Diplomat, HR, Counsellor, Partnerships",
        3: "Creative, Media, Writing, Entertainment",
        4: "Engineering, Technology, Analyst",
        5: "Sales, Marketing, Travel, Communication",
        6: "Teaching, Healthcare, Hospitality",
        7: "Research, Data Science, Spiritual",
        8: "Business, Finance, Administration",
        9: "Humanitarian, NGO, Global Service"
    }
    return careers.get(num)

# -----------------------------
# Name Evaluation Rules
# -----------------------------
rules = {
    1: [1],
    2: [1,6,7],
    3: [1,3],
    4: [1,5,6,9],
    5: [9,5,4],
    6: [6,4,9],
    7: [7,1,5],
    8: [1,5],
    9: [6,4]
}

def evaluate_name(destiny, birth, name):
    if destiny == birth and name in rules.get(destiny, []):
        return "Excellent"
    elif name in rules.get(destiny, []):
        return "Very-Good"
    elif name in rules.get(birth, []):
        return "Average"
    else:
        return "Not Good"

# -----------------------------
# Path Number Data
# -----------------------------
path_data = {
    1: {"lucky":[1,10,19,28],"fav":[4,13,22,31],"stone":"Ruby, Yellow Sapphire","color":"Golden Color, Sky Blue, Yellow"},
    2: {"lucky":[2,11,20,29],"fav":[7,16,25],"stone":"Moonstone, Pearl","color":"White"},
    3: {"lucky":[3,12,21,30],"fav":[9,18,27],"stone":"Yellow Sapphire, Emerald","color":"Orange, Rose"},
    4: {"lucky":[4,13,22,31],"fav":[1,10,19,28],"stone":"Light Blue Sapphire","color":"Golden Color, Sky Blue"},
    5: {"lucky":[5,14,23],"fav":[9,18,27],"stone":"Diamond","color":"Sky Blue, Grey, Golden Color"},
    6: {"lucky":[6,15,24],"fav":[9,18,27],"stone":"Emerald","color":"Dark Green, Blue"},
    7: {"lucky":[7,16,25],"fav":[1,10,19,28],"stone":"Pearl","color":"White, Light Green"},
    8: {"lucky":[1,10,19,28],"fav":[4,13,22,31],"stone":"Dark Blue Sapphire","color":"Golden Color, Sky Blue"},
    9: {"lucky":[9,18,27],"fav":[1,10,19,28],"stone":"Coral","color":"Red, Dark Blue, Light Green"}
}

# -----------------------------
# Color Coding
# -----------------------------
color_map = {
    "Excellent":"green",
    "Very-Good":"blue",
    "Average":"orange",
    "Not Good":"red"
}

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Numerology AI", layout="centered")

st.title("🔮 Numerology AI Chatbot")

with st.form("numerology"):
    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth")
    submit = st.form_submit_button("Calculate")

if submit:

    birth_number = calculate_birth_number(dob.day)
    destiny_number = calculate_destiny_number(dob)
    name_number = calculate_name_number(name)

    st.markdown("---")
    st.subheader("🔢 Numerology Numbers")

    st.write(f"**Birth Number:** {birth_number}")
    st.write(f"**Destiny / Path Number:** {destiny_number}")
    st.write(f"**Name Number:** {name_number}")

    # Career
    st.info(f"💼 Career Recommendation: {get_career_recommendation(destiny_number)}")

    # Name evaluation
    evaluation = evaluate_name(destiny_number, birth_number, name_number)
    color = color_map[evaluation]

    st.markdown("---")

    st.markdown(
        f"<h2 style='color:{color}'>Name Evaluation : {evaluation}</h2>",
        unsafe_allow_html=True
    )

    if evaluation == "Not Good":
        st.error(
            "Your name is not aligned. Consider consulting professional astrologer for name change. 📞 +91 9611-961-111"
        )

    # Path number guidance
    data = path_data[destiny_number]

    st.markdown("---")
    st.subheader("🌟 Path Number Guidance")

    st.success(f"🍀 Lucky Dates: {data['lucky']}")
    st.info(f"👍 Favourable Dates: {data['fav']}")
    st.warning(f"💎 Lucky Stone: {data['stone']}")

    st.markdown(
        f"<h4 style='color:green'>🎨 Lucky Color: {data['color']}</h4>",
        unsafe_allow_html=True
    )
