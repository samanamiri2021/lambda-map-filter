nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
squares = list(map(lambda n: n ** 2, evens))
print("Evens:", evens)
print("Their squares:", squares)
