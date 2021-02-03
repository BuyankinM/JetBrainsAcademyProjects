# Save the input in this variable
ticket_number = input()

# Add up the digits for each half
half1 = sum(int(c) for c in list(ticket_number[:3]))
half2 = sum(int(c) for c in list(ticket_number[3:]))

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")