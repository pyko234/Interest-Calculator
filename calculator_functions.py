from math import e

def compound_interest_per_year(principal, rate, time, compound_per_year):
    """
    Function to calculate compounding interest when interest is not continuous.

    Args:
    principal (float): The inital amount of money.
    rate (float): The annual interest rate (expressed as a decimal).
    time (int): the number of years the interest is compounded for.
    compound_per_year (int): The number of times the interest is compounded per year.

     Returns:
     float: The total amount after compounding interest.
    """

    amount = principal * (1 + rate / compound_per_year) ** (compound_per_year * time)

    return amount

def compound_interest_continuously(principal, rate, time):
    """
    Function to calculate the continuous compounding interest.

    Args:
    principal (float): The inital amount of money.
    rate (float): The annual interest rate (expressed as a decimal).
    time (int): the number of years the interest is compounded for.

    Returns:
    float: The total amount after compounding interest.
    """

    amount = principal * e ** (rate * time)

    return amount

def main():
    """
    Function to test other functions
    """

    principal = float(input("Please input inital value: "))
    time = int(input("Please input amount of time the value will collect interest (in years): "))
    rate = float(input("Please insert the rate (in decimal form): "))
    compound_per_year = input('Please input the amount of times the interest will be compounded per year (for continuous input "oo")') 
    
    if compound_per_year == "oo":
        total = compound_interest_continuously(principal, rate, time)
    else:
        total = compound_interest_per_year(principal, rate, time, float(compound_per_year))

    print(f"Your total is : {total}")


if __name__ == "__main__":
    main()