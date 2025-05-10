l1 = [1,2,3,4,5,6]
l2 = [1,2,3,4]

for l1,l2 in zip(l1,l2):
    print(l1, '+',l2,end=' = ')
    print(f'{l1 + l2}')