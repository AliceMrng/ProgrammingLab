
class CSVFile () :
    def __init__(self , name):
        self.name = name
    def get_data(self):
        values=[]
        my_file = open(self.name,'r')
        for line in my_file:
            elements = line.split(',')
            elements[-1]=elements[-1].strip()
            if elements[0] != 'Date':
                values.append(elements)
        my_file.close()
        return values
        
file=CSVFile('shampoo_sales.csv')
print(file.get_data())


