import subprocess
from fractions import gcd
from functools import reduce
import platform
import fractions 
import socket
import datetime
import time
import random
import os
import math
import sys

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print(
    """
    
░█████╗░░██████╗░█████╗░██╗██╗  ███╗░░░███╗░█████╗░███████╗░██████╗
██╔══██╗██╔════╝██╔══██╗██║██║  ████╗░████║██╔══██╗██╔════╝██╔════╝
███████║╚█████╗░██║░░╚═╝██║██║  ██╔████╔██║███████║█████╗░░╚█████╗░
██╔══██║░╚═══██╗██║░░██╗██║██║  ██║╚██╔╝██║██╔══██║██╔══╝░░░╚═══██╗
██║░░██║██████╔╝╚█████╔╝██║██║  ██║░╚═╝░██║██║░░██║██║░░░░░██████╔╝
╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═════╝░ [Version 1.0]
    """
)

# ᗩ⟆⊂⫯⫯ ⲙᎯ⨍⟆

# ▄▀█ █▀ █▀▀ █ █   █▀▄▀█ ▄▀█ █▀▀ █▀
# █▀█ ▄█ █▄▄ █ █   █░▀░█ █▀█ █▀░ ▄█

while True:
    # command prompt
    command = input(">_ ")
    command = command.strip()
    # ping command
    if command == 'ping':
        host = input("Enter website to ping: ")
        number = input("Enter how many times to ping: ")

        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            i_command = ['ping', param, number, host]
            return subprocess.call(i_command)
        print(ping(host))
    
    # this command
    elif command == 'this':
        print(f"Local IPS: {host_ip}")
        print(f"Desktop Name: {host_name}")
    
    # date command
    elif command == 'date':
        print(time.strftime("%m/%d/%Y"))
    
    # lst command
    elif command == 'lst':
        dir_list = os.listdir(path)
        print(f"Files and Directories in '{path}': {dir_list}")
    
    # new.file command
    elif command == 'new.file':
        name_of_file = input("Name of file: ")
        new_file = open(name_of_file, "w+")

    # .help command
    elif command == '.help':
        with open('Manual.txt', 'r') as f:
            contents = f.read()
            print(contents) 
    # pytimer
    elif command == 'pytimer':
        def countdown(h, m, s):
        
            # Calculate the total number of seconds
            total_seconds = h * 3600 + m * 60 + s
        
            # While loop that checks if total_seconds reaches zero
            # If not zero, decrement total time by one second
            while total_seconds > 0:
        
                # Timer represents time left on countdown
                timer = datetime.timedelta(seconds = total_seconds)
                
                # Prints the time left on the timer
                print(timer, end="\r")
        
                # Delays the program one second
                time.sleep(1)
        
                # Reduces total time by one second
                total_seconds -= 1
        
            print("TIME IS UP!")
        
        # Inputs for hours, minutes, seconds on timer
        h = input("Hours: ")
        m = input("Minutes: ")
        s = input("Seconds: ")
        countdown(int(h), int(m), int(s))

    # r function
    elif command == 'c':
        os.system('cls')
    
    # Calculator stuff: add; subtract; divide; multiply; factorial; exponent; gcf; lcm

    # add command
    elif command == 'add':
        n_of_n = int(input("How many number do you wish to add?: "))
        sum = 0
        for i in range(n_of_n):
            sum += int(input(f"Number {i+1}: "))
        print(f"Sum of all the digits entered: {sum}")
    
    # subtract command
    elif command == 'subtract':
        n1 = int(input("First number: "))
        n2 = int(input("Second number: "))
        diff = n1 - n2
        print(f"{n1} - {n2} = {diff}")

    # divide command
    elif command == 'divide':
        n1 = int(input("First number: "))
        n2 = int(input("Second number: "))
        quoti = n1 / n2
        round_or_no = str(input("Would you like to round the answer? [y/n]: "))
        round_or_no = round_or_no.lower()
        if round_or_no == 'y':
            print(f"{n1} ÷ {n2} = {round(quoti)}")
        else:
            print(f"{n1} ÷ {n2} = {quoti}")
    
    # multiply command
    elif command == 'multiply':
        n_of_n = int(input("How many number do you wish to multiply?: "))
        product = 1
        for i in range(n_of_n):
            product *= int(input(f"Number {i+1}: "))
        print(f"Sum of all the digits entered: {product}")

    # factorial command
    elif command == '-fac':
        n = int(input("Number: "))
        print(math.factorial(n))
        # n = 23
        # fact = 1
        # for i in range(1,n+1):
        #     fact = fact * i   
        # print ("The factorial of 23 is : ",end="")
        # print (fact)
    
    # exponent command
    elif command == 'exp':
        n1 = int(input("Number: "))
        n2 = int(input("Power: "))
        print(f"{n1**n2}")

    # factors command
    elif command == 'factor':
        n = int(input("Number: "))
        def print_factors(x):
            print(f"The factors of {x} are:")
            for i in range(1, x + 1):
                if x % i == 0:
                    print(i)
        print_factors(n)
    
    # log command
    elif command == 'log':
        n = int(input("Number: "))
        b = int(input("Base: "))
        print(f"Logarithm base {b} of {n} is {math.log(n, b)}")

    # nlog command
    elif command == 'nlog':
        n = int(input("Number: "))
        print(f"Natural Logarithm of {n} is {math.log(n)}")

    # Math visualization stuffs: area.quad; area.square; area.triangle -isosceles; area.triangle -right; peri.rect

    # area.quad command
    elif command == 'area.quad':
        ascii_char = str(input("Which ascii character do you wish to use as a representative for each shape? [!/@/#/$/%/^/&/*/|]: "))
        w = int(input("Width: "))
        l = int(input("Length: "))
        for i in range(w):
            print(f"{ascii_char} " * l)
        print(f"Dimensions: {l} {ascii_char} x {w} {ascii_char}")
        print(f"NOTE: the ascii characters only represent the units")

    # area.square command
    elif command == 'area.square':
        ascii_char = str(input("Which ascii character do you wish to use as a representative for each shape? [!/@/#/$/%/^/&/*/|]: "))
        side_len = int(input("Side Length: "))
        for i in range(side_len):
            print(f"{ascii_char} " * side_len)
        print(f"Dimensions: {side_len}x{side_len}")
    
    # pyth command
    elif command == 'pyth':
        a = int(input("Leg 'a': "))
        b = int(input("Leg 'b': "))
        c = (a**2) + (b**2)
        c = c**0.5
        print(f"Hypotenuse of the right angle triangle is {c}")

    # gcf command
    elif command == 'gcf':
        arr = []
        n_of_n = int(input("How many numbers do you want to find the GCF/GCD of?: "))
        for i in range(n_of_n):
            n = int(input(f"Number {i+1}: "))
            arr.append(n)
        print(arr)
        def find_gcd(list):
            x = reduce(gcd, list)
            return x
        print(find_gcd(arr))
    
    # lcm command
    elif command == 'lcm':
        n1 = int(input("First Number: "))
        n2 = int(input("Second Number: "))
        def compute_lcm(n1, n2):

            # choose the greater number
            if n1 > n2:
                greater = n1
            else:
                greater = n2
            while(True):
                if((greater % n1 == 0) and (greater % n2 == 0)):
                    lcm = greater
                    break
                greater += 1

            return lcm

        print("The L.C.M. is", compute_lcm(n1, n2))
        

    # Tests and stuff: test.add; test.subtract; test.divide; test.multiply; test.area

    # test.add command
    elif command == 'test.add':
        start_or_no = input("Start Test? [y/n]: ")
        start_or_no = start_or_no.lower()
        def quiz_1():
            prompt = int(input("How many questions do you wish to do?: "))
            score = 0
            for i in range(prompt):
                n1 = random.randint(0, 100)
                n2 = random.randint(0, 100)
                n1 += 1
                n2 += 1
                correct_ans = n1 + n2
                try:
                    ans = int(input(f"{n1} + {n2} = "))
                    if ans == correct_ans:
                        print("Correct!")
                        score += 1
                        # score increases
                    else:
                        print("Incorrect, you'll get the next one.")
                except:
                    print("Incorrect, you'll get the next one.")
            if score == prompt:
                print(f"NICE JOB! You got {score}/{prompt} = {round((score/prompt)*100)}%")
            else:
                print(f"Nice try, your score was {score}/{prompt} = {round((score/prompt)*100)}%")
                      
        # possibly add a timer to this.
        if start_or_no == 'y':
            quiz_1()
        else:
            print(" ")
    
    # test.subtract command
    elif command == 'test.subtract':
        start_or_no = input("Start Test? [y/n]: ")
        start_or_no = start_or_no.lower()
        def quiz_2():
            prompt = int(input("How many questions do you wish to do?: "))
            score = 0
            for i in range(prompt):
                n1 = random.randint(10, 100)
                n2 = random.randint(0, 100)
                n1 += 1
                n2 += 1
                correct_ans = n1 - n2
                # if correct_ans < 0:
                #     continue                    
                try:
                    ans = int(input(f"{n1} - {n2} = "))
                    if ans == correct_ans:
                        print("Correct!")
                        score += 1
                        # score increases
                    else:
                        print("Incorrect, you'll get the next one.")
                except:
                    print("Incorrect, you'll get the next one.")
            if score == prompt:
                print(f"NICE JOB! You got {score}/{prompt} = {round((score/prompt)*100)}%")
            else:
                print(f"Nice try, your score was {score}/{prompt} = {round((score/prompt)*100)}%")
                      
        # possibly add a timer to this.
        if start_or_no == 'y':
            quiz_2()
        else:
            print(" ")
        
    # test.divide -> a work in progress...

    # test.multiply command
    elif command == 'test.multiply':
        start_or_no = input("Start Test? [y/n]: ")
        start_or_no = start_or_no.lower()
        def quiz_3():
            prompt = int(input("How many questions do you wish to do?: "))
            score = 0
            for i in range(prompt):
                n1 = random.randint(0, 100)
                n2 = random.randint(0, 100)
                n1 += 1
                n2 += 1
                correct_ans = n1 * n2
                try:
                    ans = int(input(f"{n1} x {n2} = "))
                    if ans == correct_ans:
                        print("Correct!")
                        score += 1
                        # score increases
                    else:
                        print("Incorrect, you'll get the next one.")
                except:
                    print("Incorrect, you'll get the next one.")
            if score == prompt:
                print(f"NICE JOB! You got {score}/{prompt} = {round((score/prompt)*100)}%")
            else:
                print(f"Nice try, your score was {score}/{prompt} = {round((score/prompt)*100)}%")
                      
        # possibly add a timer to this.
        if start_or_no == 'y':
            quiz_3()
        else:
            print(" ")
        
    # test.area command
    elif command == 'test.area':
        start_or_no = str(input("Start Test? [y/n]: "))
        print(start_or_no)
        start_or_no = start_or_no.lower()
        def quiz_4(ascii_char):
            prompt = int(input("How many questions do you wish to do?: "))
            score = 0
            for i in range(prompt):
                w = random.randint(0, 10)
                l = random.randint(0, 10)
                for i in range(w):
                    print(f"{ascii_char} " * l)
                print(f"NOTE: the ascii characters only represent the units")
                correct_ans = l * w
                try:
                    ans = int(input(f"Dimensions: {l} {ascii_char} x {w} {ascii_char} = "))
                    if ans == correct_ans:
                        print("Correct!")
                        score += 1
                        # score increases
                    else:
                        print("Incorrect, you'll get the next one.")
                except:
                    print("Incorrect, you'll get the next one.")
            if score == prompt:
                print(f"NICE JOB! You got {score}/{prompt} = {round((score/prompt)*100)}%")
            else:
                print(f"Nice try, your score was {score}/{prompt} = {round((score/prompt)*100)}%")

        if start_or_no == 'y':
            charShape = str(input("Which ascii character do you wish to use as a representative for each shape? [!/@/#/$/%/^/&/*/|]: "))
            quiz_4(charShape)
        else:
            print(" ")
    
    # easter eggs

    # char to ascii converter
    elif command == 'ascii -gen':
        ch = input("Enter character: ")
        # converts char to ascii using ord()
        asc = ord(ch)
        print(f"ASCII code of {ch} is: {asc}")
    
    # egg
    elif command == '-e .egg':
        with open('holytxt.txt', 'r') as f:
            contents = f.read()
            print(contents) 
    
    # python
    elif command == 'python':
        import SNAKE
        print("Press enter once you're done.")

# IF I HAD MORE TIME I WOULD SEPERATE OR GROUP COMMANDS INTO DIFFERENT FILES FOR ORGANIZATION...