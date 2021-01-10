import shelve

# handles file content as dictionary
with shelve.open('mydata') as f:
    f['cats'] = ['maya', 'yuna', 'praga', 'lola','tina']

with shelve.open('mydata') as f:
    f['cats']
