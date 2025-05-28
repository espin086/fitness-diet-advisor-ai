"""ADK Tools for the Fitness Diet Advisor."""

from typing import Dict, Any

def get_nutritional_info(food_item: str) -> Dict[str, Any]:
    """Fetches nutritional information for a given food item.

    Args:
        food_item: The name of the food item (e.g., "apple", "banana").

    Returns:
        A dictionary containing nutritional data for the food item.
        Example: {'food': 'apple', 'calories': 95, 'protein': '0.5g'}
    """
    # Mock data for now (P1.T3)
    mock_data = {
        "apple": {'food': 'apple', 'calories': 95, 'protein': '0.5g', 'carbs': '25g', 'fat': '0.3g'},
        "banana": {'food': 'banana', 'calories': 105, 'protein': '1.3g', 'carbs': '27g', 'fat': '0.4g'},
    }
    return mock_data.get(food_item.lower(), {"error": f"Nutritional info not found for {food_item}"})

def get_exercise_data(exercise_name: str) -> Dict[str, Any]:
    """Fetches details for a given exercise.

    Args:
        exercise_name: The name of the exercise (e.g., "push-ups", "jumping jacks").

    Returns:
        A dictionary containing details for the exercise.
        Example: {'exercise': 'push-ups', 'category': 'strength', 'instructions': '...'}
    """
    # Mock data for now (P1.T4)
    mock_data = {
        "push-ups": {'exercise': 'push-ups', 'category': 'strength', 'calories_burned_30min_avg_person': 300, 'instructions': 'Place hands shoulder-width apart, lower body until chest nearly touches floor, push back up.'},
        "jumping jacks": {'exercise': 'jumping jacks', 'category': 'cardio', 'calories_burned_30min_avg_person': 250, 'instructions': 'Stand with feet together, jump to a position with legs spread wide and hands touching overhead, return to start.'},
    }
    return mock_data.get(exercise_name.lower(), {"error": f"Exercise data not found for {exercise_name}"}) 