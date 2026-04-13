import requests

def generate_diet(goal, weight):

    prompt = f"""
    Create a healthy diet plan.

    Goal: {goal}
    Weight: {weight} kg

    Include breakfast, lunch and dinner.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]