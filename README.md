# Python Exception Handling for Division Operation

## 📌 Overview

This project demonstrates the implementation of **exception handling in Python** using `try-except` blocks. The program accepts two integer inputs from the user, performs integer division, and handles common runtime errors such as invalid input and division by zero.

The goal is to show how Python applications can gracefully manage unexpected situations without terminating abruptly.

---

## 🚀 Features

* Accepts user input for two integers
* Performs integer division using the `//` operator
* Handles invalid numeric input
* Prevents division by zero errors
* Displays meaningful error messages
* Beginner-friendly example of Python exception handling

---

## 🛠️ Technologies Used

* Python 3

---

## 📂 Project Structure

```text
├── exception_handling.py
├── README.md
```

---

## 💻 Source Code

```python
print("Program starts...")

try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a // b   # Integer division

    print("The division of", a, "and", b, "is", c)

except ValueError:
    print("Error in data : Number not provided correctly")

except ZeroDivisionError:
    print("Error in data : Divisor should not be zero")

except Exception as e:
    print("Error in data :", e)

print("Program ends...")
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/python-exception-handling.git
cd python-exception-handling
```

### Run the Program

```bash
python exception_handling.py
```

---

## 📋 Sample Outputs

### Successful Execution

```text
Program starts...
Enter first number : 20
Enter second number : 4
The division of 20 and 4 is 5
Program ends...
```

### Invalid Input

```text
Program starts...
Enter first number : abc
Error in data : Number not provided correctly
Program ends...
```

### Division by Zero

```text
Program starts...
Enter first number : 20
Enter second number : 0
Error in data : Divisor should not be zero
Program ends...
```

---

## 🧠 Concepts Covered

* Exception Handling
* `try`, `except` Blocks
* `ValueError`
* `ZeroDivisionError`
* Generic Exception Handling
* User Input Validation
* Integer Division

---

## 🔮 Future Improvements

* Add support for floating-point numbers
* Implement a menu-driven calculator
* Use `finally` blocks for cleanup operations
* Log exceptions to a file
* Create a GUI version using Tkinter

---

## 👨‍💻 Author

**Pranay Jadhao**

Electronics & Telecommunication Engineer

Aspiring Software & Embedded Systems Engineer

---

## 📄 License

This project is open-source and available for educational and learning purposes.

<img width="666" height="791" alt="image" src="https://github.com/user-attachments/assets/f1f865be-939c-4fa8-8b4c-e02108a4452a" />

<img width="710" height="795" alt="image" src="https://github.com/user-attachments/assets/377b96c7-21b9-4302-ac8c-99634541f426" />
