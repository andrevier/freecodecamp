def arithmetic_arranger(problems, print_results=False):
  '''
  Receive a list of strings (problems) representing
  arithmetic operations and return a print of the
  operations as follows:
  var = ["12 + 1", "23 + 48"]
    12     23
  +  1   + 48
  ----   ----
  If show = True, the function also print the result.
  '''
  # Errors excede the limit of problems
  if len(problems) > 5:
    return "Error: Too many problems."

  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""

  for i in range(len(problems)):
    # separate the string in two parcels (p1 and p2) and the operator (op).
    p1 = problems[i].split()[0]
    op = problems[i].split()[1]
    p2 = problems[i].split()[2]

    try:
      x1 = int(p1)
      x2 = int(p2)
    except ValueError:
      return "Error: Numbers must only contain digits."

    if (len(p1) > 4) or (len(p2) > 4):
      return "Error: Numbers cannot be more than four digits."
      
    if (op != "+") and (op != "-"):
      return "Error: Operator must be '+' or '-'."
    
    max_len = max(len(p1), len(p2))

    l1 = " "*(max_len - len(p1) + 2) + p1
    l2 = problems[i].split()[1] + " "*(max_len - len(p2) + 1) + p2
    l3 = (max_len + 2)*"-"
    line1 = line1 + l1 + " "*4
    line2 = line2 + l2 + " "*4
    line3 = line3 + l3 + " "*4

    if print_results == True:
      if op == '+':
        r = str(x1 + x2)
      elif op == '-':
        r = str(x1 - x2)
      else:
        r = 0
      line4 = line4 + (max_len + 2 - len(r))*" " + r + " "*4
  
  arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4  
  return arranged_problems
