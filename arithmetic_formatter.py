def arithmetic_arranger(problems, show_answers=False):
    
    # Checks that there aren't more than 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        # Making sure the operator and operands are valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        

    








    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
