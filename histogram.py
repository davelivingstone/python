# Count the number of times a letter appears in  a string:

def histogram(s):
    '''We create an empty dictionary. We could
    use dict(), but a literal is faster than a function call'''
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(histogram('brontosaurus'))

# Shorter version of histogram, which I wrote using get():

def histo(s):
    d = {}
    for c in s.lower():
        d[c] = d.get(c, 0) + 1
    return d

print(histo('A man, a plan, a canal, Panama'))

