class CSVFile():
    # inizializzo l'oggetto con il nome del file .csv e ha
    # un attributo name che contiene il nome del file .csv
    def __init__(self, name):
        self.name = name

    # ha un metodo get_data() che torna i dati del file
    # come lista di liste (restituisce errore se lista vuota)
    def get_data(self):
        try:
            elements = []
            result = []
            my_file = open(self.name, 'r')
        except:
            print('Errore: il file inserito è vuoto.')
        
        for line in my_file:
            elements = line.split(',')
            elements[1] = elements[1].strip('\n')
            result.append(elements)
            
        return result[1:]


class NumericalCSVFile(CSVFile):

    #def __init__(self, name):
    #    super().__init__(name)

    # self solo nella definizione, non nella chiamata
    def original_get_data(self):
        num_values = super().get_data()
        try:
            for line in num_values:
                for number in line:
                    try:
                        number = float(number)
                    except:
                        number = None
        except:
            print('Errore: il file contiene valori diversi da numeri.')
            num_values = None

        return num_values


"""
file = NumericalCSVFile('shampoo_sales.txt')
print(file.original_get_data())
"""