def findPrefixSum(array, length):
    if not array:
        return "Empty Array."

    prefixSum = []
    prefixSum.append(array[0])

    for i in range(1, length):
        prefixSum.append(prefixSum[i - 1] + array[i])

    return prefixSum


def findEquilibriumIndex(array, prefixSum, length):
    for i in range(1, length):
        if prefixSum[i - 1] == prefixSum[length - 1] - prefixSum[i]:
            return i

    return -1


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    length = len(array)
    prefixSum = findPrefixSum(array, length)
    print(findEquilibriumIndex(array, prefixSum, length))
