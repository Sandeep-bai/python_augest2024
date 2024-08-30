import numpy as np
arrat1 =np.full((4,3),45)

print(arrat1)
print(arrat1[1][2])
print(arrat1[3][2])


# import numpy as np
# arrat1 =np.zeros((4,3))

# print(arrat1)
# print(arrat1[1][2])
# print(arrat1[3][2])



import numpy as np

array1 = np.arange(1,14)

array12 = np.arange(1,20,2)

martric1 = np.array([[2,3],[3,4]])

martric2 = np.array([[4,5],[7,8]])

print(array1)
print(array12)


print("matrix 1 \n",martric1)
print("matrix 2\n",martric2)


product = np.dot(martric1,martric2)


print("The product of two matrix is ", product)




sum1 = martric1 * martric2

print("sum is \n", sum1)




array1 = np.array([2,3,4,55,66,55])



array2 = array1.reshape(2,3)



print("result",array2)





array1 = np.array([2,3,4,55,66,55])



mean_value = np.mean(array1)

median_value = np.median(array1)

std_deviation = np.std(array1)


print("mean",mean_value)

print("median value is :",median_value)

print("standard deviation is :",std_deviation)





array1 = np.arange(2,12)

print('array',array1)

array2 = np.zeros((2,3))
print('array',array2)

array3 = np.ones((2,3))
print('array',array3)

array4 = np.full((2,3),67)
print('array',array4)




array1 = np.array([2,3,3,33,3,3,3])

print('array',array1)

root= np.sqrt(array1)
print('array',root)

array3 = np.ones((2,3))
print('array',array3)

exp = np.exp(array1)
print('array',exp)




vector = np.arange(50)

print("vector is ",vector)
print("vector shape ",vector.shape)

array3 = np.ones([3,2])
print('array',array3)
print('array shape',array3.shape)

exp = np.zeros([2,3,4])
print('tensor',exp)
print('tensor',exp.shape)

arr1 = np.arange(12)

arr2 = arr1.reshape(2,6)
arr3 = arr1.reshape(6,2)
arr4 = arr1.reshape(3,4)
arr5 = arr1.reshape(12,1)



print('array1',arr1)

print('array1',arr2)

print('array1',arr3)

print('array1',arr4)

print('array1',arr5)




arr1 = np.arange(1,10).reshape(3,-1)

print(arr1)

arr2 = np.array([2,5,7])


print("result",arr2)

mat1 = np.array([[4,6,8],[12,16,20]])

print(mat1)

rel = mat1 + arr2 

print("result",rel)




arr1 = np.arange(1,10)
arr1 = np.arange(2,25,2)

arr2 = arr1.reshape(3,-1)
arr3 = arr1.reshape(4,-1)
arr4 = arr1.reshape(2,-1)
arr5 = arr1.reshape(3,-1)



print('array1',arr1)

print('array1',arr2)

print('array1',arr3)

print('array1',arr1)

print('array1',arr1)








data1= np.array([1,2,3,4,5])
data2 = np.array([6,7,8,9,10])


data = np.stack((data1,data2),axis=0)

print("data",data)