import random
import string

"""
Read the list of email addresses from the input file and create a dictionary
with keys being domain name and value being the number of occurrences for the domain.
In other words count how many times each domain exists and create a report of the count as a dictionary.
Save the output into a .json file.

Example output:
{'yahoo.com': 19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}

"""

input_file = ".\PYTHON_SECTION\Files\exercises\count_domains_in_email_list_file_exercise_input.csv"
output_file = "count_domains_in_email_list_file_exercise_output.json"

with open (input_file, 'r') as f:
    email_list = [line.rstrip() for line in f]# 10 character Emails



email_list = [s.replace(',', '') for s in email_list]
split_emails = {email.split('@')[0]: email.split('@')[1] for email in email_list}

yahoo = 'yahoo.com'
gmail = 'gmail.com'
msn = 'msn.com'
sqa = 'supersqa.com'
outlook = 'outlook.com'


count_yahoo = sum(1 for value in split_emails.values() if value == yahoo)
count_gmail = sum(1 for value in split_emails.values() if value == gmail)
count_msn = sum(1 for value in split_emails.values() if value == msn)
count_sqa = sum(1 for value in split_emails.values() if value == sqa)
count_outlook = sum(1 for value in split_emails.values() if value == outlook)


print('\n')
print(f"yahoo.com: {count_yahoo}\ngmail.com: {count_gmail}\nmsn.com: {count_msn}\nsupersqa.com: {count_sqa}\noutlook.com: {count_outlook}")

print('\n')


with open (output_file, 'w') as f:
    f.write(f"yahoo.com: {count_yahoo}\ngmail.com: {count_gmail}\nmsn.com: {count_msn}\nsupersqa.com: {count_sqa}\noutlook.com: {count_outlook}")
