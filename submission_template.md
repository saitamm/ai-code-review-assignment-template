# AI Code Review Assignment (Python)

## Candidate
- Name:Soumaya Ait Ammi
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- **Counting cancelled orders incorrectly** :The Average Order Value is calculated by dividing total revenue by the number of orders, but the current function includes cancelled orders in the count.
- **Division by Zero** : If the orders list is empty, the count is 0, which will cause a division by zero error (crash).
- **Adding string to int** : If order["amount"] is a string, the code will throw a type error when performing arithmetic.

### Edge cases & risks
- **Empty orders list.**
- **Orders marked as "CANCELLED" instead of "cancelled".**

### Code quality / design issues
- **Hard Code** : The keys "cancelled" and "status" are hard-coded in the function.
- **No Documentation** : The function lacks comments or docstrings explaining its behavior.
- **Poor naming**: Variables total and count are unclear. Better names would be total_amount and valid_orders_count.
## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
 - Verify that the function doesn’t crash and returns a sensible value.
 - Ensure that with normal orders, the average is calculated correctly.
## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- there is missing in the deffenition of the average order value 

### Rewritten explanation
- This function calculates the average order value by summing the amounts of all non-cancelled orders (after converting them to numbers if needed) and dividing by the count of non-cancelled orders. If there are no valid orders, it returns 0 to avoid division by zero.


## 4) Final Judgment
- Decision: Request Changes
- Justification: The code and explanation need more detail on data types, handling of string amounts, empty order lists, and cancelled orders to ensure correct calculations.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- **validation mail** : the containe of @ doesn't means the mail is valid 
- **emails** : we have to check the mail is not empty
### Edge cases & risks
- **Empty emails list.** : if the emails is an empty list the count == 0 so the program crached 
- **"@" in email** : if the mail == "@" the condition is correct but the mail not valid because the mail will be valid with this form (domain@mail.com)

### Code quality / design issues
- **Hard Code** : looking for @ in the mail.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Updated validation logic to check for non-empty emails and proper email format using regex instead of only checking for @.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- **Empty email list**
-**Emails with missing @ or domain**
## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision:  Request Changes 
- Justification:The original code uses insufficient validation logic and doesn’t handle edge cases like empty or malformed emails.
- Confidence & unknowns: High confidence in identified issues; unknowns include whether some unconventional but valid emails might be incorrectly rejected.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- **Counting the None  incorrectly**:None values are included in calculations, giving wrong results.
- **divide by Zero**:Happens if there are no valid orders; dividing by zero will crash.
- **empty values**:Empty or missing fields cause errors when processing amounts.

### Edge cases & risks
- **Divide By Zero**
- **Not specific Type**


### Code quality / design issues
- **Lack of input validation**
-**Lack of clear variable names (total and count are unclear)**

## 2) Proposed Fixes / Improvements
### Summary of changes
- Updated the function to ignore None values, skip invalid types, and safely handle empty lists to avoid division by zero.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- **List with only None values**
- **Mixed types (numbers and strings)**
- **Normal list of numeric measurements**

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- specify the type

### Rewritten explanation
- This function calculates the average of valid numeric measurements. It ignores None values and any non-numeric entries, and safely handles empty input lists to avoid division by zero.

## 4) Final Judgment
- Decision:Request Changes
- Justification:The original code may fail on empty lists or invalid types; the explanation is incomplete regarding type handling and edge cases.
- Confidence & unknowns:High confidence in identified issues; unknowns include possible unusual measurement types.
