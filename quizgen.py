import random

func = ["sin","cos", "tan", "cot", "sec", "csc"] #set func as a list of trigonometric functions
values = [30,45,60,90,120,135,150,180,210,225,240,270,300,330,315,360] #possible values on unit circle

with open('exam.txt', 'w') as f: #write to file exam.txt
    for item in range(15): #loop
        prob = str(random.choice(func))+ "("+ str(random.choice(values))+ ")=" #generate random function and value
        prob = str(prob) #convert generated output to string
        f.write(prob+"\n\n") #write string to file, which you can find in your home directory
