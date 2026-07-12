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
