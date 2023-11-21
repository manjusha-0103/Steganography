import os
import cv2
import subprocess
import sys


def makeKey():
    d={}
    c={}
    for i in range(255):
        d[chr(i)]=i
        c[i] = chr(i)
    return d,c

def encryptMessag(message, password):
    tmp=subprocess.call('cls',shell=True)
    print("...........................................................")
    img = cv2.imread("bgimage.png")
    d,c = makeKey()
    m=0
    n=0
    z=0
    input("\nEncryption strated.........")
    for i in range(len(message)):
        img[n,m,z] = d[message[i]]
        n=n+1
        m=m+1
        z=(z+1)%3

    cv2.imwrite("Encryptedmsg.jpg",img)
    input("\nMeassage is encrypted successfully with image ...........")
    return img

def decryptMeassage(password,message,img):
    tmp=subprocess.call('cls',shell=True)
    print("...........................................................")
    msg =""
    d,c = makeKey()
    n=0
    m=0
    z=0

    print("\n Enter passcode for Decryption : ")
    paswd = input("Pasword : ")

    if password == paswd:
        for i in range(len(message)):
            msg = msg + c[img[n,m,z]]
            n=n+1
            m=m+1
            z=(z+1) % 3
    return msg

        

def getUserInputs():
    tmp=subprocess.call('cls',shell=True)
    print('...........................................................')
    print("\nEnter the meassage that you wan to hide")
    message = input("Message : ")
    print('...........................................................')
    print("\nEnter the Password")
    password = input("Password : ")
    return message,password

def menu():
    tmp=subprocess.call('cls',shell=True)
    print("\n                 ***** Steganography *****                 ")
    print('...........................................................')
    print('Make a Choice')
    print('...........................................................')
    print("s.HIDE MESSAGE IN IMAGE")
    print("d.SHOW HIDDEN MESSAGE")
    print('x.EXIT PROGRAM')
    print('...........................................................')
    print('Enter the choice :',end='')
    choice=input().lower()
    return choice

def showMessage(msg):
    if msg !="":
        print("\nHidden message : ",msg,end = '')
    else :
        print("\nIncorrect Password")
    input("\n........")

def main():
    password = ""
    message = ""
    img = None
    while True:
        choice = menu()
        
        if choice == 's':
            message, password = getUserInputs()
            img = encryptMessag(message,password)
            
        if choice == 'd':
            
            if message!= "" :
                msg = decryptMeassage(password,message,img)
                showMessage(msg)

            else : 
                input("First Eneter message and password ...........")
                choice = menu()

        if choice == 'x':
            print('Thank YOU !!!🙏️')
            print("...........................................................")
            print("Exited")
            sys.exit(0)
        
        print()

if __name__ == "__main__":
    main()