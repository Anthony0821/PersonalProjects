name = input("Please enter your name: ")
print(f"\nHello,{name}!")
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
age = input("How old are you?: ")
age = int(age)
if age >= 21:
    print("Nice!! Have a drink and relax before you get stared.")
else:
    print("Let's get started")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
