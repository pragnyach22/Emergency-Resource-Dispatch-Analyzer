Project Description
This Python program classifies user-entered integer values into different demand categories and applies a personalized filtering condition based on the length of a given name.
The system:
Accepts n integer inputs from the user
Categorizes values into demand groups
Applies a personalized removal condition using a calculated PLI value
Displays updated results

Features
Input Collection
User enters the number of elements
User inputs integer values
All values are stored in a list

Demand Classification
Each input value is classified as:
Condition	Category
value < 0	Invalid Requests
value = 0	No Demand
1 – 20	Low Demand
21 – 50	Moderate Demand
> 50	High Demand

Personalized Logic Index (PLI)
The program calculates:
L = Length of name (excluding spaces)
PLI = L % 3
For the name:
"Pragnya sree"
If:
PLI = 0 → Remove all Low Demand values
PLI = 1 → Remove all High Demand values
PLI = 2 → Remove Low Demand, High Demand, and Invalid Requests

Output Display
The program prints:
Lists before applying personalized condition
Lists after applying personalized condition
Total valid requests
Number of removed entries

How to Run
Open terminal or command prompt
Run the Python file:
python filename.py
Enter:
Number of elements
Integer values when prompted

Example
Input:
enter no of elements: 5
enter value: 10
enter value: 25
enter value: -3
enter value: 0
enter value: 60

Output:
Low Demand: [10]
Moderate Demand: [25]
High Demand: [60]
Invalid: [-3]
Total Valid Requests: 4
Removed Entries: Based on PLI

Learning Concepts Covered
Lists
Loops
Conditional statements
Modulus operator

String operations

Basic data classification logic# Emergency-Resource-Dispatch-Analyzer
