'''test = round(112.3232322, ndigits=-1)
print(test)

def sum (a, b):
    addi = (a + b)
    return addi

print(sum(1, 4))

compare = (3 == 3.0)

print(compare)

planets = ['Mars', 'Venus', 'Mercury', 'Earth', 'Neptune', 'Pluto', 'Saturn', 'Jupiter', 'Uranus']

plant = [planet for planet in planets if len(planet) > 6]
print(plant)'''

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False