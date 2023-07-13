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
#-----------------------------------------------

def add_list(*nums):
    if not nums:
        return 0
    
    total = 0
    for num in nums:
            if not (isinstance(num, int) or isinstance(num, float)):
                 return "NaN"
            total += num
    return total
    

print(add_list(3,43,43,53))
print(add_list(3,42.54,24,54235,664))


# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

#-----------------------------------------------
# Solution Goes Here - >
#-----------------------------------------------

def remove_ends(string):
    if len(string) < 3:
          return ''
    new_string = string[1:-1]
    return new_string
     
print(remove_ends('abc'))


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
#-----------------------------------------------

def is_palindrome(string):
    space_to_remove = " "
    new_string = ""
    for char in string:
         if char != space_to_remove:
              new_string += char
    reversed_string = new_string[::-1]
    if reversed_string.lower() == new_string.lower():
         return True
    if reversed_string.lower() != new_string.lower():
         return False
    
print(is_palindrome('A nut for a jar of tuna'))
     

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
#-----------------------------------------------

def is_prime(num):
    int(num)
    if num <= 1:
         return 'Not Prime'
    if num == 2 or num == 3 or num == 5 or num == 7:
        return 'Prime'
    if num % 2 == 0:
        return 'Not Prime'
    if num % 3 == 0:
        return 'Not Prime'
    if num % 5 == 0:
        return 'Not Prime'
    if num % 7 == 0:
        return 'Not Prime'
    else:
        return 'Prime'
    
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(29))
print(is_prime(200))
print(is_prime(79))
print(is_prime(83))
    


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
#-----------------------------------------------

def calculate_total(list, homestate):
    high_shipping_cost_states = ['HI', 'AK', 'TX', 'FL']
    low_shipping_cost_states = ['AL', 'MS', 'NV', 'IL']
    sales_tax = 0.085
    item_total = 0
    cart_total = 0
    for item in list:
        item_price = item["price"]
        item_tax = item_price * sales_tax
        item_total = item_price + item_tax
        cart_total += item_total

    if homestate in high_shipping_cost_states:
        final_total = cart_total + 10
        rounded_total = round(final_total, 2)
        return f'${rounded_total}'
    elif homestate in low_shipping_cost_states:
        final_total = cart_total + 5
        rounded_total = round(final_total, 2)
        return f'${rounded_total}'
    else:
        final_total = cart_total
        rounded_total = round(final_total, 2)
        return f'${rounded_total}'

print(calculate_total(shopping_cart, 'HI'))


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
#-----------------------------------------------

def fizz_buzz_check(num):
    if not (isinstance(num, int)):
        return f"{num} is not a number."
    if num % 3 == 0 and num % 5 == 0:
        return print('FizzBuzz')
    elif num % 3 == 0:
        return print('Fizz')
    elif num % 5 == 0:
        return print('Buzz')
    else:
        return print('')

print(fizz_buzz_check(10))
print(fizz_buzz_check(30))
print(fizz_buzz_check(18))
print(fizz_buzz_check(22))
print(fizz_buzz_check('ham_sandwich'))

def fizz_buzz_loop():
    counter = 1

    while counter < 51:
        if counter % 3 == 0 and counter % 5 == 0:
            print('FizzBuzz')
        elif counter % 3 == 0:
            print('Fizz')
        elif counter % 5 == 0:
            print('Buzz')
        else:
            print(counter)
        counter += 1

# fizz_buzz_loop()



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
#-----------------------------------------------

def grid_generator(rows, columns):
    board = []

    for y in range(rows):
        row = []
        for x in range(0, columns):
            if (x + y) % 2 == 0:
                row.append('O')
            else:
                row.append('X')
        board.append(row)

    return board
        

print(grid_generator(4, 6))
print(grid_generator(3, 7))
