"""Student Scores Report
You’re building a simple student report generator that combines names and scores.
Tasks:
    1. Define a function generate_score_report that takes two lists — one with student names and one with their scores.
    2. Use the zip() function to pair each student with their score.
    3. Return a list of strings in the format "Name scored X marks"
"""

# This function will be tested automatically. 
# Do not change the function name or parameters.
def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
    # Write your code below this line
    combine = list(zip(names, scores))
    result = []
    for name, score in combine:
        result.append(f"{name.capitalize()} scored {str(score)} marks")
    
    return result