print("🌟 Contact Card 🌟")              
name = input("Input your name >")
print()
birth = input("Input your date of birth >")
print()
number = input("Input your telephone number >")
print()
email = input("Input your email >")
print()
address = input("Input your address >")
print()
contact={"givenname":name,"born":birth,"telephone":number,"emailaddress":email,"living":address}

print(f"Hi {contact['givenname']}. Our dictionary says that you were born on {contact['born']}, we call you on {contact['telephone']}, email {contact['emailaddress']}, or write to {contact['living']}.")
