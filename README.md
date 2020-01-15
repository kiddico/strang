## Strang

Strang is a stringy library that supports (some) algebraic operations.

Originally the goal was to make the old style format strings as confusing as possible. For instance:

    'this is %s' % 'strang'

would normally evaluate to "this is istrang", but if the first string was a strang string the modulo of the first string by the second would be returned.

### What?

Seeing as there's no precedent for how mathmatical operations on strings should work (other than add/concatenate) the semantics of each operation is up for liberal interpretation.

### Why?

You clearly don't know me very well.
