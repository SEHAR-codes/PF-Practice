# Question 1: String Concatenation (Combine first_name and last_name with a space in between)
first_name = "Jane"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)        # Output: Jane Smith


# Question 2: String Length (Find and print the length of this string)
message = "Hello Python"
print(len(message))     # Output: 12


# Question 3: Accessing Characters (Print the first and last character of the string)
text = "Programming"
print(f"First: {text[0]}, Last: {text[-1]}")   # Output: First: P, Last: g


# Question 4: String Slicing (Extract "Python" from this string)
text = "I love Python programming"
print(text[7:13])       # Output: Python


# Question 5: Removing Whitespace (Remove the extra spaces from the beginning and end)
text = "   Hello World   "
print(text.strip())     # Output: Hello World


# Question 6: Find Substring (Check if "World" exists in the string)
text = "Hello World"
print("World" in text)  # Output: True
