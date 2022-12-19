def function(text):
  result = {"characters": 0, "numbers": 0}
  for ch in text:
    if ch.isdigit():
      result["numbers"] += 1
    elif ch.isalpha():
      result["characters"] += 1
  return result

result  = function(input("enter your text: "))
print(result)