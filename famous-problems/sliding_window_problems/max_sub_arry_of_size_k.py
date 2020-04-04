


def avg_sub_arrays(n, arr):

  
  sum_=sum(arr[0:n])
  avg = [sum_/n]
  for i in range(n, len(arr)):
    sum_ += arr[i] - arr[i-n]
    avg.append(sum_/n)
  return avg


av = avg_sub_arrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print(av)