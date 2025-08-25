import json
import os
from openai import OpenAI

# read from env explicitly (works even if imported from elsewhere)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SCHEMAS = {
    "flashcards": (
        "Create exactly 8 flashcards about '{topic}'. "
        "Return a JSON object with key 'flashcards' -> array of objects, each with: "
        "'front' (concise prompt/question) and 'back' (succinct answer, 1-3 sentences). "
        "No extra commentary."
    ),
    "quiz": (
        "Create a multiple-choice quiz (5 questions) about '{topic}'. "
        "Return a JSON object with key 'quiz' -> array of objects, each with: "
        "'question' (string), 'choices' (array of 4 short strings), and 'answer_index' (0-3). "
        "Keep language clear and student-friendly."
    ),
    "study_guide": (
        "Create a succinct study guide for '{topic}'. "
        "Return a JSON object with key 'study_guide' that has: "
        "'sections' (array of objects with 'title' and 'bullets' [3-6 items]) and "
        "'key_terms' (array of objects with 'term' and 'definition' one-line)."
    ),
    "outline": (
        "Create an essay outline for '{topic}'. "
        "Return a JSON object with key 'outline' that has: 'title', 'thesis', and "
        "'sections' (array of objects with 'heading' and 'bullets' [2-4 items])."
    ),
}

def generate_content(topic: str, content_type: str) -> str:
    if content_type not in SCHEMAS:
        raise ValueError("Unsupported content_type. Choose flashcards | quiz | study_guide | outline.")

    sys = (
        "You are an educational content generator. "
        "You MUST return valid JSON only. No preface, no markdown, no code fences."
    )
    user = SCHEMAS[content_type].format(topic=topic)

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": sys},
            {"role": "user", "content": user},
        ],
    )
    return resp.choices[0].message.content

