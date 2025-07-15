#You are given an array and you need to find number of tripets of indices (i, j, k) such that the elements at those indices are in geometric progression for a given common ratio r and i<j<k.


def countTripletsR1(arr):
    from collections import Counter
    freq = Counter(arr)
    total = 0
    for count in freq.values():
        if count >= 3:
            total += count * (count-1) * (count-2)//6
    return total

# Complete the countTriplets function below.
def countTriplets(arr, r):
    tripets = 0
    if r == 1:
        return countTripletsR1(arr)
    from collections import defaultdict
    left = defaultdict(int)
    right = defaultdict(int)
    for num in arr:
        right[num] += 1
    for num in arr:
        right[num] -= 1
        if num%r == 0:
            first = num//r
            third = num*r
            tripets += left[first]*right[third]
        left[num] += 1
    return tripets
        
    return tripets


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
