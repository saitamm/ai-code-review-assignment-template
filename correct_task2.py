# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
import re
def extract_valid_emails(emails):
    count_valid_emails = 0
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,}$'
    for email in emails:
        if len(email)> 0 and re.match(email_pattern, email):
            count_valid_emails += 1
    return count_valid_emails