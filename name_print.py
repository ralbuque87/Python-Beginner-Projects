while True:
    fn = input("Enter First Name: ")
    if len(fn) == 0:
        print("First Name is Blank. Try Again ")
        continue
    else:
        break

while True:
    ln = input("Enter Last Name: ")
    if len(ln) == 0:
        print("Last Name is Blank. Try Again ")
        continue
    else:
        break

print("Your name is" + " " + fn + " " + ln)


# continue goes to start of loop, break exits loop
