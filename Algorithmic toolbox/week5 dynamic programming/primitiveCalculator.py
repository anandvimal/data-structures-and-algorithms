
min_num_of_calculations={}
def primitiveCalculator(goal):
    goal = int(goal)
    calculations = ['-1','/2','/3']
    min_num_of_calculations['0']=0
    min_num_of_calculations['1']=0
    for m in range(1,goal+1):
        min_num_of_calculations[str(m)]=100 #infinite value of steps
        for cal in calculations:
            step_calculation = eval(str(m)+str(cal))
            if (type(step_calculation)==float and step_calculation.is_integer()) or type(step_calculation)==int:
                step_calculation = int(step_calculation)
                #print(f"step_calculation:{step_calculation},  m:{m}")
                if m >= step_calculation:
                    num_of_steps = min_num_of_calculations[str(step_calculation)]+1
                    #print(num_of_steps)
                    if num_of_steps < min_num_of_calculations[str(m)]:
                        min_num_of_calculations[str(m)] = num_of_steps
    #print(min_num_of_calculations)
    return min_num_of_calculations[str(goal)]-1

#print(primitiveCalculator(10))

if __name__ == "__main__":
    goal = int(input()) #ignore
    number_of_steps =primitiveCalculator(goal=goal)
    print(number_of_steps)


