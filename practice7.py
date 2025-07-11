# DAY - 8
#Creating Variables and printing their values and lengths
name = "Pratyush Barik"
college = "KIIT"
email = "24155560@kiit.ac.in"
phone  = "9777055618"
print(f"Name : {name}\nCollege : {college}\nEmail : {email}\nPhone : {phone}")
print(f"length of name : {len(name)}\nlength of college : {len(college)}\nlength of email : {len(email)}\nlength of phone : {len(phone)}")
#String Manipulation
print(f"Name in uppercase : {name.upper()}\nName in Lowercase : {name.lower()}")
print(f"Name Slicing : {name[0:3]}")
print(f"e-Mail SLicing : {email[8:]}")
email = email.replace("kiit", "IIT")
print(f"Modified e-Mail : {email}")
name_1 = input("Enter your name : ")
count = 0
for i in name_1:
    if i.isupper():
        print(i, end=".")
        count += 1
    elif i.islower():
        count += 1
    else: 
        continue
print(f"\nTotal number of characters in your name : {count}")




