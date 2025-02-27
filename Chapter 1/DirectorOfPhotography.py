def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Initialize a variable to hold the count of valid artistic photographs
    ans = 0

    # Iterate through each position in the string C (for the photographer 'P' or backdrop 'B')
    for p in range(N):
        # Early exit if the remaining space from p does not allow placing a photographer and actor
        # with a minimum distance of X
        if p + X >= N:
            break
        
        # If the current position doesn't contain 'P' or 'B', skip it (valid photographer or backdrop)
        if C[p] != "P" and C[p] != "B":
            continue

        # Iterate through possible positions for the actor 'A'
        # The actor must be between p + X and p + Y
        for q in range(min(N, p + X), min(N, p + Y + 1)):
            # Skip this position if it's not an 'A' (actor)
            if C[q] != "A":
                continue
            
            # Now, we iterate through possible positions for the backdrop 'B' or photographer 'P'
            # The backdrop (or photographer) must be within q + X to q + Y from the actor
            for r in range(min(N, q + X), min(N, q + Y + 1)):
                # We check if the photographer is at position p, and the backdrop is at position r
                # or the photographer is at position r, and the backdrop is at position p
                if (C[p] == "P" and C[r] == "B") or (C[p] == "B" and C[r] == "P"):
                    # If both the conditions are satisfied, it counts as a valid artistic photograph
                    ans += 1

    # Return the total count of valid artistic photographs
    return ans

print(getArtisticPhotographCount(5, "APABA", 1, 2))
print(getArtisticPhotographCount(8, ".PBAAP.B", 1, 3))
print(getArtisticPhotographCount(5, "APABA", 2, 3))
  
