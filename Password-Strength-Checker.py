"""
    Evaluates the strength of a password based on the following criteria:
    - Length: at least 12 characters
    - Uppercase letters: at least 1
    - Lowercase letters: at least 1
    - Digits: at least 1
    - Special characters: at least 1

    Returns a dictionary with the following keys:
    - 'strength': a score from 0 to 5, where:
        - 0: Very weak (does not meet any of the criteria)
        - 1: Weak (meets only 1 of the criteria)
        - 2: Fair (meets 2 of the criteria)
        - 3: Good (meets 3 of the criteria)
        - 4: Strong (meets 4 of the criteria)
        - 5: Very strong (meets all 5 criteria)
    - 'feedback': a list of suggestions for improving the password
    """

import re

def password_strength(password):
    feedback = []
    score = 0

    # Check length
    if len(password) < 12:
        feedback.append("Password should be at least 12 characters long")
    else:
        score += 1

    # Check for uppercase letters
    if not re.search(r"[A-Z]", password):
        feedback.append("Password should contain at least one uppercase letter")
    else:
        score += 1

    # Check for lowercase letters
    if not re.search(r"[a-z]", password):
        feedback.append("Password should contain at least one lowercase letter")
    else:
        score += 1

    # Check for digits
    if not re.search(r"\d", password):
        feedback.append("Password should contain at least one digit")
    else:
        score += 1

    # Check for special characters
    if not re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        feedback.append("Password should contain at least one special character")
    else:
        score += 1

    strength_levels = {
        0: "Very weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very strong"
    }

    return {
        'strength': strength_levels[score],
        'feedback': feedback
    }

def main():
    password = input("Enter a password: ")
    result = password_strength(password)

    print(f"Password strength: {result['strength']}")
    if result['feedback']:
        print("Suggestions for improvement:")
        for suggestion in result['feedback']:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
