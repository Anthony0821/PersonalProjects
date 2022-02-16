responses = {}
# set a flag  to indicate that poling is active
polling_active = True
while polling_active:
    # prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would yoou like to climb someday")
    # Store the response in the dictionary.
    responses[name] = response
    # find out if any one else is willing to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        # Polling is coomplete. Show the Results.
        print("\n---Poll Results ---")
        for name, response in responses.items():
            print(f"{name} would like to climb {response}.")
