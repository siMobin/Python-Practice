n = int(input())

phone_numbers = []  # To store the formatted phone numbers

for _ in range(n):
    x = input()

    # Remove leading zero if present
    if x[0] == "0":
        x = x[1:]

    if x[0:2] == "91":
        x = "+" + x
    elif x[0:3] != "+91":
        x = "+91" + x

    # Format the number and store it in the list
    formatted_x = x[0:3] + " " + x[3:8] + " " + x[8:13]
    phone_numbers.append(formatted_x)

# Print the formatted numbers
for number in phone_numbers:
    print(number)
