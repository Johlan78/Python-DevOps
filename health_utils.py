def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) from weight (kg) and height (m).
    Formula: BMI = weight / height^2
    
    Arguments:
    weight -- weight in kilograms
    height -- height in meters
    
    Returns:
    BMI value
    
    Raises:
    ValueError -- if height is less than or equal to zero
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    
    return weight / (height ** 2)


def calculate_bmr(weight, height, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) based on the Mifflin-St Jeor Equation.
    For males:
    BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    For females:
    BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    Arguments:
    weight -- weight in kilograms
    height -- height in centimeters
    age -- age in years
    gender -- gender, 'male' or 'female'
    
    Returns:
    BMR value
    
    Raises:
    ValueError -- if the gender is not recognized
    """
    if gender == "male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "female":
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Gender must be 'male' or 'female'.")