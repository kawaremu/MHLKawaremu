def bubbleSort(array):
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if(array[j] > array[j+1]):
				array[j], array[j+1] = array[j+1], array[j] 

number_list = [5,4,3,2,1]
alphabet_list = ['k','z','w','a','b']
bubbleSort(number_list)
bubbleSort(alphabet_list)
print(number_list)
print(alphabet_list)
