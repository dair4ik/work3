# Task 5
def string_permutations(s, step=0):
    if step == len(s):
        print("".join(s))
    for i in range(step, len(s)):
        s_copy = [c for c in s]
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
        string_permutations(s_copy, step + 1)
