import os
from google import genai


def ask_gemini(question: str):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ GEMINI_API_KEY not found")
        return None

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question
        )

        answer = getattr(response, "text", None)

        if answer:
            print("✅ Gemini response received")
            return answer.strip()

        print("⚠️ Gemini returned an empty response")
        return None

    except Exception as e:
        print("❌ Gemini API Error:")
        print(type(e).__name__, ":", e)
        return None