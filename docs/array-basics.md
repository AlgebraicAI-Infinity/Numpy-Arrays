# NUMPY CONCEPTS

## CREATION OF ARRAYS   

Create arrays :

```bash
array1 = np.array([1,2,3,4])
array2 = np.array([1,2],[3,4])
```

Special types of Arrays :
```bash
ones_array = np.ones((2,2))
zeroes_array = np.zeros((4,3)) 
identity_array =np.eye(2)
empty_array = np.empty((2,2))
```


Random Arrays :
```bash
random_array = np.random.random((3,2))
normal_array = np.random.normal(0,1,(2,3))          
random_integer_array = np.random.randint(0,10,(2,3))  
```

Some more sequence arrays :
```bash
spaced_array = np.linspace(0,1,4)   
range_array = np.arange(5)         
logspace_array = np.logspace(0,2,6)  


Check out the code below 👇 

[Numpy Array Code](https://github.com/AlgebraicAI-Infinity/Numpy-Arrays/blob/main/code/array-basic.py)