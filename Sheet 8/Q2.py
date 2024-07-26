def even(number):
    return 1 if number % 2 == 0 else 0

def main():
    while True:
        try:
            user_input = input("Enter an integer (or type 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            number = int(user_input)
            if even(number):
                print(f"{number} is even.")
            else:
                print(f"{number} is odd.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
