import numpy as np

print(someFormula(19))
#NameError: 'someFormula' is not defined

def someFormula(input):
	output = input ** 2 / 5 - 9
	# the following print statement will print 
	# the value of output each time the function is called
	print(output)
	output2 = output **3
	return [output, output2]

print(output)
#NameError: 'output' is not defined

test_output = someFormula(7.0)
print(test_output)

test_array = np.array(test_output)
print(test_array * 4)
