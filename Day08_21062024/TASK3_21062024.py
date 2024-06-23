def reverse_string_slicing(s):
    return s[::-1]

s = "Surya"
reversed_s = reverse_string_slicing(s)
print(reversed_s)

def reverse_string_list(s):
    s_list = list(s)
    s_list.reverse()
    return ''.join(s_list)

s = "Atomic"
reversed_s = reverse_string_list(s)
print(reversed_s)


def reverse_string_loop(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

s = "Stuart"
reversed_s = reverse_string_loop(s)
print(reversed_s)