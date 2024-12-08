from functions import salary,hello_who

assert hello_who('max') == 'hello_max', 'hello who error'
assert hello_who('leo') == 'hello_leo', 'hello who error'
assert hello_who('nikita') == 'hello_nikita', 'hello who error'
assert salary(2, 1) == 4
assert salary(2, 2) == 8
