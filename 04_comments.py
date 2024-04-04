# subject of this python script:
# Authored by: Laiba Ahmed
# Where to contact: github profile or email address

# Qs-1:  Why to use single quotation? 
print('Laiba') # when we are writing a string

# Qs-2:  Why to use double quotation? 
print("Laiba") 
print("What's Up")# when we are writing a strings and making use of other quotation marks.

# Qs-3:  When to use triple quotation? 
print('''Laiba''') 
print('''What's Up''')# when we are writing multiple line strings and also using """ or '''quotation marks inside.

# When to use comments in python, mention 10 study cases.
"""
Study Case 1: If you want to explain your code to someone else who is reading
your program for the first time.

Study Case 2: You can write long sentences that span multiple lines if needed.
This helps make your code more readable.

Study Case 3: Commenting out sections of code allows you to temporarily disable certain
parts of your program without deleting them entirely. This can be useful while debugging.

Study Case 4: Python has built-in functions like help() and docstring which
can display documentation about modules, classes, methods, and functions.
You can add these within triple quotes so they get displayed whenever those elements
are accessed.

"""
# Study case 5: Use comments to indicate where a particular section of code starts and ends
#              (e.g., "Start of user input loop", "End of user input loop

# Study Case 6: Write comments at the beginning of each function/method to describe what
#              it does, its parameters, return type etc.
def greet(name):
    """
    This function takes one parameter 'name', prints a welcome message along with name
    and returns None.
    """
    print(f"Hello {name}, Welcome!")
    # Call the above defined function
    greet("John Doe")

# Study Case 7: Add comments inside conditional statements or loops to explain 
# why a specific condition or action was taken
if True:   # A sample boolean value
        print("The statement inside if block will execute.")
else:      # The else block will only execute if the if block doesn't execute
        print("The statement inside else block will execute.")
# Study Case 8: Make a to-do list by adding comments next to tasks that
        # need to be done later
        # TODO: Implement feature X
        #       Fix bug Y
        #       Optimize performance</s>

# Study Case 9:  Providing Attribution or References
  # If you adapt code from external sources or libraries,
  # include comments with attribution or references.
'''
   example:
   Code adapted from the official Python documentation
   import math
   pi = math.pi
   radius = 10
   area = math.pi * radius**2
   
'''      
# Study Case 10:  Code Review Suggestions:
# Use comments to provide feedback or suggestions during 
# code reviews for collaborators.
'''
 example:
 Code review suggestion: Consider using a more efficient algorithm here.
  
'''               
        
