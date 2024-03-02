from collections import namedtuple

Books = namedtuple('Books', 'id name price')

books = [
    (1, "Oltin shaharlar",12000),
    (1, "Saodat Asri",120000),
    (1, "Saodatga etaklovchi hikmatlar",28000),

]

for book in books:
    bk = Books(*book)
    print(bk.id, bk.name, bk.price)


