def arithmetic_arranger(problems, solve=False):
    digerror=False
    sigerror = False
    operror = False
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
    else:
        ind=0
        firstnum = []
        ops = []
        secondnum = []
        results = []
        dashes = []
        for problem in problems:
            parts = problem.split()
            size = int(len(max(parts[0],parts[2],key=len)))
            for part in parts:
                if len(part) > 4:
                    arranged_problems = "Error: Numbers cannot be more than four digits."
                    digerror = True

            if not parts[0].isdigit() or not parts[2].isdigit():
                arranged_problems="Error: Numbers must only contain digits."
                sigerror = True
            if parts[1] != "+" and parts[1] != "-":
                arranged_problems="Error: Operator must be '+' or '-'."
                operror = True
            if parts[1] == "+" and sigerror == False:
                result = int(parts[0]) + int(parts[2])
                results.append(str(result).rjust(size+2))
            if parts[1] == "-" and sigerror == False:
                result = int(parts[0]) - int(parts[2])
                results.append(str(result).rjust(size+2))

            firstnum.append(str(parts[0].rjust(size+2)))
            secondnum.append(str(parts[1].ljust(2)+parts[2].rjust(size)))
            dashes.append(str(("-"*(size+2)).rjust(size)))
            ind += 1

        line1 = f"""{"    ".join(firstnum)}"""
        line2 = f"""{"    ".join(secondnum)}"""
        line3 = f"""{"    ".join(dashes)}"""
        line4 = f"""{"    ".join(results)}"""
        if digerror == True:
            arranged_problems = "Error: Numbers cannot be more than four digits."
        elif sigerror == True:
            arranged_problems="Error: Numbers must only contain digits."
        elif operror == True:
            arranged_problems="Error: Operator must be '+' or '-'."
        elif solve == True : arranged_problems = line1 + f"\n" + line2 + f"\n" + line3 + f"\n" + line4
        else: arranged_problems = line1 + f"\n" + line2 + f"\n" + line3  
    return arranged_problems