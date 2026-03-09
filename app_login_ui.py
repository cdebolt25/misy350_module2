import streamlit as st
import json
import pathlib
import datetime
import uuid
import time

### ---------- 1.) PROJECT SET UP ---------- ###
## Step 1

st.set_page_config(
    page_title = "Course Manager",
    layout = "centered"
)

st.title("Course Manager")

## Step 2

json_file = pathlib.Path("users.json")

if json_file.exists():
    with open(json_file, "r") as f:
        users = json.load(f)
else:
    users = [
        {
            "id": "1",
            "email": "admin@school.edu",
            "full_name": "System Admin",
            "password": "123ssag@43AE",
            "role": "Admin",
            "registered_at": datetime.datetime.now().isoformat()
        }
    ]
    with open(json_file, "w") as f:
        json.dump(users, f, indent=4)


### ---------- 2.) NAVIGATION AND PAGE STRUCTURE ---------- ###
## Sidebar Navigation 
with st.sidebar:
    st.title("Course Manager")
    st.divider()
    page = st.radio(
        "Navigate to:",
        options=["Login", "Register"],
        index=0
    )
    st.divider()
    with st.expander("Current Users (Debug)"):
        st.dataframe(users, use_container_width=True)

## Main Page
st.title("Welcome to Course Manager")

if page == "Register":
    st.subheader("Create an Account")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            reg_full_name = st.text_input("Full Name", placeholder="Chance DeBolt")
        with col2:
            reg_email = st.text_input("Email", placeholder="cdebolt@udel.edu")

        reg_password = st.text_input("Password", type="password", placeholder="Enter a password")
        reg_confirm  = st.text_input("Confirm Password", type="password", placeholder="Repeat your password")

        if st.button("Register", use_container_width=True):
            st.info("Registration logic coming soon...")

elif page == "Login":
    st.subheader("Sign In")
    with st.container():
        login_email    = st.text_input("Email", placeholder="cdebolt@udel.edu")
        login_password = st.text_input("Password", type="password", placeholder="Your password")

        if st.button("Login", use_container_width=True):
            st.info("Login coming soon...")

### ---------- 3.) THE REGISTRATION FORM ---------- ###
