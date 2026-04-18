\# 🎓 Fau-CareerPathFinder-AI



AI-powered career guidance system designed to help students and professionals choose the right career path based on their skills, interests, and goals.



\---



\## 🚀 Features



\- 🎯 Career Recommendation Agent  

\- 📊 Skill Gap Analysis  

\- 🛣️ 6-Month Learning Roadmap  

\- 🤖 AI Impact Analysis (future-proof careers)  

\- 📂 Dataset-driven insights using JSON  

\- 🧠 Multi-agent architecture using LLM (Gemini)  

\- 🌐 Interactive UI with Streamlit  



\---



\## 🏗️ Architecture



This project follows a \*\*multi-agent system design\*\*:



1\. \*\*Career Agent\*\* → Suggests suitable roles  

2\. \*\*Skill Gap Agent\*\* → Identifies missing skills  

3\. \*\*Roadmap Agent\*\* → Creates learning plan  

4\. \*\*AI Impact Agent\*\* → Explains future trends  



All agents are powered by \*\*Google Gemini API\*\* and enhanced using a local dataset.



\---



\## 📁 Project Structure



```text

Fau-CareerPathFinder-AI/

│

├── app.py

├── agents/

│   ├── career\_agent.py

│   ├── skill\_gap\_agent.py

│   ├── roadmap\_agent.py

│   └── ai\_impact\_agent.py

│

├── utils/

│   ├── gemini\_client.py

│   └── load\_careers.py

│

├── data/

│   └── careers.json

│

├── requirements.txt

└── README.md

