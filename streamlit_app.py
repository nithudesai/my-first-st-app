import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over [docs.streamlit.io](https://docs.streamlit.io/)."
)
# create form
st.header('Snowflake Role Request Form')
with st.form("form1", clear_on_submit = True):
    snowflakeAccount = st.selectbox(
        "Snowflake Account",
        ("US", "EU"),
        index=0,
        placeholder="Select US or EU",
    )

    environments = st.multiselect(
        "Environment(s)",
        ["DEV", "TST", "PRD"],
    )
    
    requestType = st.selectbox(
        "Type of Request",
        ("Grant Role", "Revoke Role"),
        index=None,
        placeholder="Select Grant or Revoke",
    )

    # TODO - need to fix conditional logic using st.empty https://discuss.streamlit.io/t/can-i-add-to-a-selectbox-an-other-option-where-the-user-can-add-his-own-answer/28525/5
    addFunctionalRoleToProjectRole = st.radio(
        "Add functional role(s) to project role(s)?",
        ["Yes", "No"],        
        index=None,
    )

    addFunctionalRoleToServiceAccountRole = st.radio(
        "Add functional role(s) to service account role(s)?",
        ["Yes", "No"],
        index=None,
    )
    removeFunctionalRoleFromProjectRole = st.radio(
        "Remove functional role(s) from project role(s)?",
        ["Yes", "No"],
        index=None,
    )

    removeFunctionalRoleFromServiceAccountRole = st.radio(
        "Remove functional role(s) from service account role(s)?",
        ["Yes", "No"],
        index=None,
    )

    reasonForRequest = st.text_area(
        "Reason for Request",
        "Please enter a brief description here",
    )

    # TODO - add validation to enforce mandatory fields
    submit = st.form_submit_button("Submit")

    # print form responses
    if submit:
        st.header('Form Responses')
        st.write("Snowflake Account: ", snowflakeAccount)
        st.write("Environment(s): ", environments)
        st.write("Type of Request: ", requestType)
        # TODO add role options 
    
        st.write("Reason for Request: ", reasonForRequest)
