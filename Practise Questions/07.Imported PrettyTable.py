import prettytable
table = prettytable.PrettyTable()
print(table)

table.add_column('#', [1,2,3,4])
print(table)
table.add_column('Name', ['Bulbasaur', 'Ivysaur','Venusaur','Mega Venusaur'])
print(table)
table.add_column('Type',['Grass','Grass','Grass','Grass'])
print(table)
table.clear()
print(table)

table.field_names = ['#', 'Name', 'Type']
table.add_row([1,'Bulabasaur','Grass'])
table.add_rows(
    [
        [2,'Ivysaur','Grass'],
        [3,'Venusaur', 'Grass'],
        [4,'Mega Venusaur', 'Grass']
    ]
)
table.align = 'l'
print(table)
