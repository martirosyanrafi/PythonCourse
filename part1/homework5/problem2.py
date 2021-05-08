values = ['a', 0, 2]

for item in values:
    print('The entry is:', item)

    try:
        print('The reciprocal of', item, 'is', 1 / item)
    except Exception as e:
        print('Oops!', e)
