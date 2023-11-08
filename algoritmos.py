def bubbleSort(array):
  i = 0;
  comp = 0;
  for i in range(0, len(array) - i, 1):
    for ii in range(0, len(array) - (i + 1), 1):
      if (array[ii] > array[ii + 1]):
        swap = array[ii]
        array[ii] = array[ii + 1]
        array[ii + 1] = swap
        comp = comp + 1
  return array, comp

def quickSort(array):
    comp = 0;
    stack = [(0, len(array) - 1)] 
    while stack:
        low, high = stack.pop()  

        if low >= high:
            continue  

        pivot = array[low]  
        left = low + 1 
        right = high

        while True:          
            while left <= right and array[left] <= pivot:
                left += 1
            while right >= left and array[right] >= pivot:
                right -= 1
            if left > right:
                break 
    
            array[left], array[right] = array[right], array[left]
            comp = comp + 1
 
        array[low], array[right] = array[right], array[low]
        comp = comp + 1

        stack.append((low, right - 1))
        stack.append((right + 1, high))
    return array, comp

def insertionSort(arry) : 
  cmp = 0
  for i in range(1, len(arry)):
    key = arry[i]
    j = i - 1
    while j >= 0 and (arry[j] > key):
      arry[j + 1] = arry[j]
      j -= 1
      cmp += 1
    arry[j + 1] = key
  return arry, cmp

def selectionSort(array):
  comp = 0
  for i in range(len(array)):
    menor = i

    for j in range(i + 1, len(array)):
      comp = comp + 1
      if array[j] < array[menor]:
        menor = j

    if array[i] != array[menor]:
      aux = array[i]
      array[i] = array[menor]
      array[menor] = aux
  return array,comp
# falta o merge

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        swaps = mergeSort(left)[1]  
        swaps += mergeSort(right)[1]  
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                swaps += len(left) - i  
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        
        return arr,swaps
    
    return arr,0

def heapify(arr, n, i): 
  comp = 0
  largest = i  # Initialize largest as root
  l = 2 * i + 1  # left = 2*i + 1
  r = 2 * i + 2  # right = 2*i + 2

  # See if left child of root exists and is
  # greater than root

  if l < n and arr[i] < arr[l]:
    largest = l

# See if right child of root exists and is
# greater than root

  if r < n and arr[largest] < arr[r]:
    largest = r

# Change root, if needed

  if largest != i:
    (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
    comp = comp + 1

    # Heapify the root.

    heapify(arr, n, largest)

  return comp
# The main function to sort an array of given size

def heapSort(arr):
  comp = 0
  n = len(arr)

  # Build a maxheap.
  # Since last parent will be at ((n//2)-1) we can start at that location.

  for i in range(n // 2 - 1, -1, -1):
    comp = comp + heapify(arr, n, i)

# One by one extract elements

  for i in range(n - 1, 0, -1):
    (arr[i], arr[0]) = (arr[0], arr[i])  # swap
    comp = comp + 1
    comp = comp + heapify(arr, i, 0)

  return arr, comp
  
def shellSort(nums):
    comp = 0
    h = 1
    n = len(nums)
    while h > 0:
            for i in range(h, n):
                c = nums[i]
                j = i
                while j >= h and c < nums[j - h]:
                    nums[j] = nums[j - h]
                    j = j - h
                    nums[j] = c
                    comp = comp + 1
            h = int(h / 2.2)
    return nums, comp

def getNextGap(gap):
  gap = (gap * 10)//13
  if gap < 1:
      return 1
  return gap
  
def combSort(arr):
  comp = 0
  n = len(arr)

  gap = n

  swapped = True

  while gap !=1 or swapped == 1:

    gap = getNextGap(gap)

    swapped = False

    for i in range(0, n-gap):
      if arr[i] > arr[i + gap]:
        arr[i], arr[i + gap]=arr[i + gap], arr[i]
        swapped = True
        comp = comp + 1
  return arr, comp