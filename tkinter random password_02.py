import tkinter as tk
from functools import partial
import random
import array
root = tk.Tk()
root.title("Railway Password")
root.geometry('320x150')
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',]

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

def call_result(label_result, n1, label_result1, n2):
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    if (number1.get() and number2.get()):
        #phone=int(number2)
        phone = len(number2.get())
        if(phone==10):
            #if(number1.get() == str):
                if(number2.get().isdigit()):
                    #print("hi")
                    #for x in range(4):
                    temp_pass = temp_pass
                    label_result.config(font=('arial',12,'bold'),text="Your Password = %s" % temp_pass)
                    labelResult.grid(row=4, column=2)
                    return
                    # the user entered data in the mandatory entry: proceed to next step
                    #print("next step")
                else:
                    label_result.config(font=('arial',12,'bold'),text="must give numbers")
                    labelResult.grid(row=4, column=2)
        else:
            label_result.config(font=('arial',12,'bold'),text="10 number is important")
            labelResult.grid(row=4, column=2)
            #print("hi")
    else:
        label_result.config(font=('arial',12,'bold'),text="mandatory data missing")
        labelResult.grid(row=4, column=2)
        # the mandatory field is empty
        #print("mandatory data missing")
        #(number1.focus_set() and  number2.focus_set())
number1 = tk.StringVar()   
number2 = tk.StringVar()
#number2 = tk.IntVar()

labelNum1 = tk.Label(root, font=('arial',12,'bold'),text="UserName").grid(row=1, column=0)  
labelResult = tk.Label(root)  
labelResult.grid(row=1, column=3)

labelNum2 = tk.Label(root, font=('arial',12,'bold'),text="MobileNumber").grid(row=2, column=0)  
labelResult1 = tk.Label(root)  
labelResult1.grid(row=2, column=3)

entryNum1 = tk.Entry(root, font=('arial',14,'bold'), textvariable=number1,width=15,bg="#eee",bd=5).grid(row=1, column=2)  
call_result = partial(call_result, labelResult, number1)

entryNum2 = tk.Entry(root, font=('arial',14,'bold'), textvariable=number2,width=15,bg="#eee",bd=5).grid(row=2, column=2)  
call_result = partial(call_result, labelResult1, number2)

buttonCal = tk.Button(root, text="Result", width=10,command=call_result).grid(row=3, column=0)

