from fastapi import FastAPI
from pydantic import BaseModel

from backend.bmi import calculate_bmi
from backend.workout_ai import generate_workout
from backend.diet_ai import generate_diet

app = FastAPI()

class FitnessInput(BaseModel):
    age: int
    height: float
    weight: float
    goal: str
    days: int
    equipment: str


@app.post("/generate-plan")
def generate_plan(data: FitnessInput):

    bmi_result = calculate_bmi(data.weight, data.height)

    workout = generate_workout(data.goal, data.days, data.equipment)

    diet = generate_diet(data.goal, data.weight)

    return {
        "bmi": bmi_result,
        "workout_plan": workout,
        "diet_plan": diet
    }