def binSe3(kumpulan,target):
    low = 0
    high = len(kumpulan) -1
    list = []
    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            list.append(mid)
            i = mid + 1
            while kumpulan[i] == target:
                list.append(i)
                i += 1
            i = mid - 1
            while kumpulan[i] == target:
                list.append(i)
                i -= 1
            return list
        elif target < kumpulan[mid]:
            high = mid -1
        else:
            low = mid +1
    return False