# 1 -

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

def is_even(num):
    return num % 2 == 0

# 2 -
def slugify(text):
    return text.strip().lower().replace(" ", "-")
 
# 3 -
def count_vowels(text):
    count_of = 0
    for i in text:
        if i in "aeiou":
            count_of += 1
    print(count_of)
    return count_of
