#Clave 9d5e3ecdeb4cdb7acfd63075ae046672 el numero es 9

#Code challenge one

def ch1(n, S):
    if (len(n) <= 100): 
        #Reverse de lista y transformación de lista -> string separado por guiones
        #[1,2,33] -> ['1','-','2','-','3','3','-']
        listWithDashes = ''
        for i in range(len(n) - 1, -1, -1):
            listWithDashes += str(n[i]) + '-'
    

        #Borrado de valores mayores a S
        aux = []
        for i in range(len(listWithDashes)):
            if(listWithDashes[i] == '-' or int(listWithDashes[i]) < S):
                    aux.append(listWithDashes[i])

        #Eliminación de guiones auxiliares y union de valores
        new_list = []
        set = ''
        for i in range(len(aux)):
            if aux[i] != '-':
                set = set + aux[i]
            else:
                if set != '':
                    new_list.append(int(set))
                    set = ''
        print(new_list)
    else:
        print("Número máximo superado")

print("\nPrimer challenge\n")

ch1([1,2,3,4,5,6],6)
ch1([10,20,30,40], 6)
ch1([6], 6)
ch1([66], 6)
ch1([65], 6)
ch1([6,2,1], 6)
ch1([60,6,5,4,3,2,7,7,29,1], 6)

ch1([99], 9)
ch1([99001290909192993,99,1,2,3], 9 )



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

print("\nSegundo challenge\n")
ch2([1,2,3,5,6,8,9], 6)
ch2([-2,-1], 6)
ch2([-6,-5,0,5,6], 6)
ch2([-10, 10], 6)

ch2([1,2,3,4,5,6,8,9,10],9)
ch2([-10,2,3,4,5,6,8,9,10],9)


def ch3(arr):
    #Tener monedas
    if (len(arr) > 0):
        #Organizarlas de menor a mayor
        arr.sort()

        min = 0
        for i in range(len(arr)):
            #Si la siguiente moneda a agarrar es mayor al minimo actual más 1, el minimo es min + 1
            if (min + 1 < arr[i]):
                break
            #Sino, tomar la moneda y aumentar el minimo
            else:
                min += arr[i]
        print(min + 1)

print("\nTercer challenge\n")
ch3([1,2,4,8])
ch3([5,7,1,1,2,3,22])
ch3([1,1,1,1,1])
ch3([1,5,1,1,1,10,15,20,100])
ch3([1,1,2,3,10])

