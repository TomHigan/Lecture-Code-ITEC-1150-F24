total = 0
more_books = True

while more_books:
    book_price = float(input('Enter price of book $: '))
    total = total + book_price
    any_more = input('Any more Books Enter "Y" or "N": ')
    if any_more.upper() == 'N':
        more_books = False

print(f'The total of all the books is ${total}.')