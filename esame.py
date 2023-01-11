class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, window):
    
        #----------- sanitizzazione valore finestra -----------#
        
        # controllo se la finestra è un valore intero
        if not isinstance(window, int):
            raise ExamException('Errore, la finestra non è un numero intero')

        #controllo se la finestra è un valore positivo    
        if window < 1:
            raise ExamException('Errore, la finestra è un numero minore di 1')

        self.window = window
            

    def compute(self, lista):
        #----------- sanitizzazione lista passata -----------#
        
        #controllo sul tipo della lista
        if not isinstance(lista, list):
            raise ExamException('Errore, non si ha passato una lista')
            
        #controllo sulla lunghezza:
        if len(lista) == 0:
            raise ExamException('Errore, lista vuota')

        # provo a convertire i valori della lista in float
        try:
            for element in lista:
                element = float(element)
        except:
            raise ExamException('Errore, dati non validi')

        
            
        # se ho una lista di 1 elemento e una finestra di 1 elemento ritorno la lista
        if self.window == 1 and len(lista) == 1:
            return lista
            
        # caso in cui la finestra è più grande della lista
        if self.window > len(lista):
            raise ExamException('finestra maggiore della lunghezza della lista')

        #----------- calcolo media mobile -----------#
        media_mobile = []
        for index in range(len(lista) - self.window + 1):
            media_mobile.append(self.media(lista[index:index+self.window]))

        return media_mobile
        
    #metodo ausiliario per la media
    def media(self, lista):
        somma = 0
        for element in lista:
            somma += element
        return somma/len(lista)

# lista = [2, 4, 8, 16]

# istanza = MovingAverage(2)
# print(istanza.compute(lista))