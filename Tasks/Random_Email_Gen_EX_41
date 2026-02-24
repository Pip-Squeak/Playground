"""EX.41
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'
"""

"""
HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))
"""

"""
V1:
- Create 20 emails for each domain
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate-random_email_with_list_of_domains_v1.csv
"""
import random
import string


list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

rand_domains = random.choices(list_of_domains, k=5)
#print(rand_domains)

letters = string.ascii_lowercase + string.digits

print("\n============Random-Email-Addresses=============\n")

email_addresses = []

for i in range (10):
    
    for j in rand_domains:
        random_string = ''.join(random.choice(letters) for i in range(7))
        comp_emails = random_string + "@" + j
        email_addresses.append(comp_emails)
        
print(email_addresses)

print("\n============END==============")


with open ('./PYTHON_SECTION/Files/sample_files/random_email_addresses.txt', 'w') as emails:
 # Option 1
    # for i in email_addresses:
    #     emails.write(str(i))
    #     emails.write("\n")

# Option 2
    # trans_emails = ',\n'.join(email_addresses)
    # emails.write(trans_emails)

# Option 3 (short code)

    emails.write(',\n'.join(email_addresses))
