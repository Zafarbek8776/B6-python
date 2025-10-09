def process_list(nums):
    def compute_sum():
        return sum(nums)  

    total = compute_sum()  
    length = len(nums)     

    return length, total   

numbers = [3, 7, 1, 8, 2]
length, total = process_list(numbers)

print("List length:", length)
print("List sum:", total)
