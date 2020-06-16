from algorithms import bubble_sort
from algorithms import selection_sort


x=[5,6,4,3,7,8,9,0,1,2]
print("Import 1 for bubble sort algorithms")
print("Import 2 for selection sort algorithms")
n=int(input("Which algorithms you want to use:"))

if n==1:
    bubble_sort(x)
if n==2:
    selection_sort(x)

print(x)  




