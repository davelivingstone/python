''' I wanted to draw a pyramid make up of asterisks.
You need to center the stars too, so I figured out
a formula that adds spaces to the left and right,
depending on the number of stars in the iteration.'''

def pyramid(n):
    for i in range(1, n+1, 2):
        print(((n-i)//2)*' ' + '*'*i + ((n-i)//2)*' ')
        '''Or, if you want to turn it into a Christmas tree :)
        Only works for odd values of n, because the loop skips even values of i.
        Still thinking of a way to tweak it, but the point was to make a pyramid,
        not a fir tree.'''
        # if i == n:
        # 	print((n//2)*' ' + '*' + (n//2)*' ')


print(pyramid(15))
print(pyramid(25))
print(pyramid(100))
