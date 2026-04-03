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
    'A':1,'B':2,'C':3,'D':4,'E':5,'F':8,'G':3,'H':5,'I':1,
    'J':1,'K':2,'L':3,'M':4,'N':5,'O':7,'P':8,'Q':1,'R':2,
    'S':3,'T':4,'U':6,'V':6,'W':6,'X':5,'Y':1,'Z':7
}

# -----------------------------
# Name Number
# -----------------------------
def calculate_name_number(name):
    name = name.upper()
    total = sum(chaldean_map.get(c, 0) for c in name if c.isalpha())
    return reduce_to_single_digit(total)

# -----------------------------
# Destiny Number
# -----------------------------
def calculate_destiny_number(dob):
    total = dob.day + dob.month + dob.year
    return reduce_to_single_digit(total)

# -----------------------------
# Birth Number
# -----------------------------
def calculate_birth_number(day):
    return reduce_to_single_digit(day)

# -----------------------------
# Career Recommendation
# -----------------------------
career_map = {
    1: "Leadership, Entrepreneurship, Management",
    2: "Diplomat, HR, Counsellor",
    3: "Creative, Media, Writing",
    4: "Engineering, Technology, Analyst",
    5: "Sales, Marketing, Travel",
    6: "Teaching, Healthcare",
    7: "Research, Data Science",
    8: "Business, Finance, Management",
    9: "Humanitarian, NGO"
}

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

def evaluate_name(destiny, birth, name_number):
    if destiny == birth and name_number in rules.get(destiny, []):
        return "Excellent"
    elif name_number in rules.get(destiny, []):
        return "Very-Good"
    elif name_number in rules.get(birth, []):
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
# Streamlit Config
# -----------------------------
st.set_page_config(page_title="Numerology AI", layout="centered")
st.title("🔮 Numerology AI Chatbot")

# -----------------------------
# Initialize session state
# -----------------------------
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'dob' not in st.session_state:
    st.session_state.dob = None

# -----------------------------
# Clear Form Function
# -----------------------------
def clear_form():
    # st.session_state.submitted = False
    # st.session_state.name = ""
    # st.session_state.dob = None
    st.experimental_rerun()  # Immediately reload home page

# -----------------------------
# Form
# -----------------------------
with st.form("numerology_form"):

    name_input = st.text_input("Full Name", value=st.session_state.name)
    dob_input = st.date_input(
        "Date of Birth",
        min_value=date(1,1,1),
        max_value=date.today(),
        value=st.session_state.dob
    )

    submit_btn = st.form_submit_button("Calculate")

# -----------------------------
# Form Submit Handling
# -----------------------------
if submit_btn:

    if not name_input.strip() or not dob_input:
        st.error("Please enter both Name and Date of Birth!")
    else:
        st.session_state.submitted = True
        st.session_state.name = name_input.strip()
        st.session_state.dob = dob_input

# -----------------------------
# Display Results
# -----------------------------
if st.session_state.submitted:

    birth_number = calculate_birth_number(st.session_state.dob.day)
    destiny_number = calculate_destiny_number(st.session_state.dob)
    name_number = calculate_name_number(st.session_state.name)

    st.markdown("---")
    st.subheader("🔢 Numerology Numbers")
    st.write(f"**Birth Number:** {birth_number}")
    st.write(f"**Destiny / Path Number:** {destiny_number}")
    st.write(f"**Name Number:** {name_number}")

    st.info(f"💼 Career Recommendation: {career_map.get(destiny_number, 'Unique path awaits you!')}")

    evaluation = evaluate_name(destiny_number, birth_number, name_number)
    color = color_map[evaluation]

    st.markdown("---")
    st.markdown(f"<h2 style='color:{color}'>Name Evaluation : {evaluation}</h2>", unsafe_allow_html=True)

    if evaluation == "Not Good":
        st.error("Your name is not aligned. Consider consulting professional astrologer for name change. 📞 +91 9611-961-111")

    data = path_data.get(destiny_number)
    st.markdown("---")
    st.subheader("🌟 Path Number Guidance")
    st.markdown(f"<h4 style='color:yellow'>🍀 Lucky Dates: {data['lucky']}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:blue'>👍 Favourable Dates: {data['fav']}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:red'>💎 Lucky Stone: {data['stone']}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:green'>🎨 Lucky Color: {data['color']}</h4>", unsafe_allow_html=True)

    # Show Clear / Refresh button only after results
    st.button("🔄 Clear / Refresh", on_click=clear_form)
