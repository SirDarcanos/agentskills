from pricing import total
actual = total([40, 60], .10)
print(actual)
assert actual == 90, (actual, 90)
