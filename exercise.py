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
          print(f"* You have a syntax error: there is an unexpected {char} where there should be a {required_char}")
          return False

      else: # there's nothing to close
        print(f"* You have a syntax error: there is an unexpected {char} where there is nothing to close.")

        return False



  if len(open) > 0:
    required_char = openables[open[-1]]
    print("* You have a syntax error: the string ended without a closing {}".format(required_char))

  return not open

print(check_syntax("(this)[] is some text"))
print("*****\n")

print(check_syntax("(this)] is some text"))
print("*****\n")

print(check_syntax("[(this] is some text"))
print("*****\n")

print(check_syntax("[this][ is some text"))
print("*****\n")

print(check_syntax("[this] is some text"))
