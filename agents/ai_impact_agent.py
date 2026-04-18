from utils.gemini_client import get_gemini_response
from utils.load_careers import load_careers_data


def ai_impact_agent(api_key, career_result):
    careers_data = load_careers_data()

    prompt = f"""
You are an AI career impact expert.

Recommended careers:
{career_result}

Available career dataset:
{careers_data}

Your task:
- Explain how AI may impact the recommended careers
- Use the dataset as the main reference
- Mention which tasks may be automated
- Mention which human skills will remain valuable
- Mention how the user can stay relevant in the next 5 to 10 years
- Keep the answer realistic, simple, and not alarming

Output format:
AI Impact Summary:
- point 1
- point 2

How to Stay Relevant:
- point 1
- point 2
- point 3
"""

    return get_gemini_response(api_key, prompt)