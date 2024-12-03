def validate_username(username: str) -> bool:
    """Checks if usernamn is at least 3 characters long and contain both a number and a letter"""
    if len(username) < 3:
        return False

    contains_num = False
    contains_letter = False

    for char in username:
        if char.isdigit():
            contains_num = True
        if char.isalpha():
            contains_letter = True
    
    conditions = [contains_num, contains_letter]
    #Returns true if all items are True otherwise returns False
    return all(conditions)
    
def validate_password(password: str) -> bool:
    """Checks if password is at least 8 characters long and contain both a number and a lower- and uppercase letter"""   
    if len(password) < 8:
        return False

    contains_num = False
    contains_letter = False
    isUpper = False
    isLower = False

    for char in password:
        if char.isdigit():
            contains_num = True
        if char.isalpha():
            contains_letter = True
        if char.isupper():
            isUpper = True
        if char.islower():
            isLower = True
    
    conditions = [contains_num, contains_letter, isUpper, isLower]
    #Returns true if all items are True otherwise returns False
    return all(conditions)