from utils.gemini_client import get_gemini_response
from utils.load_careers import load_careers_data


def roadmap_agent(api_key, user_input, career_result, skill_gap_result):
    careers_data = load_careers_data()

    prompt = f"""
You are a career roadmap planner.

User background:
{user_input}

Recommended careers:
{career_result}

Skill gaps:
{skill_gap_result}

Available career dataset:
{careers_data}

Your task:
- Create a 6-month learning roadmap
- Use the dataset as the main reference
- Break the plan into Month 1-2, Month 3-4, and Month 5-6
- Focus on the most important missing skills first
- Keep the roadmap realistic and beginner-friendly
- Include what to learn, what to practice, and what projects to build

Output format:

Month 1-2:
- tasks

Month 3-4:
- tasks

Month 5-6:
- tasks

Keep it clear, practical, and structured.
"""

    return get_gemini_response(api_key, prompt)