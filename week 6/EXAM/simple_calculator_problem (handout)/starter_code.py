
def simple_calculator(in1,in2,string1):
    if in1 == 0 and in2 == 0:
        return 0
    
    if string1 == "+":
        return  in1 + in2
    
    if string1 == "-":
        return  in1 - in2
    
    if string1 == "*":
        return  in1 * in2
    
    if string1 == "/":
        if in2 == 0:
            return "Error: Division by zero"
        return  in1 / in2
    
    if string1 == "%":
        return  in1 % in2
    
    if string1 == "**":
        return  in1 ** in2


int1= input().split(" ")
in1 = int(int1[0])
in2 = int(int1[1])
string1 = int1[2]
print(simple_calculator(in1,in2,string1))
