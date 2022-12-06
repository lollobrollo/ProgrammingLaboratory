class CSVFile():
    def __init__(self, name):

        
        #setto il nome del file
        self.name = name

        #alzo un'eccezione se il nome del file non è una stringa
        if not(type(self.name) == str):
            raise Exception('Errore, il nome del file non è una stringa.')
    
        
        #controllo se il file è vuoto
        self.is_empty = False #è una caratteristica del file, permanente
        
            
    def get_data(self, start = None, end = None):
        
        #provo ad aprire il file
        try:
            test_string = open(self.name, 'r')                
            test_string.readline()                
            test_string.close()
            
            #se qualcosa non va termino la funzione
        except Exception as e:
            print('Errore in apertura del file: "{}"'.format(e))
            return False

            
        #apro il file da analizzare
        my_file = open(self.name, 'r')

        #gestisco alcune eccezioni
        if type(my_file) == None:
            raise Exception('Errore, il file inserito è vuoto.')
            return None

        if type(my_file) == bool:
            raise Exception('Errore, il file inserito è booleano.')
            return None


        #creo una lista per immagazzinare i dati
        data = []

        #prendo il file completo e lo immagazzino
        for row in my_file:
            elements = row.split(',')
            elements[-1] = elements[-1].strip()
            data.append(elements)

            
        #devo restituire la lista in base a start e/o end
        #di seuito sanitizzo i valori estremi
            
        #prendo la lunghezza del file per fare controlli
        lunghezza = len(data)
       
        #creo una variabile per il valore di start
        start_value = 1

            
        #controllo sul valore di start
        if(start != None):
            
            #provo a convertire il valore a intero
            try:
                start = int(start)
            except:
                raise Exception('Errore, il valore inserito non è intero.')
                return None
            
            #controllo se start è un valore intero
            if(type(start) == int):
                start_value = start
            else:
                raise Exception('Errore, il valore inserito non è intero.')
                return None

            #controllo se il valore è valido nell'intervallo
            if(start_value <= 0 or start_value > lunghezza):
                raise Exception('Errore, il  valore di start non è valido.')
                return None


                
        #creo  una variabile per il valore di end
        end_value = lunghezza
        
        #passo a controllare il valore di end
        if(end != None):

            #provo a convertire il valore a intero
            try:
                end = int(end)
            except:
                raise Exception('Errore, il valore inserito non è intero.')
                return None

            #controllo se è un valore intero
            if(type(end) == int):
                end_value = end
            else:
                raise Exception('Errore, il valore di end non è intero.')
                return None

            #controllo se il valore è valido nel mio caso
            if(end_value < start_value or end_value >= lunghezza):
                raise Exceprion('Errore, il valore di end non è valido.')


        my_file.close()

        
        #se non ho valori di start e end restituisco tutta la stringa
        if(start == None and end == None):
            return data[1:]

        if(start == None and end != lunghezza):
            return data[1:end_value]

        if(start != None and end == None):
            return data[start_value-1:]

        if(start != None and end != None):
            return data[start_value-1:end_value]


  
#==============================
# Classe per file NumericalCSV
#==============================

class NumericalCSVFile(CSVFile):

    # self solo nella definizione, non nella chiamata
    def get_data(self, *args, **kwargs):
        string_values = super().get_data(*args, **kwargs)
        
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
