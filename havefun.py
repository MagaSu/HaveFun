# -*- coding: utf-8 -*-
from termcolor import colored
import subprocess
import time
import pyautogui
import os
subprocess.call('', shell=True)

def SendMessage():
    time.sleep(2)
    # The message you want to send
    message = "U ARE UGLY"
    # How many times do i send a message?
    iterations = 50

    for i in range(iterations):
        pass

    while iterations > 0:
        iterations -= 1

        pyautogui.typewrite(message.strip())
        pyautogui.press('enter')


def SendScript():
    time.sleep(2)
    with open('script.txt') as f:
        lines = f.readlines()
    for line in lines:
        pyautogui.typewrite(line.strip())
        pyautogui.press('enter')


print(colored('~'*50, 'red'))
print(colored('Welcome bro \(O V O)/', 'green'))
print(colored("Let's make fun of someone?", 'green'))
print(colored('~'*50, 'red'))


print(colored("\t[1] ===> Resend the same message (─__─)", 'magenta' ))
print(colored("\t[2] ===> Send titles from the script \(v _ v)/", 'magenta'))

print(colored('~'*50, 'red'))
print('\n')
text_a = input(colored('[Choose an option]==> ', 'cyan'))

if text_a == "1":
    SendMessage()
elif text_a == "2":
    SendScript()
else:
    print(colored('Choose a function! ¯\_(-_-)_/¯', 'red'))
    text_a = input(colored('[Choose an option]==> ', 'cyan'))
    if text_a == "1":
        SendMessage()
    elif text_a == "2":
        SendScript()
    else:
        print(colored('Come back when you find your glasses ^_^', 'yellow'))

print(colored("\n" 'Do you want to try again? XD', 'green'))
symb = input(colored('Yes or No?: ', 'cyan'))
if symb == "Yes" or symb == "yes":
    os.system("havefun.py")
elif symb == "No" or symb == "no":
    print(colored('See you later dude!', 'magenta'))
    exit(0)
else:
    print(colored("Damn man, you're so lazy", 'red' ))
