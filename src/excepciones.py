# @author luis

# proximo en implementarse v2
num: int = 24
numpy: int = 0

try:
    print(f'{num/numpy}')
except ZeroDivisionError as e:
    print(f'Error: {e}')


def proxy(error: str):
    raise KeyError('Error pulgadas no validas')