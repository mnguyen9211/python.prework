# Question 1
def hello_name(user_name):
    print(f"hello_{user_name}")

hello_name("USERNAME")

# Question 2
def first_odds():
    for n in range(0, 101):
        if n % 2 != 0:
            print(n)

first_odds()

# Question 3

def max_num_in_list(a_list):
    a_list.sort()
    position = len(a_list)
    print(a_list[position - 1])

sample_list = [100, 9, 8, 7 ,6, 250000, 0]
max_num_in_list(sample_list)

# Question 4

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 4 ==0 and a_year % 100 != 0:
        return True
    else:
        return False
year = int(input("Enter a year\n"))
print(is_leap_year(year))

# Question 5

def is_consecutive(a_list):
    count = 0
    list_legnth = len(a_list)
    for n in a_list[0:list_legnth-1]:
        count += 1
        if n + 1 == a_list[count]:
            x = True
        else:
            x = False
            break
    return bool(x)

list2 = [0,1,2]
print(is_consecutive(list2))
list3 = [1,10,4,5,6,7]
print(is_consecutive(list3))