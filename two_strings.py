def two_strings(s1,s2):
    s1_list = []
    for k in s1:
        s1_list.append(k)
    for i in s2:
        if i in s1_list:
            return 'YEs'
    return 'No'

print(two_strings('hi', 'world'))