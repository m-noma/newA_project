for i in range(3):
    locals()["var" + str(i)] = i
    print("var{} : {}".format(i, locals()["var" + str(i)]))
