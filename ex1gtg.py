from numpy import *
import pandas as pd


def MyArcTan(x,N):
    
    
    answer = 0
    i = 0
    for i in range(N+1):
        if -1 <= x <= 1: 
            answer = answer + (((-1)**i)*(x**((2*i)+1)))/((2*i)+1)
        elif x > 1:
            answer = pi/2 - answer - (((-1)**i)*((1/x)**((2*i)+1)))/((2*i)+1)
        elif x < 1:
            answer = -pi/2 -answer - (((-1)**i)*((1/x)** ((2*i)+1)))/((2*i)+1)
    return answer

MyInput = 0
while MyInput != 'q':
    print('')   
    print('Option "a" is a series expansion of arctan')
    print('Option "b" is a table of values for arctan(x) between the values -2 <= x <= 2')
    print('Option "c" is a calculation of pi to 7 significant figures')
    print('Option "d" is a calculation of pi to 12 decimal places')
    print('')
    print('NOTE - The value for N will be the upper limit of summation for the arctan series expansion')
    print('') 
    MyInput = input ( 'Enter a choice, "a", "b", "c", "d" or "q" to quit: ')
    print('') 
    print('You entered the choice: ', MyInput)
    print('')
    if MyInput == 'a' :
        print ('You have chosen part (a)' )
        print('')
        Input_x = input('Enter a value for x ( floating point number ): ')
        print('')
        Input_N = input('Enter a value for N (positive integer): ') 
        print('')
        print('The answer is: ', MyArcTan(float(Input_x), int(Input_N)))

    elif MyInput == 'b':
        print ('You have chosen part (b)') 
        print('')
        Input_N = input('Choose a value for N: ')
        xvalues_list = []
        arcvalues_list = []
        arctanactual_valueslist = []
        for i in range (10):
            xvalues_list.append(-2+(4*i/10))
            arcvalues_list.append(MyArcTan((-2+(4*i/10)), int(Input_N)))
            arctanactual_valueslist.append(arctan(-2+(4*i/10)))
        dict = {'x-value': xvalues_list, 'Arctan(x-values)': arcvalues_list, 'Arctan actual value': arctanactual_valueslist} 
        df = pd.DataFrame(dict)
        print(df)
        
    elif MyInput == 'c':
        print ('You have chosen part (c)' )
        print ('')
        print('An evaluation of pi will be calculated to 7 significant figures using the fact arctan(1) = pi/4. The function MyArcTan() will be used with the N value being 1200000.')
        print('')
        #1200000 works
        pi_evaluation = 4*MyArcTan(1, 1200000)
        pi_eval_7sf = float('%.7g' % pi_evaluation)
        perdiff = ((pi-pi_evaluation)/pi)*100
        print('Evaluated pi: ', pi_eval_7sf)
        print('')
        print('The percentage difference between the evaluated pi and actual value of pi: ', perdiff, '%')
   
    elif MyInput == 'd':
        print('You have chosen part (d)')
        print('')
        print('An evaluation of pi will be calculated to 12 decimal places using the identity arctan(1/2) + arctan(1/5) + arctan(1/8) = pi/4. The function MyArcTan() will be used with the smallest N value which is correct to 12 decimal places being 18.')
        print('')
        pi_evaluation= 4*(MyArcTan(0.5, 18) + MyArcTan(0.2, 18) + MyArcTan(0.125, 18))
        perdiff = ((pi-pi_evaluation)/pi)*100
        pi_eval_12dp = round(pi_evaluation, 12)
        print('Evaluated pi: ', pi_eval_12dp)
        print('')
        print('The percentage difference between the evaluated pi and actual value of pi: ', perdiff, '%')
        
    elif MyInput != 'q':
        print('This is not a valid choice')
        print('You have chosen to finish - goodbye.')