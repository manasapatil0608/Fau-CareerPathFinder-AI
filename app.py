import streamlit as st
from agents.career_agent import career_agent
from agents.skill_gap_agent import skill_gap_agent
from agents.roadmap_agent import roadmap_agent
from agents.ai_impact_agent import ai_impact_agent
from utils.load_careers import load_careers_data

st.set_page_config(page_title="Fau-CareerPathFinder-AI", page_icon="🎓")

st.title("🎓 Fau-CareerPathFinder-AI")
st.write("AI-powered career guidance for students and professionals")

api_key = st.text_input("Enter your Gemini API Key", type="password")

user_input = st.text_area(
    "Tell me about your skills, education, interests, and how much time you can study daily:"
)

careers_data = load_careers_data()

with st.expander("View available careers in dataset"):
    for career in careers_data["careers"]:
        st.markdown(f"**{career['role']}**")
        st.write(f"Skills: {', '.join(career['skills'])}")
        st.write(f"Tools: {', '.join(career['tools'])}")
        st.write(f"Certifications: {', '.join(career['certifications'])}")
        st.write(f"Salary Range: {career['salary_range']}")
        st.write(f"Outlook: {career['outlook']}")
        st.write("---")

if st.button("Get Career Guidance"):
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not user_input.strip():
        st.error("Please enter your background details.")
    else:
        try:
            with st.spinner("Generating your career plan..."):
                career_result = career_agent(api_key, user_input)
                skill_gap_result = skill_gap_agent(api_key, user_input, career_result)
                roadmap_result = roadmap_agent(api_key, user_input, career_result, skill_gap_result)
                ai_impact_result = ai_impact_agent(api_key, career_result)

            tab1, tab2, tab3, tab4 = st.tabs([
                "🎯 Career",
                "📊 Skill Gap",
                "🛣️ Roadmap",
                "🤖 AI Impact"
            ])

            with tab1:
                st.subheader("Career Recommendations")
                st.write(career_result)

            with tab2:
                st.subheader("Skill Gap Analysis")
                st.write(skill_gap_result)

            with tab3:
                st.subheader("Learning Roadmap")
                st.write(roadmap_result)

            with tab4:
                st.subheader("AI Impact")
                st.write(ai_impact_result)

        except Exception as e:
            st.error(f"Error: {e}")