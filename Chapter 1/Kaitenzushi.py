from typing import List
from collections import deque

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # If K is 0 or all dishes are unique, you can eat all dishes since there are no restrictions
    if K == 0 or len(set(D)) == N:
        return N  

    # Queue to keep track of the last K eaten dishes
    recent_dishes = deque()  
    # Set to store unique dish types in the recent K dishes
    eaten_dishes = set()  
    dishes_eaten = 0  

    # Iterate through each dish on the conveyor belt
    for dish in D:
        # Eat the dish only if it hasn't been eaten in the last K dishes
        if dish not in eaten_dishes:
            dishes_eaten += 1 
            recent_dishes.append(dish)  # Add the dish to recent history
            eaten_dishes.add(dish)  # Mark it as recently eaten

            # If the queue exceeds K, remove the oldest dish from tracking and unique dish set
            if len(recent_dishes) > K:
                removed_dish = recent_dishes.popleft()
                eaten_dishes.remove(removed_dish)

    # Return the total number of dishes eaten
    return dishes_eaten

print(getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 1))  # Expected output: 5

print(getMaximumEatenDishCount(7, [1, 2, 1, 2, 1, 2, 1], 2))  # Expected output: 2

print(getMaximumEatenDishCount(5, [10, 20, 30, 40, 50], 2))  # Expected output: 5
