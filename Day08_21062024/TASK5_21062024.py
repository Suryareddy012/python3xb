def check_anagrams(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Check if the lengths of the strings are equal
    if len(s1) != len(s2):
        return False

    # Sort the characters in both strings and compare
    return sorted(s1) == sorted(s2)

# Test the function
string1 = "silent"
string2 = "listen"
if check_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")