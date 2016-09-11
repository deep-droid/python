#generators
#OK yield statement?
#OK generators - iterators that create the elements on-the-fly
#OK generators have next method?

#Generators simplifies creation of iterators. A generator is a function #that produces a sequence of results instead of a single value.

# When a generator function is called, it returns a generator object without even beginning execution of the function. When next method is called for the first time, the function starts executing until it reaches yield statement. The yielded value is returned by the next call.