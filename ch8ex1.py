#def chop(t):
#    del t[0]
#    del t[-1]
#    print(t)

def middle(x):
    return x[1:-1]


#     This was useful to truncate any list's first and last characters##############################
# def chop1(t):
#    n = len(t)
#    t2 = t[1:n-1]
#    print(t)
#    print(t2)


inp = ['a', 'b', 'c', 'd', 'e']

print('here is your first list:', inp)

rest = middle(inp)
print(rest)


#   this is useful to end a _while_ function#################################
    #while True:
        #inp = input("\n\nwatch me truncate your word, bro! first and last character's are TOAST!\n")
        #if inp == "done": exit()
