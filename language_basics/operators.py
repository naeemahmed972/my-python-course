# # symbols like + , -, / , <, > 

# # print( 5 * 4)

# # Arithmatic Operators

# # Addition + 

# print(5 + 6)

# # Subtraction -

# print(6 - 5)

# # Multiply *

# print(5 * 6)

# # Division /
# print(20 / 4)

# # floating point division
# print(19/4)

# # Integer division //
# print(19 // 4)

# # Remainder Modulus operator % 
# print(19 % 4)

# # exponent operator **
# print(2 ** 4)








# Assignment Operators

# my_var = 5

# my_var = 4 + 5
















# x = 20

# x = x + 1

# print(x)

# x += 1    # x = x + 1

# print(x)












# x = 50

# x -= 5    # x = x - 5















# x *= 5     # x = x * 5

# x /= 5     # x = x / 5

# x **= 5    # x = x ** 5

# x //= 5    # x = x // 5

# x %=5      # x = x % 5















# Comparison Operators

#       ==      Equal to
#       !=      Not Equal to
#       >       Greater than
#       <       Lesser than
#       >=      Greater than or equal to
#       <=      Lesser than or equal to

# print(5 == 5)

# print(5 == 6)

# print(6 <= 6)











# Logical Operators

#       and         Logical AND
#       or          Logical OR
#       not         Logical NOT
















# TRUTH TABLE

#   P       Q       P and Q     P or Q      Not P
#   True    True    True        True        False
#   True    False   False       True
#   False   True    False       True        True
#   False   False   False       False




# print(True and True)

# print(False or False)

# print( not False)


# print(5>4 and 16<10)









# Logical Operators Short Circuiting

# print( 4 < 2 and 5 < 10)

# print( 4 == 4 or 5 < 3)

# print( course == Computer Science and cgpa > 3 )











# Bitwise Logical Operators

# perform bit by bit comparison operations between two numbers or expessions

# and evaluates to a new number

# Binary AND                &       bit is 1 if both bits are 1
# Binary OR                 |       bit is 1 if either bit is 1
# Binary XOR                ^       bit is 1 if both bits are opposite
# Binary Complement (NOT)   ~       Inverts all the bits










# Decimal 16 in binary is 0 0 0 1 0 0 0 0
# Decimal 25 in binary is 0 0 0 1 1 0 0 1
# print(16 & 25)        # 0 0 0 1 0 0 0 0 = 16

# Decimal 16 in binary is 0 0 0 1 0 0 0 0
# Decimal 25 in binary is 0 0 0 1 1 0 0 1
# print(16 | 25)        # 0 0 0 1 1 0 0 1 = 25

# Decimal 16 in binary is 0 0 0 1 0 0 0 0
# Decimal 25 in binary is 0 0 0 1 1 0 0 1
# print(16 ^ 25)        # 0 0 0 0 1 0 0 1 = 9

# Decimal 16 in binary is 0 0 0 1 0 0 0 0
# print(~16)            # 1 1 1 0 1 1 1 1 = -17










# Bitwise Shift Operators

# Binary Shift Left     <<      Number of bits to be moved to the left. 0's are inserted on the                                 right side binary places of the number. Number of bits to be                                    shifted are specified on the right side of the operator while                                   the number which is shifted is written on the left side. like                                   33 << 2

# Binary Shift Right    >>      Opposite to what Binary Shift Left Does. Like 33 >> 2













# Decimal 33 in binary is       0 0 1 0 0 0 0 1 = 33
# print(33 << 3)    #       0 0 1 0 0 0 0 1 0 0 = 132

# Decimal 60 in binary is       0 0 1 1 1 1 0 0 = 60
# print(60 >> 3)    #           0 0 0 0 1 1 1 1 = 15











# Operator Precedence

# print( 2 + 4 * 3 )

# print( (2 + 4) * 3 )














# Operator Precedence

#   Operators                   Name

#   ()                          Parentheses
#   **                          Exponent
#   +x, −x, ~x                  Unary plus, Unary minus, Bitwise NOT
#   *, /, //, %                 Multiplication, Division, Floor division, Modulus
#   +, −                        Addition, Subtraction
#   <<, >>                      Bitwise shift operators
#   &                           Bitwise AND
#   ^                           Bitwise XOR
#   |                           Bitwise OR
#   ==, !=, >, >=, <, <=        Comparisons
#   is, is not, in, not in      Identity, Membership operators
#   not                         Logical NOT
#   and                         Logical AND
#   or                          Logical OR