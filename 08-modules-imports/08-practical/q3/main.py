""" Make the code below produce the desired output ONLY by adding 
import statements to this file, with ONE exception. You will find
that one of the imported names is not available in the module where
you expect to find it. Add that to the module.
"""


for sketch in mod.sketches:
    print(sketch)
oddly_sorted = weirdsort(mod.sketches)
package2.pretty.pretty_print_list(oddly_sorted)

roots = []
for val in package1.various_numbers():
    root = math.sqrt(val)
    roots.append(val)
package2.pretty.pretty_print_list(roots)

print(mod.homework_is_done())

# Expected output
"""
Cheese Shop
Dennis Moore
The Undertaker
Nudge Nudge
Self Defense Against Fresh Fruit
Exploding Penguin
The Fish-Slapping Dance
The Dead Parrot
[
  The Fish-Slapping Dance,
  Nudge Nudge,
  Dennis Moore,
  Exploding Penguin,
  Cheese Shop,
  The Undertaker,
  Self Defense Against Fresh Fruit,
  The Dead Parrot,
]
[
  10.288239290237525, (Your numbers will 
  13.658960612888274,  probably differ.)
  15.562899809880935,
  11.998011262506582,
  8.910524960549013,
  4.581276799932274,
  11.658837209140273,
  3.996341009687031,
  9.262174943321124,
  9.421888920408774,
]
My homework is done.
"""

