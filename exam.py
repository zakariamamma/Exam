# hello guys now i finish learning basics in python and here i test myself 
import time # i write import to use fonction time.sleep(number) 
# first class
print("studing First ")
print()

greeting = input("enter your name here >>> ")

print(f"hello {greeting} how are you , im so happy to meet you ")
time.sleep(3)

point = 0 # first value

# x + 2 = 9


def Q1():
  global point # here i use global to keep point in ll programme
  while True :
    print("\033[34mYou have this equation X + 12 = 6/2 \nwhat value of X = ?\n\033[0m")
    print()
    time.sleep(2)
    repeat = input(" ==> Do you want to continue : type yes or no :) >>> ").lower()
    if repeat != "yes":
      break
      print()
    time.sleep(2)

    X = float(input("enter the Value >>> "))
    print()
    time.sleep(2)

    equation = int( X + 12 == 6/2 )
    if equation == True:
        print(f" ==> yes \033[32m{X}\033[0m is solution \033[34m-9 +12 = 6/2\033[0m ")
        point += 1
        break

    else :
      print("\033[31mFALSE\033[0m")
      break

print()

def Q2():
  global point
  lists = ["Zakaria","Younes","Akram"]
  print("\033[33mthis is list hase a 3 character names ")
  print()
  print(30*"=")
  for i in lists: # | Here i use for loop to print all items inside my list
    print(i)      # |
    time.sleep(3/2)
  time.sleep(2)
  print("what is fonction to delete name 'akram'")
  print()
  print(30*"=")
  time.sleep(2)

  question = int(input("1_ append \n2_clear \n3_remove\n\033[0m"))
  time.sleep(2)
  print()
  if question == 1:
    print("\033[31mFalse : append is fonction to add item in list\033[0m")
    # don't forgot
  elif question == 2 :
    print("\033[31mFalse : clear is remeved all items in lists\033[0m")

  elif question == 3:
    print("\033[32m True \033[0m")
    point += 1
    # don't forgot
  else:
    print("\033[31mValue error enter number 1 to 3 \033[0m")
    # don't forgot


def Q3():
  global point
  example_dict = {
      "name" : "youssef",
      "age" : 27
  }

  print("\033[33mhere we have a dictioneryse hase a name\033[0m")
  print(30*"=")
  time.sleep(2)
  print("\033[33m1_example_dict.insert(name)\n2_example_dict(name)='amin'\n3_example_dict['name'] = 'amin'\033[0m")
  print()
  time.sleep(2)
  print("\033[33mhow to change value of name ?\033[0m")
  print(30*"=")

  question = int(input("enter your result >>> "))
  print()
  time.sleep(3)
  if question == 1:
    print("\033[31mFalse : this list is dict\033[0m")
    # don't forgot

  elif question == 2 :
    print("\033[31mFalse : don't use tuple\033[0m")

  elif question == 3:
    print("\033[32mTrue\033[0m")
    point += 1
    # don't forgot
  else:
    print("\033[31mValue error enter number 1 to 3 \033[0m")
    print()

def Q4():
  global point
  print("\033[33mhere we have a fonction while loop\033[0m")
  time.sleep(2)
  print("\033[33myou have value i = 5 ,when a good chose\033[0m")
  print()

  question = int(input("While i : \n1_While i > or < 0:\n2_While i = 0:\n3_While i: "))
  time.sleep(3)
  if question == 1:
    print("\033[32mTrue\033[0m")
    point += 1
    # don't forgot
  elif question == 2 :
    print("\033[31mFalse\033[0m")

  elif question == 3:
    print("\033[31mFalse\033[0m")
    # don't forgot
  else:
    print("Value error enter number 1 to 3 ")



print(Q1())
print(Q2())
print(Q3())
print(Q4())
time.sleep(5/2)
print(f"now \033[32m{greeting}\033[0m you return a \033[35m{point}\033[0m/4 point ")
time.sleep(3/2)
if 3 <= point <= 4:
  print("\033[32m that so perfect \033[0m")
elif 2 <= point <= 3:
  print("\033[33m that is not bad you can to continue \033[0m") # Finaly i use if & elif else to send message with result 
else:
  print("\033[31m no you should to go a back \033[0m")

  print("Thanks for use my programme :)")