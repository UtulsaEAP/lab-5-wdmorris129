def feet_to_steps(user_feet):
    # Assuming an average step length of 2.5 feet
    step_length = 2.5

    # Calculate the number of steps
    steps = user_feet / step_length

    return steps

if __name__ == '__main__':
    # Take user input for feet
    user_feet = float(input("Enter the distance in feet: "))

    # Call the feet_to_steps function and store the result
    result_steps = feet_to_steps(user_feet)

    # Display the result
    print(f"{user_feet} feet is approximately {result_steps:.2f} steps.")