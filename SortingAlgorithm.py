def bubbleSort(array):
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if(array[j] > array[j+1]):
				array[j], array[j+1] = array[j+1], array[j] 


y = [5,4,3,2,1]
bubbleSort(y)
print(y)
