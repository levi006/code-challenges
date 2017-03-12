def capitals(word):
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    found_caps = []
    for i in range(len(word)):
        if word[i] in caps:            
            found_caps.append(i)
    return (found_caps)
            