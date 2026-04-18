from google import genai


def get_gemini_response(api_key, prompt, model="gemini-2.5-flash"):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text