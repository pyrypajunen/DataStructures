def selection_sort(nums):

    for i in range(len(nums)-1):

        index = i

        # this is a linear search - O(N)
        for j in range(i, len(nums)):
            if nums[index] < nums[j]:
                index = j

        if index != i:
            nums[index], nums[i] = nums[i], nums[index]


if __name__ == '__main__':

    n = [45, 100, 0, 1, -5, -10, 4, 5, 6, 13]
    selection_sort(n)
    print(n)
