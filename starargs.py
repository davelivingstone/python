# Proving that *args creates a tuple of arguments,
# not a list of arguments. Then I add them up.

def sumall(*args):
    print(f'{args} are the arguments.')
    return 'Their sum is '+ str(sum(args))

print(sumall(3, 43, 34))

