"""
Program: camper_age_input.py
Author: Levi Shepherd
Last date modified: 09/07/2020



The purpose of this program is to accept input of
a child's age in years and then output the age of the
child in months.
"""


def convert_to_months(years):
    MONTHS_IN_YEAR = 12
    months = years * MONTHS_IN_YEAR
    return months


if __name__ == '__main__':
    # Ask user for input of child's age and cast the input to an integer
    age_in_years = int(input("Enter the child's age in years: "))

    # Pass the input value to the function to calculate age to months
    age_in_months = convert_to_months(age_in_years)

    # Display the input of years and output of months to user
    print(str(age_in_years) + " years is " + str(age_in_months) + " months.")
