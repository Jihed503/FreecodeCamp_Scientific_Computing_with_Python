def arithmetic_arranger(problems, display=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    if any('-' not in i and '+' not in i for i in problems):
        return "Error: Operator must be '+' or '-'."
    
    arranged_problems = ''
    for i in problems:
        if '-' in i:
            p = i.index('-')
            if not i[:p-1].isdigit() or not i[p+2:].isdigit():
                return "Error: Numbers must only contain digits."
            elif len(i[:p-1]) > 4 or len(i[p+2:]) > 4 :
                return "Error: Numbers cannot be more than four digits."
            else:
                width = max(len(i[:p-1]),len(i[p+2:]))+2
                arranged_problems += i[:p-1].rjust(width)+'    '
                
        else:
            p = i.index('+')
            if not i[:p-1].isdigit() or not i[p+2:].isdigit():
                return "Error: Numbers must only contain digits."
            elif len(i[:p-1]) > 4 or len(i[p+2:]) > 4 :
                return "Error: Numbers cannot be more than four digits."
            else:
                width = max(len(i[:p-1]),len(i[p+2:]))+2
                arranged_problems += i[:p-1].rjust(width)+'    '
    #arranged_problems.strip()
    arranged_problems = arranged_problems[:-4]
    arranged_problems += '\n'

    for i in problems:
        if '-' in i:
            p = i.index('-')
            width = max(len(i[:p-1]),len(i[p+2:]))+2
            arranged_problems += '-' + i[p+2:].rjust(width-1) + '    '
        else:
            p = i.index('+')
            width = max(len(i[:p-1]),len(i[p+2:]))+2
            arranged_problems += '+' + i[p+2:].rjust(width-1) + '    '
    #arranged_problems.strip()
    arranged_problems = arranged_problems[:-4]
    arranged_problems += '\n'

    for i in problems:
        if '-' in i:
            p = i.index('-')
            width = max(len(i[:p-1]),len(i[p+2:]))+2
            arranged_problems += '-'*width + '    '
        else:
            p = i.index('+')
            width = max(len(i[:p-1]),len(i[p+2:]))+2
            arranged_problems += '-'*width + '    '
    #arranged_problems.strip()
    arranged_problems = arranged_problems[:-4]
    

    if display == True:
        arranged_problems += '\n'
        for i in problems:
            if '-' in i:
                p = i.index('-')
                width = max(len(i[:p-1]),len(i[p+2:]))+2
                arranged_problems += str(int(i[:p-1])-int(i[p+2:])).rjust(width) + '    '
            else:
                p = i.index('+')
                width = max(len(i[:p-1]),len(i[p+2:]))+2
                arranged_problems += str(int(i[:p-1])+int(i[p+2:])).rjust(width) + '    '
            
        #arranged_problems.strip()
        arranged_problems = arranged_problems[:-4]
    
    return arranged_problems
