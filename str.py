def str():
    message = "Lkkokvekk pkykthon kprkkogrkammkinkkgk."
    sliced = message[len(message) - 7:len(message)]
    print(sliced)          # inkkgk.

    result = []
    for _, value in enumerate(message):
        if value == "k":
            continue
        
        result.append(value)

    print("".join(result))
    
str()