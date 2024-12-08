from functions import salary,hello_who

if salary != 20:
    print('error')
if hello_who('max') != 'hello,':
    print('failed')
else:
    print ('good')
if hello_who('leo') != 'hello,leo':
    print('failed')
else:
    print('amazing')
if hello_who('dima') != 'hello,dima':
    print('failed')





