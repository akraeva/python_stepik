def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2 * key in d:
        d[2*key].append(value)
    else:
        d[2 * key] = [value]


dc = {}
print(update_dictionary(dc, 1, -1))  # None
print(dc)                            # {2: [-1]}
update_dictionary(dc, 2, -2)
print(dc)                            # {2: [-1, -2]}
update_dictionary(dc, 1, -3)
print(dc)                            # {2: [-1, -2, -3]}
