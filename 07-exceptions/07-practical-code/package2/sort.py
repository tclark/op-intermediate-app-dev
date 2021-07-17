
def weirdsort(strlist):
    revs = [s[::-1] for s in strlist]
    revs.sort()
    return [s[::-1] for s in revs]

