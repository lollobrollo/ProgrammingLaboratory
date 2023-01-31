class ExamException(Exception):
    pass


class CSVFile():
    def __init__(self, name):
        self.name = name
        if not(isinstance(self.name, str)):
            raise ExamException('Errore, il nome non è una stringa.')
            
    def get_data(self):
         pass


class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        try:
            input_data = open(self.name, 'r')
        except:
            raise ExamException('Errore, file con il nome desiderato inesistente.')

        # assumo che in ogni caso la prima colonna contenga l'epoch, la seconda la temperatura
        output_data = []
        previous_epoch = 0
        for line in input_data:
            line_elements = line.split(',')
            line_elements[1].strip()
            try:
                line_elements[0] = int(line_elements[0])
                line_elements[1] = float(line_elements[1])
                output_data.append(line_elements[0:2])
                                    
                if line_elements[0] > previous_epoch:
                    previous_epoch = line_elements[0]
                else:
                    raise ExamException('Errore, epoch non ordinati.')
            except:
                pass

        return output_data


def compute_daily_max_difference(data_list):
    try:
        if len(data_list) < 1:
            raise ExamException('Errore, lista vuota.')
    except:
        raise ExamException('Errore, lista non valida.')

    one_day = 86400
    previous_day = None
    daily_temperatures = []
    output_list = []
    for line in data_list:
        # prima iterazione
        if previous_day == None:
            daily_temperatures.append(line[1])
            previous_day = line[0] - (line[0]%one_day)
        # iterazioni intermedie
        elif line != data_list[-1]:
            # dato dello stesso giorno
            if line[0] < previous_day + one_day:
                daily_temperatures.append(line[1])
            # dato del giorno seguente
            else:
                output_list.append(max_delta(daily_temperatures))
                daily_temperatures = []
                daily_temperatures.append(line[1])
                previous_day += one_day
        # ultima iterazione
        else:
            # stesso giorno
            if line[0] < previous_day + one_day:
                daily_temperatures.append(line[1])
                output_list.append(max_delta(daily_temperatures))
            # giorno seguente
            else:
                output_list.append(max_delta(daily_temperatures))
                output_list.append(None)
    return output_list


def max_delta(list):
    if len(list) == 1:
        return None
    return round(max(list) - min(list), 2)


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





time_series_file = CSVTimeSeriesFile(name = 'data.csv')
time_series = time_series_file.get_data()
daily_delta = compute_daily_max_difference(time_series)

lista1 = IncrementModel()
print('errore medio: ', lista1.evaluate(daily_delta, 3))

print('--------- uso anche il fit --------')
lista2 = FitIncrementModel()
lista2.fit(daily_delta[:17])
print('errore medio: ', lista2.evaluate(daily_delta[18:], 3))