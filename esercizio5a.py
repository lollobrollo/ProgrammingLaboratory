'''
class CSVFile():

    # inizializzo l'oggetto con il nome del file .csv e ha
    # un attributo name che contiene il nome del file .csv
    def __init__(self, name):
        self.name = name
        
    # ha un metodo get_data() che torna i dati del file
    # come lista di liste
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
        '''

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