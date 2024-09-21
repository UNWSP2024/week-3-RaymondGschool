# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

def is_valid_input(prompt: str, valid_inputs: list[str]):
    # makes all valid_inputs lower case for flexability
    valid_inputs = [item.lower() for item in valid_inputs]

    while True:
        inp : str = input(prompt)
        # if the user input is valid
        if inp.lower() in valid_inputs:
            return inp
        
        # if its not valid
        print(f"'{inp}' is not a valid input.")


def order_hotdog() -> tuple[float]:
    """
    Returns subtotal, tax, and total.

    Values would be wanted if integrated into a system
    """
    
    hotdog_types : dict = {"chili": 4.50, "hotdog": 3.50}
    type_prompt : str = "Which type of hotdog do you want? Chilidog (chili) for $4.50 or Hotdog (hotdog) for $3.50. "
    # hotdog_types.keys() gets the strings in the array and puts them into a list
    hotdog_type : str = is_valid_input(type_prompt, list(hotdog_types.keys()))

    hotdog_topping_types : dict = {"none": 0, "cheese": 0.50, "peppers": 0.75, "onions": 1.00}
    topping_prompt : str = "Which type of topping do you want? None (none) for $0, Cheese (cheese) for $0.50, \
Peppers (peppers) for $0.75 or Grilled onions (onions) for $1.00. "
    # hotdog_topping_types.keys() gets the strings in the array and puts them into a list
    hotdog_topping : str = is_valid_input(topping_prompt, list(hotdog_topping_types.keys()))

    # get the price using the name
    subtotal: float = hotdog_types[hotdog_type] + hotdog_topping_types[hotdog_topping]
    taxes: float = subtotal * 0.07
    total: float = subtotal + taxes

    return (subtotal, taxes, total)

if __name__ == "__main__":
    output : tuple[int] = order_hotdog()

    print(f"Subtotal: ${output[0]:.2f}\nTax: ${output[1]:.2f}\nTotal: ${output[2]:.2f}")