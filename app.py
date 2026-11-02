import streamlit as st

st.set_page_config(page_title="AI Investigation Room", layout="wide")
st.title("🚀 AI Investigation Room")
st.subheader("Case #101: The Missing University Database")

col1, col2 = st.columns([1,2])

with col1:
    st.header("📋 Evidence Board")
    e1 = st.checkbox("CCTV - Person entered Lab at 2:03 AM")
    e2 = st.checkbox("USB Drive found - Deleted DBMS files")
    e3 = st.checkbox("System Log - IP 192.168.1.5 at 2:15 AM")
    e4 = st.checkbox("Coffee cup fingerprints")
    
    st.header("👥 Suspects")
    suspect = st.radio("Select suspect:", ["Rahul (Lab Staff)", "Priya (Student)", "Admin"])

with col2:
    st.header("🤖 AI Co-Detective")
    st.info("Hi Detective! I'm your AI partner. Select evidence on left.")
    
    question = st.text_input("Ask AI: Who had lab access?")
    
    if question:
        if e1 and e2 and e3:
            st.success("AI Analysis: All evidence same time 2:00-2:15 AM. Only Rahul had night access!")
        elif e3:
            st.warning("AI Analysis: IP 192.168.1.5 is Lab PC. Check who logged in.")
        else:
            st.write("AI: Collect more evidence daa!")
    
    st.divider()
    if st.button("🔍 SOLVE CASE"):
        st.balloons()
        st.error("CASE SOLVED: Culprit is Rahul")
        st.write("Proof: Night shift + CCTV + IP + USB fingerprint")

st.sidebar.success("Ready for submission! Deadline Today 11:59 PM")
