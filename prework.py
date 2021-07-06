#Different ways to do questions 1
#Mike's way 
# def hello_name(user_name):
#     print("Hello, " + user_name.title() + "!")

# hello_name("Nate")


# def greeting(user_name):
#     print("Hello, {}!".format(user_name.title()))
#     print(f"Hello, {user_name}. What is your favorite language?")

# greeting("Nate")


#Different ways for question 2
# n = 1
# Counter = 0
# while Counter < 100:
#     n += 2
#     print(n)
#     Counter += 1


def odds():
    for i in range(1,200,2):
        print(i)

odds()