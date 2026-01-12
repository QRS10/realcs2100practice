"""
TODO: A very useful temperature-conversion app.
"""

def is_it_cold_f(temp_f: float) -> bool:
    """Determines if the inputted temp is below a certain threshold
    Parameters
    ==========
    temp_f: float 
        supplied temperature in F
    
    Returns
    =======
    bool

    """
    if temp_f < 68:
        return True
    else:
        return False


def greet_human() -> None:
    """Get a name from the keyboard and say hello!"""
    name: str = input('what is your name?')
    print(f"hello {name}")

def main() -> None:
    pass

if __name__ == "__main__":
    main()

