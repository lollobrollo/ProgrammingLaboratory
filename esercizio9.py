class Model():
# la classe generale è questa, quando voglio fare qualcosa di 
# specifico posso fare sottoclasse con fit e/o predict

# uso un'eccezione per mandare un segnale

    def fit(self, data):
        #fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
#

#-------======= sottoclasse che implementa metodo predict =======-------#
        
class IncrementModel(Model):

    #metodo per calcolare l'incremento medio dei dati passati
    def comp_avg_inc(self, data):
        
        #procedo a sanitizzare gli input

        #controllo se ho una lista in input
        if type(data) != list:
            raise TypeError('Errore, il file non è una lista.')

        #controllo se la lista ha solo un valore
        if len(data) <= 1:
            raise Exception('Errore, numero di elementi insufficenti.')

        #provo a convertire la lista in valori interi
        for element in data:
            try:
                element = float(element)
            except Exception as e:
                print('Errore nella conversione a float: "{}"'.format(e))

        #controllo se il valore è negativo
        for element in data:
            if element < 0:
                print('Attenzione, alcuni valori inseriti sono negativi.')

        #calcolo l'incremento medio
        precedente = None
        med_value = 0
        for item in data:
            if precedente == None:
                precedente = float(item)
            else:
                med_value += item - precedente
                precedente = float(item)

        med_increment = med_value / (len(data)-1)
        return med_increment
        
    
    #metodo predict implementato
    def predict(self, data):

        #calcolo l'incremento medio
        med_increment = comp_avg_inc(data)

        #restituisco il valore predetto
        return (data[-1] + med_increment)


#-------======= sottoclasse che implementa metodo fit =======-------#

class FitIncrementModel(IncrementModel):

    def __init__(self):
        self.global_avg_inc = None

        
    #implemento metodo fit
    def fit(self, data):
        self.global_avg_inc = comp_avg_inc(data)
        
    #metodo predict che utilizza il fit
    def predict(self, data):

        med_increment = (self.global_avg_inc + comp_avg_inc(data))/2
        #restituisco il valore predetto
        return (data[-1] + med_increment)