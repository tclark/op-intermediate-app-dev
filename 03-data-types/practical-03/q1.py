# Below are three pairs of strings. Before you run the code, try to 
# predict what will happen in each case. Then run the code. Did the
# results match your expectations? Can you explain the results?


st1 = 'Spam, spam, spam'
st2 = st1

print('st1 == st2: ' , st1 == st2)
print('st1 is st2: ', st1 is st2)

###
st3 = 'a'
st4 = 'a'

print('st3 == st4:', st3 == st4)
print('st3 is st4: ', st3 is st4)

### Triple quotes give us multi-line strings.
st5 = """Though yet of Hamlet our dear brother's death
The memory be green, and that it us befitted
To bear our hearts in grief and our whole kingdom
To be contracted in one brow of woe,
Yet so far hath discretion fought with nature
That we with wisest sorrow think on him,
Together with remembrance of ourselves.
"""
st6 = """Though yet of Hamlet our dear brother's death
The memory be green, and that it us befitted
To bear our hearts in grief and our whole kingdom
To be contracted in one brow of woe,
Yet so far hath discretion fought with nature
That we with wisest sorrow think on him,
Together with remembrance of ourselves.
"""

print('st5 == st6: ',st5 == st6)
print('st5 is st6: ',st5 is st6)
