def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    letter = 0
    digit = 0
    for i in txt:
        if txt[i].isalpha():
            letter += 1

        elif txt[i].isdigit():
            digit += 1

    return {"LETTERS": letter, "DIGITS": digit}