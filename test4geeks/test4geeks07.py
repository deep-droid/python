#list as dictionary keys
#https://wiki.python.org/moin/DictionaryKeys

# Dictionaries, in Python, are also known as "mappings", because they "map" or "associate" key objects to value objects:


# Toggle line numbers
   # 1 # retrieve the value for a particular key
   # 2 value = d[key]
# To be used as a dictionary key, an object must support the hash function (e.g. through __hash__), equality comparison (e.g. through __eq__ or __cmp__), and must satisfy the correctness condition above

# That said, the simple answer to why lists cannot be used as dictionary keys is that lists do not provide a valid __hash__ method. Of course, the obvious question is, "Why not?"

# The builtin list type should not be used as a dictionary key.

# Note that since tuples are immutable, they do not run into the troubles of lists - they can be hashed by their contents without worries about modification. Thus, in Python, they provide a valid __hash__ method, and are thus usable as dictionary keys.


# Answer:
# lists are mutable and therefore not hashable
