#!/usr/bin/env python3

# Strang : Breaking the % operator since 1994.

class Strang(str):

    def verify_stringy(questionable):
        if type(questionable) is not str:
            try:
                str(questionable)
                return True
            except:
                raise TypeError('Cannot convert {} to string.'.format(questionable))
        return True


    def __init__(self, given):
        if Strang.verify_stringy(given):
            string = str(given)
        else:
            string = given
        self.s = string


    # The operation that sparked the idea.
    # aka : What if I made "'%s' % (string)" more confusing?
    # Casts each character in a string to an int, mods the lsv by the corresponding rsv
    # Casts the result back to characters.
    # Then it's all joined into a new (and slightly less useful) string.
    def __mod__(self, other):
        if Strang.verify_stringy(other):
            other = str(other)
        else:
            raise TypeError('Cannot convert {} to a string.'.format(repr(other)))

        A = self.s
        B = other

        ## Pad both strings to the max length of either.
        pad_to = max( len(A), len(B) )
        pad = lambda string:'{: <{pad_to}}'.format(string, pad_to=pad_to)
        A, B = pad(A), pad(B)

        # -32 at start, and +32 at exit.
        # Aligns to ascii 32 (space) and beyond. kinda hard to print control codes.
        aints = tuple( ord(char)-32 for char in A )
        bints = tuple( ord(char)-32 for char in B )

        # Manual toggle to watch each step.
        if False:
            changed(self.s, A, pad_to)
            changed(other,  B, pad_to)
            stepwise(aints, bints)
        # All lines below 100 characters will be ~~REDACTED~~.
        return ''.join( chr(pair[0]) if pair[1] <= 0 else chr((pair[0] % pair[1]) + 32 ) for pair in zip(aints, bints) )

    def __repr__(self):
        return repr(self.s)

# Strang wants to be a big boy like str
stra = Strang

def stepwise(aints, bints):
    pairs = tuple(pair for pair in zip(aints, bints))
    mod_pairs = tuple( pair[0] if pair[1] <=0 else pair[0] % pair[1] for pair in pairs )
    mod_pairs_chars = tuple( '' if (v+32)<0 else chr(v+32) for v in mod_pairs)
    for p, m, c in zip(pairs, mod_pairs, mod_pairs_chars):
        print('{}\n{}\n"{}"'.format(p,m,c))
def changed(pre, post, pad_to):
    print('{:<{pad_to}} ({}) -> {} ({})'.format(pre, len(pre), post, len(post), pad_to=pad_to))



def main():
    strang = Strang('abc')
    print('"abc" % "defdef"')
    print('"{}"'.format( strang % 'defdef') )

    print('')
    print('"defdef" % "abc"')
    print('"{}"'.format( Strang('defdef') % strang) )

    print('')
    print('"abc" % "aaa"')
    print('"{}"'.format( strang % 'aaa') )

    print('')
    print('"aaa" % "abc"')
    print('"{}"'.format( Strang('aaa')%strang) )

    strange_string = Strang('e')





if __name__ == '__main__':
    main()
