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
            raise ExamException('Errore, file con il nome cercato inesistente.')
            
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
    previous_epoch = None
    daily_temperatures = []
    output_list = []
    for line in data_list:
        #prima iterazione
        if previous_epoch == None:
            daily_temperatures.append(line[1])
            previous_epoch = line[0]
        #iterazioni intermedie
        elif line != data_list[-1]:
            #dato dello stesso giorno
            if line[0]%one_day > previous_epoch%one_day:
                previous_epoch = line[0]
                daily_temperatures.append(line[1])
            #dato del giorno seguente
            else:
                output_list.append(my_average(daily_list))
                daily_list = []
                daily_list.append(list[1])
                previous_epoch = line[0]
        #ultima iterazione
        else:
            #stesso giorno
            if line[0]%one_day > previous_epoch%one_day:
                daily_temperatures.append(line[1])
                output_list.append(my_average(daily_temperatures))
            #giorno seguente
            else:
                output_list.append(my_average(daily_list))
                output_list.append(None)
        return output_list


def my_average(list):
    if len(list) == 1:
        print('none')
        return None
    sum = 0
    for value in list:
        sum += value
    print('somma')
    return float(sum/len(list))



time_series_file = CSVTimeSeriesFile(name = 'data.csv')
time_series = time_series_file.get_data()
print(compute_daily_max_difference(time_series))
