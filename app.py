import sys

number_list = sys.argv[1:]

def number_sum(no_list):
    if len(no_list)!=3:
        return "Exactly 3 numbers are required"
    else:
        sum = 0
        for i in no_list:
            try:
                i = int(i)
                if i==15 or i==16:
                    sum += int(i)
                elif i>=13 and i<=19:
                    pass
                else:
                    sum += int(i)

            except ValueError as e:
                return "All inputs must be numeric"
                
        return sum


print(number_sum(number_list))