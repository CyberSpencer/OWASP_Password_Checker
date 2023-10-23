# OWASP_Password_Checker.py
# Author: CyberSpencer
# Date: 10/23/2023
# Description: A Python script to check the strength of a user-provided password 
#              based on OWASP guidelines. The script evaluates the password based 
#              on multiple criteria such as length, use of uppercase and lowercase 
#              letters, digits, and special characters. It then calculates a strength 
#              score and provides a description of the password strength.

import string # Imported string module for predefined character sets used in password checks.

def describe_password_strength(password_strength_score):
    if password_strength_score == 100:
        return "Very Strong Password"
    elif 80 <= password_strength_score < 100:
        return "Strong Password"
    elif 60 <= password_strength_score < 80:
        return "Moderate Password"
    elif 40 <= password_strength_score < 60:
        return "Weak Password"
    else:
        return "Very Weak Password"

def calculate_password_strength_score(password):
    config = {
        "min_length": 12,
        "max_length": 128,
        "lowercase": set(string.ascii_lowercase),
        "uppercase": set(string.ascii_uppercase),
        "digits": set(string.digits),
        "special_characters": set(string.punctuation),
        "no_spaces": set(' ')
    }
    length = len(password)
    criteria_met = 0
    criteria = {
        "length": False,
        "lowercase": False,
        "uppercase": False,
        "digits": False,
        "special_characters": False,
        "no_spaces": True
    }
    password_chars = set(password)
    if config['min_length'] <= length <= config['max_length']:
        criteria["length"] = True
        criteria_met += 1
    for key in ['lowercase', 'uppercase', 'digits', 'special_characters']:
        if password_chars & config[key]:
            criteria[key] = True
            criteria_met += 1
    if password_chars & config['no_spaces']:
        criteria['no_spaces'] = False
    else:
        criteria_met += 1
    total_criteria = len(criteria)
    password_strength_score = (criteria_met / total_criteria) * 100
    result = {
        'criteria_met': criteria_met,
        'criteria': criteria,
        'password_strength_score': password_strength_score
    }
    return result

def calculate_and_describe_password_strength(password):
    result = calculate_password_strength_score(password)
    result['strength_description'] = describe_password_strength(result['password_strength_score'])
    return result

def format_output(result):
    formatted_output = f"""
    Password Strength Report:
    --------------------------
    Strength Description: {result['strength_description']}
    Password Strength Score: {result['password_strength_score']}%

    Criteria Met:
    - Length: {'Yes' if result['criteria']['length'] else 'No'}
    - Lowercase: {'Yes' if result['criteria']['lowercase'] else 'No'}
    - Uppercase: {'Yes' if result['criteria']['uppercase'] else 'No'}
    - Digits: {'Yes' if result['criteria']['digits'] else 'No'}
    - Special Characters: {'Yes' if result['criteria']['special_characters'] else 'No'}
    - No Spaces: {'Yes' if result['criteria']['no_spaces'] else 'No'}
    """
    return formatted_output

def get_user_password():
    return input("Please enter the password you'd like to test: ")

if __name__ == '__main__':
    user_password = get_user_password()
    result_with_description = calculate_and_describe_password_strength(user_password)
    formatted_output = format_output(result_with_description)
    print(formatted_output)
