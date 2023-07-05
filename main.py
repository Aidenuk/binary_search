
# this approach uses while loop leading to N(logN) time complexity.
def bin_search(array,start,end,target):
  while start <= end:
    
    mid = start + end // 2
    if target == arr[mid]:
      
      return mid
    elif arr[mid] < target:
      start = mid + 1
    else:
      end = mid -1
  return None
  

# this approach uses recursive by using stack.

def recur_search(array,start,end,target):
  while start <= end:
    mid = (start+end) //2
    if target == array[mid]:
      return mid
    elif array[mid] < target:
      start = recur_search(array,mid+1,end,target)
    else:
      end = recur_search(array,start,mid-1,target)


n,target = list(map(int,input().split()))

arr = list(map(int,input().split()))


result = recur_search(arr,0,n-1,target)

if result == None:
  print("the value does not exit")
else:
  print(result+1)


# However, we need to make sure the give array is already sorted otherwise, it is not efficient to use binary search. 