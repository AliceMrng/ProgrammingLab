def sum_csv(files_name):
    values=[]
    my_file = open('shampoo_sales.csv','r')
#print(my_file.read())
#my_file.close()

    for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
            values.append(float(value))
    my_file.colse()
    somma=0
    for elements in my_file
        somma += elements
    return somma
    print (somma)