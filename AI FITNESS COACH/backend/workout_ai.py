import requests

def generate_workout(goal, days, equipment):

    prompt = f"""
    Create a {days}-day workout plan.

    Goal: {goal}
    Equipment: {equipment}

    Include exercises with sets and reps.
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