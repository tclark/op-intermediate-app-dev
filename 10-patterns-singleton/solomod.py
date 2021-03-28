
# The class below is "private" to this module.
class _SoloMod:
    def __init__(self):
        # do some init stuff, idk
        pass

# The line below is only executed when the module is imported.
# Thus, we only ever make one instance.
solomod = _SoloMod() # The name 'solomod' is used by importers of this module.

# or, if you want it to look more object-y

class SoloMod:
    def __new__(cls):
        return solomod
