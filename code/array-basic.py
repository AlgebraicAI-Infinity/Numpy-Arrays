import numpy as np

"""creating basic arrays"""

array1 = np.array([1,2,3,4])
array2 = np.array([[1,2],[3,4]])


"""Some special types of arrays """

ones_array = np.ones((2,2))
zeroes_array = np.zeros((4,3)) # Here 4 is row and 3 is column
identity_array =np.eye(2)
empty_array = np.empty((2,2))

"""random array"""

random_array = np.random.random((3,2))
normal_array = np.random.normal(0,1,(2,3))           # this is for gaussian distribution
random_integer_array = np.random.randint(0,10,(2,3)) # Here 0 is lower bound and 10 is upper bound

"""Some more sequence arrays"""

spaced_array = np.linspace(0,1,4)   # It creates array 0f 4 evenly space numbers between 0 and 1
range_array = np.arange(5)          # Here is 5 upper bound which is exclusive
logspace_array = np.logspace(0,2,6) # It creates a numpy array of 6 numbers spaced logarithimically between 10^0 and 10^2



if __name__=="__main__":
    print(f'Array 1 is : {array1}')
    print(f'Array 2 is : {array2}')
    print(f'ones array is : {ones_array}')
    print(f'zeros array is : {zeroes_array}')
    print(f'identity array is :{identity_array}')
    print(f'empty array is: {empty_array}')
    print(f'Random array is : {random_array}')
    print(f'Normal array is : {normal_array}')
    print(f'Random integer array is : {random_integer_array}')
    print(f'Range array is : {range_array}')
    print(f'spaced array is :{spaced_array} ')
    print(f'Log space array is : {logspace_array}')