def unique(new_list=[]):
    no_dup = []
    for x in new_list:
        if x not in no_dup:
            no_dup.append(x)
    return no_dup

#print(unique([1, 1, 4, 5, 1]))

print(unique(['Mark', 'Mark', 'John', 'Anne']))
        