implications = []
sizes = ['s', 'm', 'l']

for i in sizes:
    implications.append(('t-shirt-' + i, 't-shirts'))

for i in range(1, 4):
    i_str = str(i)
    implications.append(('t-shirt-' + 'x' * i + 'l', 't-shirts'))
    implications.append(('t-shirt-' + 'x' * i, 't-shirts'))
    implications.append(('t-shirt-' + i_str + 'x', 't-shirts'))
    implications.append(('t-shirt-' + i_str + 'xl', 't-shirts'))
    implications.append(('t-shirt-' + 'x' * i + 'l',
                         't-shirt-' + 'x' * i))
    implications.append(('t-shirt-' + 'x' * i + 'l',
                         't-shirt-' + i_str + 'xl'))
    implications.append(('t-shirt-' + 'x' * i,
                         't-shirt-' + i_str + 'x'))

for i in implications:
    print('tmsu imply', i[0], i[1])
