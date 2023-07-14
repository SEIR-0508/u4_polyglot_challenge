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

### resource used: https://www.geeksforgeeks.org/args-kwargs-python/

def add_list(*nums):
    sum = 0
    if nums != '':
        for num in nums:
            if type(num) != int:
                print('NaN')
            else:
                sum += num
        print(sum)
    else:
        print('0')

# add_list(1, 2, 3, 1)
# add_list(1, 2, 3, 1, 10)
# add_list()
# add_list('catdog', 1, 1)

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
    if len(string) < 3:
        print("")
    else:
        ### first attempt at solution:
        # remove_first = string.replace(string[0], "")
        # new_string = remove_first.replace(remove_first[-1], "")
        # print(new_string)

        ### better solution:
        print(string[1:-1])
        ### resource used: https://www.w3schools.com/python/gloss_python_string_slice.asp

# remove_ends('hello')
# remove_ends('a')
# remove_ends('asdlfkajsdlf')


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
    if len(string) <= 1:
        print('true')
    else:
        reverse = string[::-1] # <-- string[start : end : step]
        if reverse.lower().replace(" ","") == string.lower().replace(" ",""):
            print('true')
        else:
            print('false')

# is_palindrome('hello')
# is_palindrome('a')
# is_palindrome('RadAr')
# is_palindrome('Ra dAr')
# is_palindrome('A nut for a jar of tuna')

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

# evenly divisible -> NOT a FLOAT -> int

def is_prime(num):
    int(num)
    counter = 0
    if num >1 and num % num == 0:
        counter += 1
        if num % counter == 0:
            print('false')
        else:
            print('true')
    else:
        print('false')

# is_prime(3)
# is_prime(200)



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

def total_cost(cart, state):
    subtotal = 0
    if state in ['HI', 'AK', 'TX', 'FL']:
        shipping_fee = 10
    elif state in ['AL', 'MS', 'NV', 'IL']:
        shipping_fee = 5
    else:
        shipping_fee = 0
    for item in cart:
        subtotal += item["price"]
    total = subtotal + shipping_fee
    print(total)

# total_cost(shopping_cart, 'HI')
# total_cost(shopping_cart, 'CT')
# total_cost(shopping_cart, 'AL')

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

def fizz_buzz():
    nums = range(1, 51, 1)
    for num in nums:
        if num % 3 == 0 and num % 5 == 0:
            print('fizzbuzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        else:
            print(num)
# fizz_buzz()

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

# each row is its own list
# each column is an element in the row lists

def chessboard(rows, cols):
    # if first row -> start w/ O
    # else -> alternate row start w/ X and O
    # for num of cols -> alternate X and O ### 0 = 0 X = 1
    # if given el is X -> next return O 
    # if given el is O -> next return X 

    # √ rows argument -> create X (empty) lists to be elements in overall / nested in BOARD list 
    # √ if rows = 3 -> create 3 new (empty) lists 

    counter_col = 0
    counter_row = 0
    board = []
    board_rows = []
    # board_col_els = ''
    i = 0
    # create empty lists for number of rows and append to board list/array
    while counter_row < rows:
        board_rows.append([])
        counter_row += 1
    board.append(board_rows)
    # print(board_rows)
    while counter_col < cols - 1:
        if board_rows[i] == '':
            board_rows[i] = "O"
            i += 1
        else:
            board_rows[i] = "X"
            i += 1
        counter_col += 1
    # if board_rows[0] == '': #<- WORKING
    #     board_rows[0].append("O") #<- WORKING
    # else: #<- WORKING
    #     board_rows[0].append("X") #<- WORKING
    print(board)

    # for el in board: # of which there are 3 rn
    #     while counter_col < cols:
    #         #     board_rows[i].append("O")
    #         #     counter_col += 1
    #         #     i += 1
    #         if board[i] == []:
    #             board[board_rows[i]].append("O")
    #         else:
    #             board[board_rows[i]].append("X")
    #         i += 1
    #         counter_col += 1
    # print(board)


    # put this in a for loop; iterate through board_rows array/list



chessboard(3,4)
#-----------------------------------------------
