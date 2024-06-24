from fake_math import divide as div_fake
from true_math import divide as div_true


result1 = div_fake(69, 3)
result2 = div_fake(3, 0)
result3 = div_true(49, 7)
result4 = div_true(15, 0)
print('Деление из модуля fake_meth:', result1)
print('Деление из модуля fake_meth:', result2)
print('Деление из модуля true_meth:', result3)
print('Деление из модуля true_meth:', result4)
