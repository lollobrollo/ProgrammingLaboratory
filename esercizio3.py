def containsLetter(string, letter):
    return letter in string

def sum_csv(file_name):
    my_file = open(file_name, 'r')
    sum = 0
    for line in my_file:
        elements = line.split(',')
        
        if(test_string(elements[1])):
            sum += float(elements[1])

    my_file.close()
    if(sum == 0):
        sum = None
    return sum

def test_string(string):
    alphabet = {'a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    flag = 0
    for letter in alphabet:
        if(letter in string):
            flag += 1

    if(flag == 0):
        return 0
    return 1