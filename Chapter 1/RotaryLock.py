from typing import List  # Importing List type for type hinting

# Function to calculate the minimum time to enter a code
def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Initialize the current position as 1 (starting point)
    current = 1
    
    # Initialize total_time to accumulate the time taken to move between numbers
    total_time = 0
    
    # Iterate over each number in the list C (which represents the code to be entered)
    for num in C:
        # Calculate the absolute difference between the current position and the target number
        diff = abs(num - current)
        
        # Check if the difference is greater than half the total number of positions (N//2)
        # If yes, it's quicker to go the other way around the circle
        if diff > N // 2:
            total_time += N - diff  # Time to go the longer way
        else:
            total_time += diff  # Time to go the direct way
        
        # Update the current position to the number just entered
        current = num
    
    # Return the total time accumulated
    return total_time


print(getMinCodeEntryTime(5, 3, [2, 4, 1]))             #Expected Output: 5
print(getMinCodeEntryTime(6, 4, [1, 3, 5, 6]))          #Expected Output: 5
print(getMinCodeEntryTime(8, 5, [8, 1, 3, 7, 5]))       #Expected Output: 10
