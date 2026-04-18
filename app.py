import streamlit as st
import datetime
from agents.career_agent import career_agent
from agents.skill_gap_agent import skill_gap_agent
from agents.roadmap_agent import roadmap_agent
from agents.ai_impact_agent import ai_impact_agent
from utils.load_careers import load_careers_data

st.set_page_config(
    page_title="Fau-CareerPathFinder-AI",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------
# SESSION STATE
# ----------------------------
if "selected_feature" not in st.session_state:
    st.session_state.selected_feature = None

# ----------------------------
# HEADER
# ----------------------------
st.title("🎓 Fau-CareerPathFinder-AI")
st.write("AI-powered career guidance, academic planning, and student support platform")

api_key = st.text_input("Enter your Gemini API Key", type="password")

user_input = st.text_area(
    "Tell me about your skills, education, interests, and how much time you can study daily:"
)

careers_data = load_careers_data()

with st.expander("View available careers in dataset"):
    for career in careers_data["careers"]:
        st.markdown(f"*{career['role']}*")
        st.write(f"Skills: {', '.join(career['skills'])}")
        st.write(f"Tools: {', '.join(career['tools'])}")
        st.write(f"Certifications: {', '.join(career['certifications'])}")
        st.write(f"Salary Range: {career['salary_range']}")
        st.write(f"Outlook: {career['outlook']}")
        st.write("---")

# ----------------------------
# CAREER GUIDANCE SECTION
# ----------------------------
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

st.markdown("---")

# ----------------------------
# STUDENT JOURNEY
# ----------------------------
st.header("🚀 How It Works — Student Journey")

journey_col1, journey_col2, journey_col3 = st.columns(3)

with journey_col1:
    st.info("Create account")
    st.info("Upload syllabus PDF")
    st.info("AI extracts deadlines")
    st.info("Dashboard goes live")

with journey_col2:
    st.info("Log appointments")
    st.info("AI spots patterns")
    st.info("Weekly briefing delivered")
    st.info("Student stays on track")

with journey_col3:
    st.info("AI detects risk")
    st.info("Nudge sent proactively")
    st.info("Advisor alerted")
    st.info("Student helped early")

st.markdown("---")

# ----------------------------
# FEATURE BUTTONS
# ----------------------------
st.header("🧩 Feature Layers")
st.write("Click any feature to open its dummy module.")

feature_rows = [
    [
        ("📅 Professor Booking", "professor_booking"),
        ("📘 Syllabus Import", "syllabus_import"),
        ("⏰ Deadline Dashboard", "deadline_dashboard"),
        ("🧠 AI Risk Detection", "risk_detection"),
    ],
    [
        ("💰 Budget Tracker", "budget_tracker"),
        ("📄 Resume Coach", "resume_coach"),
        ("🎓 Scholarship Finder", "scholarship_finder"),
        ("👥 Study Group Match", "study_group_match"),
    ],
    [
        ("🗺️ Campus Navigation", "campus_navigation"),
        ("📚 Flashcards", "flashcards"),
        ("📈 Weekly Briefing", "weekly_briefing"),
        ("📝 Timetable Gap Optimizer", "timetable_optimizer"),
    ]
]

for row in feature_rows:
    cols = st.columns(4)
    for i, (label, key_name) in enumerate(row):
        with cols[i]:
            if st.button(label, use_container_width=True):
                st.session_state.selected_feature = key_name

# ----------------------------
# FEATURE DETAILS
# ----------------------------
selected = st.session_state.selected_feature

if selected:
    st.markdown("---")
    st.subheader("Opened Feature")

# ----------------------------
# 1. PROFESSOR BOOKING
# ----------------------------
if selected == "professor_booking":
    st.markdown("## 📅 Professor Appointment Booking")

    professors = [
        {
            "name": "Dr. Emily Carter",
            "role": "Professor of Data Science",
            "department": "Computer Science and Data Analytics",
            "available_slots": ["10:00 AM", "11:00 AM", "2:00 PM"]
        },
        {
            "name": "Dr. Michael Johnson",
            "role": "Professor of Machine Learning",
            "department": "Artificial Intelligence",
            "available_slots": ["9:00 AM", "1:00 PM", "3:00 PM"]
        },
        {
            "name": "Dr. Sarah Williams",
            "role": "Professor of Business Analytics",
            "department": "Business",
            "available_slots": ["11:30 AM", "2:30 PM", "4:00 PM"]
        },
        {
            "name": "Dr. David Brown",
            "role": "Professor of Artificial Intelligence",
            "department": "Computer Science",
            "available_slots": ["10:30 AM", "12:00 PM", "3:30 PM"]
        }
    ]

    professor_names = [prof["name"] for prof in professors]
    selected_professor_name = st.selectbox("Select Professor", professor_names)

    selected_professor = next(prof for prof in professors if prof["name"] == selected_professor_name)

    st.write(f"*Role:* {selected_professor['role']}")
    st.write(f"*Department:* {selected_professor['department']}")

    student_name = st.text_input("Student Name")
    student_email = st.text_input("Student Email")
    appointment_date = st.date_input("Appointment Date", min_value=datetime.date.today())
    appointment_time = st.selectbox("Available Slots", selected_professor["available_slots"])
    appointment_reason = st.text_area("Reason for Appointment")

    if st.button("Confirm Booking"):
        if student_name and student_email and appointment_reason:
            st.success("Appointment booked successfully.")
            st.write("### Booking Summary")
            st.write(f"*Student:* {student_name}")
            st.write(f"*Email:* {student_email}")
            st.write(f"*Professor:* {selected_professor['name']}")
            st.write(f"*Date:* {appointment_date}")
            st.write(f"*Time:* {appointment_time}")
            st.write(f"*Reason:* {appointment_reason}")
        else:
            st.error("Please fill all fields.")

# ----------------------------
# 2. SYLLABUS IMPORT
# ----------------------------
elif selected == "syllabus_import":
    st.markdown("## 📘 Syllabus Import")
    st.write("Dummy feature: upload a syllabus and extract deadlines, quizzes, and exams.")

    uploaded_file = st.file_uploader("Upload syllabus PDF", type=["pdf"])

    if uploaded_file:
        st.success(f"Uploaded: {uploaded_file.name}")
        st.write("### Extracted Items")
        st.table([
            {"Task": "Assignment 1", "Due Date": "2026-04-25", "Course": "Data Mining"},
            {"Task": "Quiz 1", "Due Date": "2026-04-28", "Course": "Machine Learning"},
            {"Task": "Midterm Exam", "Due Date": "2026-05-05", "Course": "Advanced Analytics"},
        ])
    else:
        st.info("Upload any syllabus PDF to see dummy extracted deadlines.")

# ----------------------------
# 3. DEADLINE DASHBOARD
# ----------------------------
elif selected == "deadline_dashboard":
    st.markdown("## ⏰ Deadline Dashboard")

    deadlines = [
        {"Course": "Data Mining", "Task": "Assignment 1", "Deadline": "2026-04-25", "Priority": "High"},
        {"Course": "Machine Learning", "Task": "Quiz 1", "Deadline": "2026-04-28", "Priority": "Medium"},
        {"Course": "Business Analytics", "Task": "Case Study", "Deadline": "2026-05-01", "Priority": "High"},
        {"Course": "AI Systems", "Task": "Lab Submission", "Deadline": "2026-05-03", "Priority": "Low"},
    ]

    st.dataframe(deadlines, use_container_width=True)

# ----------------------------
# 4. RISK DETECTION
# ----------------------------
elif selected == "risk_detection":
    st.markdown("## 🧠 AI Risk Detection")

    st.warning("Dummy AI alert: You may be at risk of missing 2 upcoming deadlines.")
    st.write("### Why this alert was triggered")
    st.write("- Low study hours logged this week")
    st.write("- Multiple deadlines within 7 days")
    st.write("- No professor/advisor meeting scheduled")
    st.write("### Suggested Action")
    st.success("Schedule an advisor meeting and complete the highest priority task first.")

# ----------------------------
# 5. BUDGET TRACKER
# ----------------------------
elif selected == "budget_tracker":
    st.markdown("## 💰 Budget Tracker")

    monthly_income = st.number_input("Monthly Income", min_value=0, value=1500)
    rent = st.number_input("Rent", min_value=0, value=700)
    food = st.number_input("Food", min_value=0, value=250)
    transport = st.number_input("Transport", min_value=0, value=100)
    other = st.number_input("Other Expenses", min_value=0, value=150)

    total_expenses = rent + food + transport + other
    savings = monthly_income - total_expenses

    st.write(f"*Total Expenses:* ${total_expenses}")
    st.write(f"*Estimated Savings:* ${savings}")

    if savings > 0:
        st.success("You are within budget this month.")
    else:
        st.error("Your expenses exceed your income.")

# ----------------------------
# 6. RESUME COACH
# ----------------------------
elif selected == "resume_coach":
    st.markdown("## 📄 Resume Coach")

    target_role = st.selectbox(
        "Target Role",
        ["Data Analyst Intern", "Machine Learning Intern", "Business Analyst Intern", "Data Engineer Intern"]
    )

    resume_text = st.text_area("Paste Resume Summary")

    if st.button("Analyze Resume Match"):
        if resume_text.strip():
            st.write("### Resume Feedback")
            st.write(f"*Target Role:* {target_role}")
            st.write("- Strong technical base detected")
            st.write("- Add more quantified project outcomes")
            st.write("- Include tools like SQL, Python, Power BI more clearly")
            st.write("- Add role-specific keywords for better matching")
            st.success("Dummy match score: 82%")
        else:
            st.error("Please paste some resume content.")

# ----------------------------
# 7. SCHOLARSHIP FINDER
# ----------------------------
elif selected == "scholarship_finder":
    st.markdown("## 🎓 Scholarship Finder")

    scholarships = [
        {
            "name": "FAU Graduate Success Scholarship",
            "amount": "$2,000",
            "deadline": "2026-05-15",
            "eligibility": "Graduate students with 3.5+ GPA"
        },
        {
            "name": "STEM Excellence Grant",
            "amount": "$3,500",
            "deadline": "2026-06-01",
            "eligibility": "Students in AI, Data Science, or Engineering"
        },
        {
            "name": "International Student Achievement Fund",
            "amount": "$1,500",
            "deadline": "2026-05-25",
            "eligibility": "International students with strong academic standing"
        }
    ]

    for scholarship in scholarships:
        with st.container(border=True):
            st.write(f"### {scholarship['name']}")
            st.write(f"*Amount:* {scholarship['amount']}")
            st.write(f"*Deadline:* {scholarship['deadline']}")
            st.write(f"*Eligibility:* {scholarship['eligibility']}")

# ----------------------------
# 8. STUDY GROUP MATCH
# ----------------------------
elif selected == "study_group_match":
    st.markdown("## 👥 Study Group Match")

    groups = [
        {"Group Name": "ML Night Owls", "Course": "Machine Learning", "Members": "Aarav, Neha, Kevin", "Time": "7:00 PM"},
        {"Group Name": "Data Wizards", "Course": "Data Mining", "Members": "Priya, John, Fatima", "Time": "6:00 PM"},
        {"Group Name": "Analytics Circle", "Course": "Business Analytics", "Members": "Rohan, Lisa, Emma", "Time": "5:30 PM"},
    ]

    st.dataframe(groups, use_container_width=True)

# ----------------------------
# 9. CAMPUS NAVIGATION
# ----------------------------
elif selected == "campus_navigation":
    st.markdown("## 🗺️ Campus Navigation")

    location = st.selectbox(
        "Choose destination",
        ["Engineering East", "Library", "Student Union", "Computer Lab", "Career Center"]
    )

    routes = {
        "Engineering East": "Walk straight from the main entrance, turn right near the parking lot, 4 minutes.",
        "Library": "Go left from the main plaza, cross the lawn, 3 minutes.",
        "Student Union": "Head past the cafeteria and continue for 5 minutes.",
        "Computer Lab": "Inside Engineering Building, 2nd floor, Room 204.",
        "Career Center": "Near the administration block, first floor."
    }

    st.info(routes[location])

# ----------------------------
# 10. FLASHCARDS
# ----------------------------
elif selected == "flashcards":
    st.markdown("## 📚 Flashcards")

    topic = st.selectbox("Choose Topic", ["Python", "Machine Learning", "SQL", "Statistics"])

    flashcards = {
        "Python": [
            ("What is a list?", "A mutable ordered collection in Python."),
            ("What is a dictionary?", "A key-value data structure."),
        ],
        "Machine Learning": [
            ("What is overfitting?", "When a model memorizes training data and performs poorly on new data."),
            ("What is supervised learning?", "Learning from labeled data."),
        ],
        "SQL": [
            ("What does SELECT do?", "Fetches data from a database."),
            ("What is JOIN?", "Combines rows from multiple tables."),
        ],
        "Statistics": [
            ("What is mean?", "Average of values."),
            ("What is standard deviation?", "Measure of spread."),
        ],
    }

    for q, a in flashcards[topic]:
        with st.expander(q):
            st.write(a)

# ----------------------------
# 11. WEEKLY BRIEFING
# ----------------------------
elif selected == "weekly_briefing":
    st.markdown("## 📈 Weekly Briefing")

    st.write("### This Week's Summary")
    st.write("- 3 deadlines coming up")
    st.write("- 1 missed study session")
    st.write("- 2 recommended job applications")
    st.write("- 1 professor appointment suggested")
    st.write("- Scholarship deadline in 12 days")

    st.success("Recommendation: Focus on Data Mining assignment first, then prepare for Machine Learning quiz.")

# ----------------------------
# 12. TIMETABLE OPTIMIZER
# ----------------------------
elif selected == "timetable_optimizer":
    st.markdown("## 📝 Timetable Gap Optimizer")

    schedule = [
        {"Time": "9:00 AM - 10:00 AM", "Activity": "Class: Machine Learning"},
        {"Time": "10:00 AM - 12:00 PM", "Activity": "Free Slot"},
        {"Time": "12:00 PM - 1:00 PM", "Activity": "Class: Data Mining"},
        {"Time": "1:00 PM - 3:00 PM", "Activity": "Free Slot"},
        {"Time": "3:00 PM - 4:00 PM", "Activity": "Class: AI Systems"},
    ]

    st.dataframe(schedule, use_container_width=True)

    st.write("### Suggested Use of Free Slots")
    st.write("- 10:00 AM - 12:00 PM → Assignment work / library session")
    st.write("- 1:00 PM - 3:00 PM → Professor appointment / internship applications")

st.markdown("---")

# ----------------------------
# WELLBEING, CAREER & SOCIAL
# ----------------------------
st.header("🌟 Wellbeing, Career & Social")

wc1, wc2, wc3, wc4 = st.columns(4)

with wc1:
    st.markdown("### Budget Tracker")
    st.caption("CSV → smart spending plan")

with wc2:
    st.markdown("### Resume Coach")
    st.caption("Semantic job matching")

with wc3:
    st.markdown("### Scholarship Finder")
    st.caption("RAG over grant databases")

with wc4:
    st.markdown("### Study Group Match")
    st.caption("Collaborative filtering")

st.markdown("---")

# ----------------------------
# BUILD TIMELINE
# ----------------------------
st.header("🛠️ Build Timeline")

t1, t2 = st.columns(2)
t3, t4 = st.columns(2)

with t1:
    st.success("### Phase 1\nWeeks 1–2\nAccounts, syllabus import, deadline dashboard")

with t2:
    st.info("### Phase 2\nWeeks 3–5\nAI predictions, briefings, tutor, misconceptions")

with t3:
    st.warning("### Phase 3\nWeeks 6–8\nProductivity, wellbeing, budget, flashcards")

with t4:
    st.error("### Phase 4\nWeeks 9–12\nCareer, social, scholarships, campus navigation")
