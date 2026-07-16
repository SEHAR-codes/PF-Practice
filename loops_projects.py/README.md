###Explanation of while loop projects
### Program 1: Print Even Numbers from 1 to 20

* num = 1 – Starts the variable from 1.
* while num <= 20: – Runs the loop until 20.
* if num % 2 == 0: – Checks if the number is even.
* print(num, end=" ") – Prints the even number.
* num += 1 – Increases the number by 1.
* print() – Moves to the next line.


### Program 2: Calculate Average of Positive Numbers

* sum_numbers = 0 – Stores the total sum.
* count = 0 – Counts the numbers entered.
* while True: – Starts an infinite loop.
* num = int(input(...)) – Takes input from the user.
* if num < 0: – Checks for a negative number.
* break – Stops the loop.
* sum_numbers += num– Adds the number to the sum.
* count += 1 – Increases the count.
* if count > 0: – Checks if numbers were entered.
* average = sum_numbers / count – Calculates the average.
* print(...) – Displays the sum, count, and average.
* else: – Runs if no positive numbers were entered.
* print(...)– Displays a message if no positive numbers were entered.

### **3. Factor Finder Program**

* Takes a positive number as input.
* Starts checking from **1** up to the entered number.
* Finds numbers that divide the input without a remainder.
* Prints all the factors of the number.
* Ends after checking all numbers.

### **4. Password Checker Program**

* Stores the correct password.
* Allows the user **3 attempts** to enter the password.
* Checks if the entered password is correct.
* Grants access if the password is correct.
* Shows an error message for incorrect passwords.
* Locks the account after 3 unsuccessful attempts.

### **5. Prime number checker**

1. num = 97 stores the number to be checked.
2. If num <= 1, it is **not a prime number**.
3. If num == 2, it is **a prime number**.
4. Otherwise, assume the number is prime by setting is_prime = True.
5. Use a for loop to check divisibility from 2 to the **square root** of the number.
6. If the number is divisible by any value, set is_prime = False, display the divisor, and stop the loop.
7. After the loop:

   * If is_prime is True, print that the number is **PRIME**.
   * Otherwise, print that the number is **NOT prime**.
  
### **6. multiplication tables from 1 to 5.**
* The first loop runs from 1 to 5.
* The second loop runs from 1 to 10.
* Each table is printed one by one.
* It multiplies the current number with numbers from 1 to 10.
* The result is displayed in the format `number x number = result`.
* A blank line is printed after each table.
* The program prints the multiplication tables from 1 to 5.

