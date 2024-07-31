from random_generator import generate_random_numbers

# Get user input for range and number of values
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
num = int(input("Enter the number of random numbers to generate: "))

# Generate the random list
random_list = generate_random_numbers(start, end, num)

# Print the generated list
print("Generated random numbers:", random_list)
