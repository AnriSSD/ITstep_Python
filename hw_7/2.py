def are_anagrams(str1, str2):
    str1_sorted = sorted(str1.lower())  # Convert to lowercase and sort characters
    str2_sorted = sorted(str2.lower())
    return str1_sorted == str2_sorted


# Nimushi
string1 = "race"
string2 = "care"
print(are_anagrams(string1, string2))
