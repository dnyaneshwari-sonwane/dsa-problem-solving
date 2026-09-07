def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):

        # If character is already in the current window
        if char in seen and seen[char] >= left:
            left = seen[char] + 1

        # Store the latest index of the character
        seen[char] = right

        # Calculate current window length
        current_length = right - left + 1

        # Update maximum length
        max_length = max(max_length, current_length)

    return max_length


# Example
s = "abcabcbb"

result = length_of_longest_substring(s)

print("Input:", s)
print("Longest substring length:", result)
