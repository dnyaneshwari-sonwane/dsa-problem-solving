def longest_unique(s):
    window = set()
    start = 0
    answer = 0

    for end in range(len(s)):
        while s[end] in window:
            window.remove(s[start])
            start += 1

        window.add(s[end])

        if end - start + 1 > answer:
            answer = end - start + 1

    return answer


text = "abcabcbb"

print("String:", text)
print("Answer:", longest_unique(text))
