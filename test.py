from example import add

assert add(1, 2) == 3
assert add(1, 3.0) == "Bad inputs"
assert add("a", "b") == "Bad inputs"
