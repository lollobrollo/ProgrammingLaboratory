class CSVFile():

    #inizializzo l'oggetto con il nome del file .csv e ha un attributo name che contiene il nome del file .csv
    def __init__(self, name):
        self.name = name

    #ha un metodo get_data() che torna i dati del file come lista di liste
    def get_data(self):
        elements = []
        result = []
        my_file = open(self.name, 'r')
        
        for line in my_file:
            elements = line.split(',')
            elements[1] = elements[1].strip('\n')
            result.append(elements)
            
        return result[1:]

"""
file = CSVFile('shampoo_sales.txt')
print(file.get_data())
"""    