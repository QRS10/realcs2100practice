"""
Example OOP for coffee
"""

class CoffeeBag:
    """
    Represents a bag of coffee
    """

    def __init__(self, location: str, name: str, grams: int, tasting_notes: list[str]) -> None:
        """
        Initialize the supplied coffee bag instance (object)

        Parameters
            growing_location: string
                location the beans were grown
        """

        self.location: str = location
        self.name: str = name
        self.grams: int = grams
        self.tasting_notes: list[str] = tasting_notes

    def __str__(self) -> str:
        """Provides readable version of the bag"""

        return f"{self.grams}g of {self.name}, from {self.location}"
    
    def brew(self, grams_to_use: int) -> None:
        """
        Brews a bag, taking supplied beans away

        Parameters
            grams_to_use: int
                grams needed for the cup of coffee
        """

        self.grams -= grams_to_use

    def grind_beans(self) -> None:
        """
        What happens when you grind the beans?
        """

        print(f"I smell {self.tasting_notes}")

def main() -> None:
    """
    Coffee App
    """

    current_bag: CoffeeBag = CoffeeBag("Ethiopia", "bochesa natural", 283, ["tangerine", "vanilla"])
    favorite_bag: CoffeeBag = CoffeeBag("Colombia", "lychee coffee", 250, ["chocolate", "lemon"])

    print(f"Current: {current_bag}, {current_bag.grams} grams of {current_bag.name} @ {current_bag.location}")
    print(f"Favorite: {favorite_bag}, {favorite_bag.grams} grams of {favorite_bag.name} @ {favorite_bag.location}")
    print(f"Current: {current_bag}")
    print(f"Favorite: {favorite_bag}")

    # current_name: str = str(current_bag)
    # print(current_name)

    print("Brewed 15 grams")
    current_bag.brew(15)
    # CoffeeBag.brew(current_bag, 15)

    current_bag.grind_beans()
    favorite_bag.grind_beans()

if __name__ == "__main__":
    main()