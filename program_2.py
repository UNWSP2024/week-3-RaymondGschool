# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:
"""         Pseudocode

GET age and make it a number

IF age is less then or equal to 1
    SET ageCategory to 'infant'

ELSEIF age greater than 1 and less then 13
    SET ageCategory to 'child'

ELSEIF age greater than or equal to 13 and less than 20
    SET ageCategory to 'teenager'

ELSE
    SET ageCategory to 'adult'
ENDIF



"""


# If the person is 1 year old or less, it should display "infant" (without quotes).
# If the person is older than 1 year, but younger than 13 years, it should display "child".
# If the person is at least 13 years old, but less than 20 years old, it should display "teenager".
# If the person is at least 20 year old, it should display "adult".


def categorize_age(age):
    ageCategory = "TBD"
    ######################
    # WRITE YOUR CODE HERE
    ######################
    if age <= 1:
        ageCategory = 'infant'
    elif 1 < age < 13:
        ageCategory = 'child'
    elif 13 <= age < 20:
        ageCategory = 'teenager'
    else:
       ageCategory = 'adult'

    return ageCategory


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)