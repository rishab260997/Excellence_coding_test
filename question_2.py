def MaxConsecutive(arr, n):

    # intitialize count
    count = 0

    # initialize max
    result = 0

    for i in range(0, n):

        # Reset count when 0 is found
        if (arr[i] == 0):
            count = 0

        # If 1 is found, increment count
        else:

            # increase count
            count+= 1
            result = max(result, count)

    return result
