# Challenge 1:  add_List

# Prompt:
# - Write a function called add_list that accepts any quantity of numbers as arguments, adds them together and returns the resulting sum.
# - If called with no arguments, return 0 (zero).
# - If any non-number arguments are in the argument, return "NaN"


# Examples:
# add(1) //=> 1
# add(1,50,1.23) //=> 52.23
# add(7,-12) //=> -5
# add("peanut_butter", "marshmellow_fluff") //=> NaN

#-----------------------------------------------
# Solution Goes Here - >
def add_list(*nums):
    sum = 0
    num_list = []
    NaN = False
    for num in nums:
        if type(num) == int or type(num) == float:
            num_list.append(num)
        else:
            NaN = True
    for num in num_list:
        sum = sum + num
    if not NaN:
        print(sum)
    else:
        print('NaN')

add_list(1,2,4.3)
#-----------------------------------------------


# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

#-----------------------------------------------
# Solution Goes Here - >
def remove_ends(string):
    if type(string) == str and len(string) > 2:
        string = string[slice(1,-1)]
    else:
        string = ''
    print(string)

    # string.remove(string[-1])
remove_ends('okie dokie')
#-----------------------------------------------



# Challenge 3: is_palindrome

# Prompt:
# - Write a function called is_palindrome that accepts a single string argument, then returns true or false depending upon whether or not the string is a palindrome.
# - A palindrome is a word or phrase that is the same forward or backward.
# - Casing and spaces are not included when considering whether or not a string is a palindrome.
# - If the length of the string is 0 or 1, return true.
# Examples:
# is_palindrome('SEI Rocks'); //=> false
# is_palindrome('rotor'); //=> true
# is_palindrome('A nut for a jar of tuna'); //=> true
# is_palindrome(''); //=> true

#-----------------------------------------------
# Solution Goes Here - >
def is_palindrome(string):
    if type(string) == str:
        if len(string) > 1:
            string = string.lower()
            if string == string[::-1]:
                print(True)
            else:
                print(False)
        else:
            print(True)
    else:
        print('Not a string')

is_palindrome(True)
#-----------------------------------------------



# Challenge 4: is_prime

# Prompt:
# - Write a function named is_prime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
# - A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.
# Examples:
# is_prime(2) //=> true
# is_prime(3) //=> true 
# is_prime(4) //=> false
# is_prime(29) //=> true
# is_prime(200) //=> false

#-----------------------------------------------
# Solution goes here ->
def is_prime(num):
    prime = True
    test_digits = [2,3,4,5,6,7,8,9]
    if type(num) == int:
        if num == 1 or num == 2 or num == 3 or num == 5 or num == 7:
            prime = True
        elif num == 4 or num == 6 or num == 8 or num == 9:
            prime = False
        else:
            for digit in test_digits:
                result = num/digit
                test_result = str(result)
                if '.0' in test_result:
                    prime = False
                    continue
                else:
                   x = 1
    else:
        prime = 'Not an integer'
    print(prime)
is_prime(17)
#-----------------------------------------------




# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost if there is an 8.5% sales tax attached to each item. Then set up a conditional that adds a $10 Shipping Fee if the user lives in HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL. All other states recieve free shipping. 

# Your function should take the list and the user's homestate as arguments

shopping_cart = [ 
  {"item": "headphones", "price": 25},
  {"item": "speakers", "price": 40 },
  {"item": "microphone", "price": 70},
  {"item": "lamp", "price": 15 },
  {"item": "tower fan", "price": 35 },
]


#-----------------------------------------------
# Solution Goes Here ->
def total_checkout_cost(list,homestate):
    sum = 0
    for item in list:
        sum += item['price']
    sum *= 1.085
    if homestate == 'HI' or homestate == 'AK' or homestate == 'TX' or homestate == 'FL':
        sum += 10
        total_cost = sum
    elif homestate == 'AL' or homestate == 'MS' or homestate == 'NV' or homestate == 'IL':
        sum += 5
        total_cost = sum
    else:
        total_cost = sum
    print(f'Your total cost is {total_cost}')
    
total_checkout_cost(shopping_cart,'NJ')
#-----------------------------------------------


# Challenge 6: fizz_buzz

# Prompt -> Write a program that prints the numbers from 1 to 50. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
# If your argument is not a number, return "is not a number"

# Examples:
# fizz_buzz(10) //=> 10 "Buzz"
# fizz_buzz(30) //=> 30 "FizzBuzz"
# fizz_buzz(18) //=> 18 "Fizz"
# fizz_buzz(22) //=> 22 ""
# fizz_buzz(ham_sandwich) //=> "ham_sandwich is not a Number"

#-----------------------------------------------
# Solution Goes Here ->
def fizzbuzz():
    x = 0
    while x < 50: 
        x = x + 1
        if '.0' in str(x/3) and '.0' in str(x/5):
            print('fizzbuzz') 
        elif '.0' in str(x/3):
            print('fizz')
        elif '.0' in str(x/5):
            print('buzz')
        else:
            print(x)   
fizzbuzz()
#-----------------------------------------------




# Challenge 7 - Chessboard Creator

# A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

# Making a digital chessboard is an interesting way of visualising how loops can work together.

# Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.

# So chess_board(6,4) should return an array like this:

[
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"]
]
# And chess_board(3,7) should return this:


[
    ["O","X","O","X","O","X","O"],
    ["X","O","X","O","X","O","X"],
    ["O","X","O","X","O","X","O"]
]

#The white spaces should be represented by an: 'O' and the black an: 'X'

# The first row should always start with a white space 'O'


#-----------------------------------------------
# Solution Goes Here - >

def chess_board(rows, columns):
    i = 0
    board = []
    for r in range(rows):
        row = []
        for c in range(columns):
            if (r + c) % 2 == 0:
                row.append('O')
            else: 
                row.append('X')
        board.append(row)
    print(board)
#Kristina helped me a lot with this. Shoutout!
chess_board(8,8)
#-----------------------------------------------
