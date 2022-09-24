import camelot
file="foo1.pdf"
table=camelot.read_pdf(file)
print(table[0].df)

# print("Hello")
