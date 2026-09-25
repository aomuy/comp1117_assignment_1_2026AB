# A1 Museum Ticketing: My Specifications
## Input and output types
- **Input Variables:** 
Use these as variable names directly.
- day: int between 1 and 8. Days 1 to 5 means a weekday, days 6 and 7 mean a weekend, and day 8 means a holiday.
- age: int between 0 and 80, or -1. The program will continuously ask for user input and assign it to int, until -1 was inputted. Read the input with input("Enter age (-1 to stop): ") 

- **Outputs:** 
After input ends, print exactly these nine lines and nothing else. Labels, capitalisation, and punctuation must match exactly. The three money values Discount, Service fee and Total cost must always show two decimal places; the other values are plain integers.
Day type: <weekday|weekend|holiday>
Children: <int>
Adults: <int>
Seniors: <int>
Total people: <int>
Groups formed: <int>
Discount: <0.00>
Service fee: <0.00>
Total cost: <0.00>

## Variables
Use these as variable names directly.
- children
- adults
- seniors
- groups_formed
- cost
- discount
- service_fee
- total_cost
All variables above are initialized to 0.
You may also use other variables if necessary.

## Rules
### Program Logic Flow
1. Each time a valid number is assigned to age, check if age <= 12 then children+1, elif age >= 60 then senior+1, else adult+1
2. After the input phrase ends, ie user inputs -1, calculate the maximum number of groups of exactly 5 that can be formed and assign it to groups_formed. Only adults can form groups. Adults in a group pay the group price while those that cannot form a group of 5 pay the adult price. A person is never charged both a group price and an individual price.
3. Calculate the total ticket price based on the following table:
|         | Child | Adult | Senior | Group price |
|---------|------:|------:|-------:|------------:|
| Weekday | 30    | 60    | 40     | 35          |
| Weekend | 40    | 80    | 50     | 65          |
| Holiday | 50    | 100   | 60     | 75          |
store the calculated value in cost.
4. Check if the day is on a weekend or holiday and least one complete group was formed. If yes, assign 0.1*cost to discount. 
5. Check if weekday and there are fewer than 3 visitors. If yes, the service fee is 0. Else a service fee of 5 per person is added, but capped at 30. Assign the result to service_fee
6. calculate the total price with cost-discount+service_fee and assign it to total_cost.

### Project instructions for AI
Follow the bullet points below STRICTLY when writing code. 
1. Only use the basic types int, float, str and bool; input() and print(); conditionals if, elif and else; loops; and operators in your program. Do not use anything outside this: no lists, no dictionaries, no functions of your own, and no try and except statements.
2. Strictly follow this file while you are implementing the code. If there are any ambigurity in the specifications or user prompt, you must ask for clarifications before proceed. Never make assumptions or invent rules. 
3. If you think the user has written something wrong, point it out, implement anyway, add comments next to the wrong code to briefly explain what is wrong, and ask the user to correct themself. Never implement what you think is right if it is not mentioned in this file.