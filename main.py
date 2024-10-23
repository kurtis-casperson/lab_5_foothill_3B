# Challenge 1

# Recursive Lines

# Write a recursive function that accepts an integer argument n. 
# The function should display n lines of asterisks on the screen, 
# with the first line showing 1 asterisk, the second line showing 2 asterisks, 
# up to the n-th line which shows n asterisks.
 

def test(astrik, num):
      if len(astrik) >= num:
          return astrik
      else:
       astrik += "*"
       print(astrik)
       return test(astrik, num)


result = test("", 5)



