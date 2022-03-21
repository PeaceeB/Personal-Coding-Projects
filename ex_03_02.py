strhours = input("Enter Hours:")
strrate = input("Enter Rate:")
try:
    fh = float(strhours)
    fr = float(strrate)
except:
    print("Error, please enter numeric input")
    quit()

print(fh,fr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    pay = reg + otp
else:
    pay = fh * fr
print("Pay:",pay)
