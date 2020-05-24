# python3
import sys


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """
  result = []
  # Implement this function yourself
  #print(sort_characters(text))
  order = sort_characters(text) 
  #print(order)
  classes = compute_char_classes(text,order)
  # sort_dbl = sort_doubled(text,2,order,clss)
  # print(sort_dbl)
  L = 1
  while L < len(text):
    order = sort_doubled(text,L,order,classes)
    classes = update_classes(order,classes,L)
    L = 2*L

  return order


def sort_characters(arr): 
  
    output = [0 for i in range(256)] 
    count = [0 for i in range(256)] 
    order = [0] * len(arr)
    ans = ["" for _ in arr] 
  
    for i in arr: 
        count[ord(i)] += 1

    for i in range(256): 
        count[i] += count[i-1] 
  
    # Build the output character array 
    for i in range(len(arr)-1,-1,-1):         
        count[ord(arr[i])] -= 1
        order[count[ord(arr[i])]] = i
  
    return order  



def compute_char_classes(arr, order):

  classes = [0] * len(arr)
  classes[order[0]] = 0
  for i in range(1,len(arr)):
    if arr[order[i]] != arr[order[i-1]]:
      classes[order[i]] = classes[order[i-1]] + 1
    else:
      classes[order[i]] = classes[order[i-1]]

  return classes



def sort_doubled(arr,L,order,classes):
  count = [0] * len(arr)
  new_order = [0] * len(arr)
  for i in range(len(arr)):
    count[classes[i]] = count[classes[i]] + 1
  for j in range(1,len(arr)):
    count[j] += count[j-1]
  for i in range(len(arr)-1,-1,-1):
    start = (order[i] - L + len(arr)) % len(arr)
    cl = classes[start]
    count[cl] -= 1
    new_order[count[cl]] = start

  return new_order

def update_classes(new_order,classes,L):
  n = len(new_order)
  new_classes = [0] * n
  new_classes[new_order[0]] = 0
  for i in range(1,n):
    cur = new_order[i]
    prev = new_order[i-1]
    mid = cur + L
    mid_prev = (prev + L) % n
    if classes[cur] != classes[prev] or classes[mid] != classes[mid_prev]:
      new_classes[cur] = new_classes[prev] + 1
    else:
      new_classes[cur] = new_classes[prev]
  return new_classes



if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
