from utils.gemini_client import get_gemini_response
from utils.load_careers import load_careers_data


def skill_gap_agent(api_key, user_input, career_result):
    careers_data = load_careers_data()

    prompt = f"""
You are a skill gap analysis expert.

User background:
{user_input}

Recommended careers:
{career_result}

Available career dataset:
{careers_data}

Your task:
- Identify missing skills for the recommended careers
- Use the dataset as the main reference for required skills
- Prioritize the most important skills first
- Focus on technical and job-relevant skills
- Keep the answer simple and practical

Output format:
- Skill 1
- Skill 2
- Skill 3
- Skill 4

Keep it clear and concise.
"""

    return get_gemini_response(api_key, prompt)