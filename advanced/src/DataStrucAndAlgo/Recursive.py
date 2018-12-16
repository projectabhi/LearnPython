# Perform such splitting in order to carry out some kind of clever recursive algoriths

items = [1, 10, 7, 4, 6, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))