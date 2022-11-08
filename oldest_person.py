def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    name = list(people)
    age = list(people.values())
    maximum = max(age)
    index = age.index(maximum)

    
    return name[index]

print(oldest({"Javohir": 22, "Sharof": 23, "Tolib": 34, "Rustam": 16}))