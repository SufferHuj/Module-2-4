# def process_data(data):
#     processed_data = transform_data(data)
#     result = calculate_result(processed_data)
#     return result
#
# def transform_data(data):
#     return [x * 2 for x in data]
#
# def calculate_result(data):
#     return sum(data)
#
# data = [1, 2, 3]
# final_result = process_data(data)
# print(final_result)
#
# def inner(a, b):
#     c = a + b
#     d = c * 2 # Поставьте тут точку останова
#     return d
#
# def outer(x):
#     y = 10
#     z = inner(x, y)
#     return z
#
# result = outer(5)
# print(result)

# def a(x): print("a"); return x + 1
# def b(x): print("b"); return x * 2
# def c(x): print("c"); return x ** 2
#
# result = a(b(c(2))) # Поставьте тут точку останова
# print(result)