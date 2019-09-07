## Saturday, Sep 7th
# 01 - Reinforcing Exercises

These short exercises will give you a chance to practice the fundamental programming concepts you've learned so far.
## Prerequisites

+ Programming fundamentals

## The code

Copy this code into a Python file, try running it, and then read the source code to see what it's doing.

~~~~
def check_syntax(str):
  openables = {
    "(": ")",
    "[": "]",
    "{": "}"
  }
  open = []
  opening_chars = openables.keys()
  closing_chars = openables.values()

  for char in list(str):

    if char in opening_chars: # opening bracket

      open.append(char)

    elif char in closing_chars: # closing bracket

      if open:
        required_char = openables[open[-1]]

        if char == required_char: # it's the right kind of closing bracket

          open.pop()

        else: # it's the wrong kind of closing bracket
          print("* You have a syntax error: there is an unexpected {}".format(char))
          return False

      else: # there's nothing to close
        print("* You have a syntax error: there is an unexpected {} where there is nothing to close.".format(char))

        return False

  if len(open) > 0:
    required_char = openables[open[-1]]
    print("* You have a syntax error: the string ended without a closing {}".format(required_char))

  return not open


print(check_syntax("(this)[] is some text"))
print("*****")
print(check_syntax("(this)] is some text"))
print("*****")
print(check_syntax("[(this] is some text"))
print("*****")
print(check_syntax("[this][ is some text"))
print("*****")
print(check_syntax("[this] is some text"))
~~~~

The output should currently look like this:

~~~~
True
*****
* You have a syntax error: there is an unexpected ] where there is nothing to close.
False
*****
* You have a syntax error: there is an unexpected ]
False
*****
* You have a syntax error: the string ended without a closing ]
False
*****
True
~~~~

## Exercise 1

Modify the code to improve the error messages it gives, specifying what character was missing. This should be your new output:

~~~~
print(check_syntax("(this)[] is some text"))
True
~~~~

~~~~
print(check_syntax("(this)] is some text"))
* You have a syntax error: there is an unexpected ] where there is nothing to close.
False
~~~~

New, improved error message:

~~~~
print(check_syntax("[(this] is some text"))
* You have a syntax error: there is an unexpected ] where there should be a )
False

print(check_syntax("[this][ is some text"))
* You have a syntax error: the string ended without a closing ]
False
~~~~

## Exercise 2

Modify the code to make it work for angled brackets (`<` and `>`) as well.

The new output for these strings containing angled brackets should look like this:

~~~~
print(check_syntax("<html> (this)[] is some text</html>"))
True
~~~~

~~~~
print(check_syntax("<html> (this)] is some text</html>"))
* You have a syntax error: there is an unexpected ] where there is nothing to close.
False
~~~~

~~~~
print(check_syntax("<html> [(this] is some text</html>"))
* You have a syntax error: there is an unexpected ] where there should be a )
False
~~~~

~~~~
print(check_syntax("<html> [this][ is some text</html>"))
* You have a syntax error: the string ended without a closing ]
False
~~~~

~~~~
print(check_syntax("<html> [this] is some text</html"))
* You have a syntax error: the string ended without a closing >
False
~~~~
