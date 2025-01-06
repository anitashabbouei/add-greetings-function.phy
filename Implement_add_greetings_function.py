# add_greetings.py

def add_greetings(nameList):
    """
    This function takes a list of names and returns a list of greetings in the format 'Hello, <name>'.
    
    Parameters:
    nameList (list): A list of strings (names)
    
    Returns:
    list: A list of greetings
    """
    greetings = []
    for item in nameList: 
        greetings.append('Hello, ' + item)
    return greetings

# Uncomment the line below to test the function
if __name__ == "__main__":
    print(add_greetings(["Owen", "Max", "Sophie"]))  # Output: ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']
