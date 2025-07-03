import sys
import os
import streamlit as st

# ✅ Add src to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# ✅ Now import the crew class
from my_first_agent.crew import MyFirstAgent  # or use MultiphaseAutomationCrew if you're using that

# Streamlit UI
st.set_page_config(page_title="CrewAI Assistant", layout="centered")
st.title("🚀 CrewAI Planner & Executor")

st.markdown("Enter a goal below and let your agents plan and execute it!")

objective = st.text_input("🧠 Objective", value="Create a simple marketing plan for a new AI writing tool")

if st.button("Run Crew"):
    st.info("Starting Crew Execution...")
    with st.spinner("Working with agents..."):
        try:
            crew = MyFirstAgent()  # ✅ or MultiphaseAutomationCrew()
            result = crew.crew().kickoff(inputs={"objective": objective})
            st.success("✅ Crew finished successfully!")
            st.markdown("### 📝 Final Result")
            st.markdown(result)
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
