from utils.gemini_client import get_gemini_response
from utils.load_careers import load_careers_data


def career_agent(api_key, user_input):
    careers_data = load_careers_data()

    prompt = f"""
You are a career recommendation expert.

User background:
{user_input}

Available career dataset:
{careers_data}

Your task:
- Suggest 2 to 3 suitable career paths from the dataset
- Explain why each career fits the user
- Keep it realistic and aligned with current market demand
- Use the dataset roles as the primary options

Output format:
Career 1: reason
Career 2: reason
Career 3: reason (optional)

Keep it simple, clear, and practical.
"""

    return get_gemini_response(api_key, prompt)