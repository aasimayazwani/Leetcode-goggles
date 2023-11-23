class Solution:

    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        ret = []  # list for storing the count of distinct numbers
        store = {}  # Hash table - for storing the numbers frequency for a particular sub array

        # Traversing the 1st sub array from num[0:k]
        for i in range(k):
            # Storing the frequency in hash table
            if store.get(nums[i], None):
                store[nums[i]] += 1
            else:
                store[nums[i]] = 1

        # getting the number of distinct keys form hash map
        a = len(store.keys())
        ret.append(a)  # saving the number to return list

        # Traversing nums for further sub arrays
        for i in range(k, len(nums)):
            # decreasing the count for number (i-k) as it does not belong to the current sub array
            store[nums[i - k]] -= 1
            # checking if it's count became 0
            if store[nums[i - k]] <= 0:
                # deleting the key if it has count <= 0
                del store[nums[i - k]]

            # adding the latest number to the hash table
            if store.get(nums[i], None):
                # increasing it's count if it already exists
                store[nums[i]] += 1
            else:
                store[nums[i]] = 1

            # getting the number of distinct keys form hash map
            a = len(store.keys())
            ret.append(a)  # saving the number to return list

        # returning the created list
        return ret