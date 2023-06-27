
#https://replit.com/@CodeSumner/boilerplate-arithmetic-formatter#arithmetic_arranger.py
import operator
"""
Strategy: pase each problem in arithmetic problems list to create first operands list, second openrands list
        and openrators list, add each element and a appropriate space as string of each list for three lines,
        calculate the arithmetic problems and add the result as fourth line, connect all four lines as big 
        string, assign it to arranged_problems.
"""

def arithmetic_arranger(problems):
   
    i = 0 # record the number of times of Errors.
    Error_No = 0 # mark what kind of Error is.
    problem_elem = [] # element list of each problem in arithmetic problems.
    first_operands = [] # list for first operand of each problem 
    second_operands = [] # list for second operand of each problem 
    operators = []  # list for operators of each problem 
    
   
    # set string variables
    arranged_problems = ""
    gap = "  " # it's the space of each problem's rightside and leftside.
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    dashs = ""
    gap_under_dashs = ""
    gap1 = "" #
    gap2 = ""

   
    # check if the supplied problems are properly formatted, or return Error.
    for problem in problems:
        # pase each problem to create three lists.
        problem_elem = list(problem.split(' '))
        first_operands.append(problem_elem[0])
        second_operands.append(problem_elem[2])
        operators.append(problem_elem[1])
        # mark what kind of problem is and record the number of Errors.
        if problem_elem[0].isnumeric() == False or problem_elem[2].isnumeric() == False:
            i += 1 
            Error_No = 1
        if problem_elem[1] != '+' and problem_elem[1] != '-':
            i += 1
            Error_No = 2
        if len(problem_elem[0]) > 4 or len(problem_elem[2]) > 4:
            i += 1
            Error_No = 3  
    # if there is Error, return.      
    if i >= 5:
        return "Error: Too many problems."
    if Error_No == 1:
        return "Error: Numbers must only contain digits."
    if Error_No == 2:
        return "Error: Operator must be '+' or '-'."
    if Error_No == 3:
        return "Error: Numbers cannot be more than four digits."
    

    # dictionnary for converting string to math operator.
    ops = { "+": operator.add, "-": operator.sub }     
    # creat arranged_problems list.
    for j in range(len(first_operands)):
                
        max_operand = max(first_operands[j], second_operands[j])   
        # the length of dashs is depending on length of max operand for each problem.            
        for k in range(len(max_operand) + 2):
            dashs += "-"
        third_line += (gap + dashs + gap )
        # the space next to first operand' leftside is gap1.
        for g in range(len(dashs) - len(str(first_operands[j]))):
            gap1 += " "
        first_line += (gap + gap1 + str(first_operands[j])+ gap)
        # the space between operator and second operand is gap2.
        for e in range(len(dashs) - len(str(second_operands[j])) - 1):
            gap2 += " "
        second_line += (gap + str(operators[j]) + gap2 + str(second_operands[j])+ gap)
        # the space next to result is gap under dashs.        
        result = ops[operators[j]](int(first_operands[j]), int(second_operands[j]))   
        for h in range(len(dashs) - len(str(result))):
            gap_under_dashs += " "
        fourth_line += (gap + gap_under_dashs + str(result) + gap)
        # reset the variable to null for next loop.
        dashs = ""
        gap1 = ""
        gap2 = ""
        gap_under_dashs = ""
    # add four lines as arranged problems.
    arranged_problems = (first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line)
    
    return arranged_problems



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

