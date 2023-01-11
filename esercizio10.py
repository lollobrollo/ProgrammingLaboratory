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

    def evaluate(self, data):
        #evaluate non implementato nella classe base
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
                precedente = item
            else:
                med_value += item - precedente
                precedente = item

        med_increment = med_value / (len(data)-1)
        return med_increment


    #metodo predict implementato
    def predict(self, data):
        #restituisco il valore predetto
        return (data[-1] + self.comp_avg_inc(data))


    def evaluate(self, data, window):
        # se sono nella sottoclasse con il fit, procedo solo se lo ho fatto
        try:
            if self.global_avg_increment == None:
                print("Errore, non è stato fatto il fit")
                return None
        except:
            pass
            
        # sanitizzo la finestra di valori
        try:
            window = int(window)
        except:
            raise Exception("Errore, finestra non intera")

        if (window<=0) or (window >= len(data)):
            raise Exception("Errore, lunghezza finestra non valida")

        # calcolo gli errori su tutte le predizioni
        errors = []
        
        for index, element in enumerate(data):
            print('indice ed elemento attuale: ', index, ', ', element)
            end_index = index + window
            if (end_index) < len(data):
                try:
                    print('dati per la predizione: ',data[index: end_index])
                    prediction = self.predict(data[index: end_index])
                    errors.append(self.abs_val(prediction, element))
                except:
                    raise Exception("Errore, metodo predict non funzionante")
        
        # calcolo l'errore medio e lo restituisco
        media = 0
        for value in errors:
            media += value

         # se sono nella sottoclasse col fit faccio il calcolo di conseguenza
        try:
            return(media + self.global_avg_increment)/(len(errors)+1)
        except:
            print('la classe attuale predice senza il fit')
            return media /(len(errors))
        
    # metodo per il valore assoluto   
    def abs_val(self, a, b):
        if (a-b) < 0:
           return b-a
        return a-b
        
#-------======= sottoclasse che implementa metodo fit =======-------#

class FitIncrementModel(IncrementModel):

    def __init__(self):
        self.global_avg_increment = None

        
    #implemento metodo fit
    def fit(self, data):
        self.global_avg_increment = self.comp_avg_inc(data)
        
    #metodo predict che utilizza il fit
    def predict(self, data):

        med_increment = (self.global_avg_increment + self.comp_avg_inc(data))/2
        #restituisco il valore predetto
        return (data[-1] + med_increment)
#


# lista = [8, 19, 31, 41, 50, 52, 60, 67, 72, 72, 67, 72]

# lista1 = IncrementModel()
# print('errore medio: ', lista1.evaluate(lista, 3))

# print('-----------------')
# lista2 = FitIncrementModel()
# lista2.fit(lista[:6])
# print('errore medio: ', lista2.evaluate(lista[7:], 3))