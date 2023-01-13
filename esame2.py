class ExamException(Exception):
    pass

class Diff():
    def __init__(self, ratio = 1):
        #controllo sul valore di ratio
        if not (((isinstance(ratio, float)) or (isinstance(ratio, int))) and (ratio > 0)):
            raise ExamException('Erroe, valore del ratio non valido')
        self.ratio = ratio


    def compute(self, data):
        #----------- sanitizzazione lista passata -----------#
        
        #controllo sul tipo della lista
        if not isinstance(data, list):
            raise ExamException('Errore, non si ha passato una lista')
            
        #controllo sulla lunghezza:
        if len(data) == 0:
            raise ExamException('Errore, lista vuota')
        if len(data) == 1:
            raise ExamException('Errore, è presente solo un elemento')
            
        # provo a convertire i valori della lista in float
        try:
            for element in data:
                element = float(element)
        except:
            raise ExamException('Errore, dati non validi')


        #----------- calcolo differenza valori -----------#
        diff = []
        for index in range(len(data)-1):
            temp = data[index+1] -data[index]
            if temp<0: 
                temp = -temp
            diff.append(temp)

        # applico il ratio
        print(self.ratio)
        if self.ratio != 1:
            for index in range(len(diff)):
                diff[index] = diff[index]/self.ratio
                
        return diff

lista = [2,4,8,16,32,64]
diff = Diff(2)
print(diff.compute(lista))