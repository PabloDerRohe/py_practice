#########################################################
#            TEXT TO CSV EXPENSES CONVERTER             #
#########################################################

#### VARIABLES 
integers = '0,1,2,3,4,5,6,7,8,9'
file1 = []
raw_file = []

open_name = input('Type the name of the file you want to convert: ')

# Abrimos el archivo y lo almacenamos en filas como lista
with open(open_name, 'r') as f:
    raw_file = f.readlines()

# Chequeo de contenido del archivo
# print(raw_file)

# Recorremos el archivo y lo transformamos en lista
def clean_up():
    for item in raw_file:
        indx = 0
        # Limpiamos el archivo de saltos
        item = item.strip('\n')
        for i in item:
            if i in integers:
                indx = item.index(i)
                break
        item_f = ','.join(item.rsplit(' ', 1))
        if item != '':
            file1.append(item_f.split(','))

def indexes():
    for item in file1:
        item.insert(0, str(file1.index(item)))

def transform():
    global file2
    file2 = [','.join(item) for item in file1]
    file2 = '\n'.join(file2)
    # print(file2)


clean_up()
indexes()
transform()

# Imprimimos resultados
print(file1)

save_name = input('Save file as: ')


# Guardamos resultado en archivo
with open(save_name + '.csv', 'w') as file_csv:
    file_csv.write(file2)
