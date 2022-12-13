#Clave 9d5e3ecdeb4cdb7acfd63075ae046672 el numero es 9

#Code challenge one

def ch1(n, S):
    if (len(n) <= 100): 
        #Cambio de posiciones en lista y transformación de lista -> string
        word = ""
        for i in range(len(n) - 1, -1, -1):
            word += str(n[i]) + '-'

        #Borrado de valores mayores a S
        index = 0
        while(index < len(word)):
            if(word[index] != '-' and int(word[index]) >= S):
                    word_list = list(word)
                    word_list.pop(index)
                    word = "".join(word_list)
            else:
                index += 1

        #Transformación de string a lista
        new_list = []
        set = ''
        for i in range(len(word)):
            if word[i] != '-':
                set = set + word[i]
            else:
                if set != '':
                    new_list.append(int(set))
                    set = ''
        print(new_list)
    else:
        print("Número máximo superado")

ch1([1,2,3,4,5,6], 6)
ch1([10,20,30,40], 6)
ch1([6], 6)
ch1([66], 6)
ch1([65], 6)
ch1([6,2,1], 6)
ch1([60,6,5,4,3,2,7,7,29,1], 6)



def ch2(arr, S):
    for i in range(len(arr)):
            arr[i] = abs(arr[i])**2
    
    index = 0
    while(index < len(arr)):
        if (arr[index] > int(str(S) + str(S))):
            del arr[index]
        else:
            index += 1

    for i in range(0,len(arr)-1):  
        for j in range(len(arr)-1):  
            if(arr[j]>arr[j+1]):  
                temp = arr[j]  
                arr[j] = arr[j+1]  
                arr[j+1] = temp  

    
    print(arr)

ch2([1,2,3,5,6,8,9], 6)
ch2([-2,-1], 6)
ch2([-6,-5,0,5,6], 6)
ch2([-10, 10], 6)


def ch3(arr):
    if (len(arr) > 0):
        arr.sort()

        min = 0

        for i in range(len(arr)):
            if (min + 1 < arr[i]):
                break
            else:
                min += arr[i]
        print(min + 1)

        
ch3([5,7,1,1,2,3,22])
ch3([1,1,1,1,1])
ch3([1,5,1,1,1,10,15,20,100])
