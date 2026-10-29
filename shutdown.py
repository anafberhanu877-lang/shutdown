# 1. Define the function exactly as required by the project
def shutdown(user_input):
    if user_input == "Yes":
        print("shutting down")
    elif user_input == "no":
        print("abort shut down")
    else:
        print("sorry.")

# 2. Use input() to get the response from the terminal
response = input("Enter your response: ")

# 3. Call the function using the input provided by the user
shutdown(response)
