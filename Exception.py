# wa code yar 
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Program execution completed.")
