# Python doesn't have a counting for loop in the way that 
# many other languages do (e.g., for(i=0;i<max;i++)).
# Instead, we use range() to produce a loop like this.

for i in range(5):
    print(i)
# The loop above works the way we would like.
# What does that tell us about range()?

print('\n\n') # just making some white space for later  

print(type(range(5)))
print(type(iter(range(5))))
# Explain the output of the above in terms of the Iterator 
# pattern.
