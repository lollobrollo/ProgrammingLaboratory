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
            print('Errore in apertura del file: "{}"'.format(e))

            
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
                #per ogni riga splitto sulla virgola
                elements = row.split(',')

                #rimuovo i caratteri speciali
                elements[-1] = elements[-1].strip()

                #se non sono sulla prima riga 
                if elements[0] != 'Date':
                    result.append(elements)
                    
            my_file.close()
            return result


            
#==============================
# Classe per file NumericalCSV
#==============================

class NumericalCSVFile(CSVFile):

    # self solo nella definizione, non nella chiamata
    def get_data(self):
        string_values = super().get_data()
        
        #creo lista per immagazzinare i valori convertiti a float
        num_values = []

        #se il file non è vuoto
        if string_values != None:

            #per ogni riga della lista
            for row in string_values:
                
                #creo lista temporanea per i valori della riga
                temp_row = []
                #setto una flag a True
                test_float = True

                #per ogni elemento nella riga
                for i,column in enumerate(row):
                    #se sono nella prima colonna
                    if i == 0: 
                        temp_row.append(column)

                    #se non sto processando la data
                    else:
                        #provo a convertire a float il valore
                        try:
                             num_val = float(column)
                            
                        #se non ci riesco alzo la flag per saltare la riga
                        except Exception as e:
                            test_float = False
                            print('Errore, il valore "{}" non è numerico: "{}"'.format(num_val, e))
                        if test_float:
                            temp_row.append(num_val)
                    
                if test_float:
                    num_values.append(temp_row)
                    
            return num_values

        else:    #se il file è vuoto
            print('Errore, il file è vuoto.')
            return None

'''
file = NumericalCSVFile('shampoo_sales.txt')
print(file.get_data())
'''
