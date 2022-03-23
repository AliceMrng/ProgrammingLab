lista=[3,4,5]
def somma (list):
    Sum=0
    for i in range(len(list)):
        Sum = list[i] + Sum
    return Sum
risult = somma(lista)           
print('Somma:{}'.format(risult))

def somma (list):
    Sum=0
    for element in list:
        Sum = Sum + element
    return Sum
risult = somma(lista)           
print('Somma:{}'.format(risult))
