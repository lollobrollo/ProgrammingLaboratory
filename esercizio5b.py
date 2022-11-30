class CSVFile():
    def __init__(self, name):
        #setto il nome del file
        self.name = name
        
        #controllo se il file è vuoto
        self.is_empty = False #è una caratteristica del file, permanente
        try:
            test_string = open(self.name, 'r')
            test_string.readline()
        except Exception as e:
            self.is_empty = True
            print('Errore in apertura del file: {}'.format(e))

            
    def get_data(self):
        #controllo se posso utilizzare il file pasato
        if self.is_empty == True:
            print('Errore, il file non è stato aperto o è illeggibile')
            return None
            
        else:
        #se il file è valido procedo con la funzione
        
            result = []
            my_file = open(self.name, 'r')
            
            for row in my_file:
                elements = row.split(',')
                elements[-1] = elements[-1].strip('\n')
                if elements[0] != 'Date':
                    result.append(elements)
                    
            my_file.close()
            return result


            
#==============================
# Classe per file NumericalCSV
#==============================

class NumericalCSVFile(CSVFile):

    #def __init__(self, name):
    #    super().__init__(name)

    # self solo nella definizione, non nella chiamata
    def get_data(self):
        values = super().get_data()
        num_values = []
        if values != None:    #se il file non è vuoto
            for row in values:    #per ogni riga della lista
                temp_row = []    
                test_float = True
                for i,column in enumerate(row):    #per ogni colonna delle righe
                    while test_float:
                        if i == 0: #se  sono nella prima colonna
                            temp_row.append(column)
                        else:    
                            num_val = None
                            try:
                                 num_val = float(column)
                            except Exception as e:
                                test_float = False
                                print('Errore, il valore "{}" non è numerico: "{}"'.format(val, e))
                                
                    if test_float:
                            temp_row.append(num_val)
                
                if test_float:
                    num_values.append(temp_row)
            return num_values

        else:    #se il file è vuoto
            print('Errore, il file è vuoto.')
            return None

"""
file = NumericalCSVFile('shampoo_sales.txt')
print(file.original_get_data())
"""
