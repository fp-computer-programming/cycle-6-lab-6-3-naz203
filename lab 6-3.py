"""
Create a Python file named lab_6-3

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a list of 4 colors and store it as a variable.
Use a method to add 3 more colors to the list in a single statement.
Use a different method to add one additional color to the list.
Use a method to insert a new color at index 3.
Use a method to create a copy of the list
Use a method to remove one element from the copy of the list.

"""
# author : nazeer thompson

# list of 4 colors and store it as a variable
colors =["red","blue","green","yellow"]

# method to add 3 more colors to list in a single statement.
colors.extend(["orange","purple","pink"])

# different method to add one additional color to the list
colors.insert("brown")

# method to insert a new colors at index 3.
colors.insert(3,"violet")

# copy of the list.
colors_copy = colors.copy()

# method to remove one element from the copy of the list.
colors_copy.pop(2)  #removes the element at index 2, which is "green"