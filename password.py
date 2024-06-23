import streamlit as st
import requests,sqlite3,hashlib ,string,pyperclip
API_KEY = 'ZH+fZzgrfbOclJuktL0DHg==J5T0OcE93umMFzj7'
def pass_strength(password):
    uppercase_criteria=any(c.isupper() for c in password)
    lowercase_criteria=any(c.islower() for c in password)
    digit_criteria=any(c.isdigit() for c in password)
    special_char_criteria=any(c in string.punctuation for c in password)
    total_criteria_met=(uppercase_criteria+lowercase_criteria+digit_criteria+special_char_criteria)
    if total_criteria_met==4:
        return "Strong"
    elif total_criteria_met>=2:
        return "Medium"
    else:
        return "Weak"
def clipboard_copy(password):
    pyperclip.copy(password)
    return "Password copied to clipboard!"
def fetch_password(length):
    api_url = f"https://api.api-ninjas.com/v1/passwordgenerator?length={length}"
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    data = response.json()
    return data['random_password']

def init_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  password TEXT NOT NULL,
                  length INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

def insert_password(password, length):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    h=hashlib.new("md5")
    h.update(password.encode())
    password= h.hexdigest()
    c.execute('INSERT INTO passwords (password, length) VALUES (?, ?)', (password, length))
    conn.commit()
    conn.close()

def main():
    st.write("""
        <style>
        body {
            background-color: #000000!important;
        }
       .stButton > button {
            background-color: #4dc6b8;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
        }
       .stButton > button:hover {
            background-color: #3a9d94;
            color: white;
        }
       .stButton > button:active {
            background-color: #4dc6b8;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Password Generator")

    # Initialize the database
    init_db()

    length = st.number_input("Enter the length of the password", min_value=12, max_value=35)

    if 'generated_password' not in st.session_state:
        st.session_state['generated_password'] = ""

    if st.button("Generate"):
        if length < 12:
            st.error("Length should be greater than 10")
        elif length > 35:
            st.error("Length should be less than 35")
        else:
            st.session_state['generated_password'] = fetch_password(length)
    
    if st.session_state['generated_password']:
        st.markdown(f'<p style="color:white;font-weight:bold;font-size:20px;">Generated Password: <span style="color:#4dc6b8; font-weight:bold;">{st.session_state["generated_password"]}</span></p>', unsafe_allow_html=True)
        password_strength=pass_strength(st.session_state['generated_password'])
        st.markdown(f'<p style="color:white;font-weight:bold;font-size:20px;">Password Strength: <span style="color:#4dc6b8; font-weight:bold;">{password_strength}</span></p>', unsafe_allow_html=True)
        if st.button("Confirm"):
            insert_password(st.session_state['generated_password'], length)
            st.success("Password saved successfully!")
        if st.button("Copy to Clipboard"):
            st.success(clipboard_copy(st.session_state['generated_password']))
if __name__ == "__main__":
    main()
