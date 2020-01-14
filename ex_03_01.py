hrs = input ('Enter Hours: ')
rt = input ('Enter Rate: ')
try:
    fh = float (hrs)
    fr = float (rt)
except:
    print("Error, please enter numeric input")
    quit ()
print(fh, fr)
if fh > 40.0 :
    reg = fr *fh
    ovt = (fh - 40.0) * (fr * .5)
    print (reg,ovt)
    py = reg + ovt
else:
    py = fh * fr
print('Pay: ',py)
