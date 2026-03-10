def calculate_risk(age: int, bmi: float, glucose: float) -> float:
    risk = 0.3 * bmi + 0.5 * glucose + 0.2 * age
    return min(risk / 100, 1.0)