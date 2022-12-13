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
    #classe che implementa metodo predict
    def predict(self, data):

        #procedo a sanitizzare gli input

        #controllo se ho una lista in input
        if type(data) != list:
            raise TypeError('Errore, il file non è una lista.')

        #controllo se la lista è vuota
        if(data == None):
            raise Exception('Errore, la lista è vuota.')

        #controllo se la lista ha solo un valore
        if len(data) == 1:
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
                precedente = int(item)
            else:
                med_value += item - precedente
                
                precedente = int(item)

        #calcolo l'incremento medio
        med_increment = med_value / (len(data)-1)

        
        # if incremento >= 0:
        predicted_value = int(data[-1]) + med_increment  
        # else:
        # #rendo negativo l'incremento se serve
        #     predicted_value = int(data[-1]) - med_increment

        #calcolo e restituisco il valore predetto
        return predicted_value
#



# data = [50, 20, -10]
# data = {'1':1}
# model = IncrementModel()
# print(model.predict(data))