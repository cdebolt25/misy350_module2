import streamlit as st
import time
import json
from pathlib import Path 

st.set_page_config(
    page_title="Course Manager",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Course Management App")

st.divider()

next_assignment_id_number = 3

# Load Assignments
assignments = [
    {
        "id" : "HW1",
        "title" : "Introduction to Database",
        "description" : "basics of database design",
        "point" : 100,
        "type" : "homework"
    },
    {
        "id" : "HW2",
        "title" : "Normalizaiton",
        "description" : "Normalize the table designs",
        "points" : 100,
        "type" : "lab"
    }
]

json_path = Path("assignments.json")

if json_path.exists:
    with json_path.open("r", encoding="utf-8") as f:
        assignments = json.load(f)

tab1, tab2, tab3 = st.tabs(["View Assignments", "Add New Assignment", "Updated an Assignment"])

with tab1:
    #st.info("This tab is under development!")
    option = st.radio("View/Search", ["View", "Search"], horizontal=True)

    if option == "View":
        st.dataframe(assignments)

    else:
        titles = []
        for assignment in assignments:
            titles.append(assignment["title"])

        if not titles:
            st.warning("No assignment is found")
        else:
            selected_title = st.selectbox("Assignment Titles", titles)
            
            for assignment in assignments:
                if assignment["title"] == selected_title:
                    with st.expander( "Assignment Details", expanded=True):
                        st.markdown(f"### Title: {assignment["title"]}")
                        st.markdown(f"Description: {assignment["description"]}")
                        st.markdown(f"Type: **{assignment["type"]}**")
                    break
            selected_title = st.selectbox("Assignment Title",
                                          options=assignments,
                                          format_func=lambda x: f"{x['title']} {x['type']}",
                                          key = "new assignment")

with tab2:
    # Add New Assignment
    st.markdown



tab1, tab2, tab3 = st.tabs(["View Assignments", "Add New Assignment", "Updated an Assignment"])

#with tab1:

#with tab2:

with tab3:
    st.markdown("# Update an Assignment")

    titles = []
    for assignment in assignments:
        titles.append(assignment["title"])

    selected_item = st.selectbox("Select an item", titles, key="search_titles")

    selected_assignment = {}
    for assignment in assignments:
        if assignment["title"] == selected_item:
            selected_assignment = assignment
            break

edit_title = st.text_imput("Title", key = "edit_title", value = selected_assignment["title"])
edit_description = st.text_area("Description", value = selected_assignment['description'], key = "edit_description")


type_list = ["Homework", "Lab"]
selected_assignment_type_index = type_list.index(selected_assignment['type'])

edit_type = st.radio("Type", type_list, index=selected_assignment_type_index,
                     key = f"edit_type_{selected_assignment['id']}")

update_btn = st.button("Update Assignment", key="btn_update", use_container_width=True, type="primary")
if update_btn:
    with st.spinner("Updating the assignment..."):
        time.sleep(5)
        selected_assignment["title"] = edit_title
        selected_assignment["description"] = edit_description

#        with json_path.open("w")
