from typing import List
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # If no diners are already seated (M = 0), we can place diners in every (K+1)th position
    if M == 0:
        return N // K

    # Sort the list of already seated diners to easily calculate the gaps between them
    S.sort()
    additional_people = 0

    # Calculate the number of additional diners that can fit before the first seated diner
    # The first gap is between the first position (1) and the first seated diner (S[0])
    left_gap = S[0] - 1
    additional_people += left_gap // (K + 1)  # This divides the gap into parts of (K+1) cells

    # Loop through each pair of seated diners to calculate the gaps between them
    for i in range(M - 1):
        # `left` is the current seated diner, `right` is the next seated diner
        left = S[i]
        right = S[i + 1]
        
        # Calculate the gap between the current seated diner and the next
        gap = right - left - 1  # Subtract 1 to exclude the two seated diners themselves
        
        # If the gap is larger than the minimum distance required (K), we can add more diners
        if gap > K:
            # The number of diners we can fit in this gap is the available space (gap - K) divided by (K + 1)
            additional_people += (gap - K) // (K + 1)

    # Calculate the number of additional diners that can fit after the last seated diner
    # The last gap is between the last seated diner (S[-1]) and the end of the cafeteria (N)
    right_gap = N - S[-1]
    additional_people += right_gap // (K + 1)  # Again, we divide by (K + 1) to fit diners in the gap

    # Return the total number of additional diners we can seat
    return additional_people


print(getMaxAdditionalDinersCount(10, 1, 2, [2, 6]))  
print(getMaxAdditionalDinersCount(15, 2, 3, [11,6,14]))

