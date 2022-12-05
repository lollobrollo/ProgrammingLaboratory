class CSVFile:
    
    def __init__(self, name):

        #con il type() verifico che il nome sia una stringa
        
        if not type(name) == str :
            raise Exception('Errore, il nome del file non è una stringa')

        #inzializzo self.name a name
        
        self.name = name

    def get_data(self, start=None, end=None): 
            
        #provo ad aprire il file
            
        try:

            my_file = open(self.name, 'r')
            
        except:
            
            print("Errore nell'apertura del file")

            #restituisco false se non riesco ad aprire il file
            
            return False

        #in qualunque caso io mi salvo tutti i dati
        #dopodiché capirò cosa devo restituire 
        #all'utente
    
        data = []

        for row in my_file:
                elements = row.split(',')
                elements[-1] = elements[-1].strip()
                data.append(elements)
            
        #caso base in cui non ci sono indici
        #di inizio o di fine
        
        if start == None and end == None:
        
            return data[1:]

        #un caso base in cui devo alzare 
        #un'eccezione è start == 0

        if start == 0:
            raise Exception('Errore Logico-Matematico: Start value 0')

        #provo a convertire in int start ed end

        #booleana che mi indica se ho valori negativi
            
        negative = False

        #booleana che mi indica se start = None
        
        start_None = False

        #booleana che mi indica se end = None
        
        end_None = False

        #verifico tutto ciò che serve sullo start
        
        try:

            #questa semplice espressione mi indica se un oggetto
            #è di tipo None
            
            if not start:
                start_None = True

            #se start non è None provo a convertirlo ad intero
                
            else:
                
                int_start = int(start)

                #se start è negativo lo segno
                
                if int_start < 0 :
                    negative = True

        #se mi ha dato problemi durante la conversione
        #alzo un'eccezione e returno None (eccezione non necessaria)
        except:
            raise Exception()
            print('Errore di conversione')
            return None

        #verifico tutto ciò che serve su end
            
        try:

            if not end:
                end_None = True

            else:
                
                int_end = int(end)

                if int_end < 0 :
                    negative = True
                
        except:
            raise Exception()
            print('Errore di conversione')
            return None

        #caso in cui start e/o end siano negativi

        if negative == True:
            raise Exception('Errore: Start e/o End negativi')
            return False

        #ora devo controllare una singola cosa:
        #che il range rischiesto esista
        
        #con len(data) ottengo la dimensione della lista
            
        dim = len(data)

        #studio i casi di Start == None / Endl == None

        #caso di start == None

        if start_None:

            #io so che se start == None allora end è un intero
            
            end = int(end)

            #verifico che end sia all'interno del range
            
            if end < dim:

                #il programma in tal caso richiede di non ritornare 
                #l'intestazione nell'ultimo elemento 
                
                return data[1:end]

            #se end è all'esterno del range alzo un'eccezione e restituisco None
                
            raise Exception('Errore: End maggiore di dim')
            return None

        #caso end == None
        
        if end_None:

            #io so che se end == None allora start è un intero
            
            start = int(start)

            #verifico che start sia all'interno del range
            
            if start < dim:

                #il programma in tal caso richiede di ritornare
                #gli elementi dalla posizione start meno uno a 
                #end menu uno

                #carico su una nuova lista le righe che ci servono
                
                correct_data = []
                
                for item in data[start-1:]:
                    
                    correct_data.append(item)
                
                return correct_data

            #se start è all'esterno del range alzo un eccezione e restituisco None
                
            raise Exception('Errore: Start maggiore di dim')
            return None
            
        #ora mi è solo rimasto il caso in cui entrambi start ed end
        #sono numeri interi

        start = int(start)
        end = int(end)

        #caso in cui start sia maggiore di end
        
        if start > end:

            #se start è maggiore di end alzo un eccezione e restituisco None
            
            raise Exception('Errore Logico-Matematico: Start maggiore di End')    
            return None
        
        #poiché sappiamo che start < end non c'è il caso in cui
        # start > dim ed end < dim
        
        if start > dim or end > dim:

            #se start oppure end sono all'esterno del range
            #alzo un eccezione e restituisco None
            
            raise Exception("Errore Logico-Matematico: Start ed End / End out of bound")
            return None

        #possiamo finalmente dire che non ci sono più possibili errori
        #il programma in tal caso ci richiede di restituire 
        #dall'elemento prima di start all'ultimo escluso

        return data[start-1:end]
         
class NumericalCSVFile(CSVFile):

    #con args e kwargs posso importare in manier automatica
    #la possibilità o meno di usare start and end
    
    def get_data(self, *args, **kwargs):
        data_str = super().get_data(*args, **kwargs)
        data_num = []
        #print("ciao!!!")
        for row_str in data_str:
            row_num = []
            for i, data in enumerate(row_str):
                if i==0:
                    row_num.append(data)
                else:
                    try:
                        row_num.append(float(data))
                    except:
                        print('Errore di conversione')
                        break;

            #con questo non inserisco le righe corrotte
                        
            if(len(row_num) == len(row_str)):         
                data_num.append(row_num)
                              
        return data_num