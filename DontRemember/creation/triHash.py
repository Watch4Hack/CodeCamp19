import md5
import hashlib

SHA256 = ["B9776D7DDF459C9AD5B0E1D6AC61E27BEFB5E99FD62446677600D7CACEF544D0",
          "5694D08A2E53FFCAE0C3103E5AD6F6076ABD960EB1F8A56577040BC1028F702B",
          "14EBE56A5008E7C251101E9E1FDBE281AB0A82BD6FA00A5CEF746B9EE0DD31D1"]

def valid_lenght(Flag):
    if len(Flag) > 14:
        print 'La clave es demasiado larga'
        return False
    if len(Flag) % 7 != 0:
        print 'La clave es demasiado corta'
        return False
    if len(Flag) == 0:
        print 'No se ha introducido ninguna clave'
        return False
    else:
        return True

print ("#####  #####  ###    #####  #####  #####  ### ###  #####     ##  #####")
print ("#      #   #  #  #   #      #      #   #  #  #  #  #   #    # #  #   #")
print ("#      #   #  #   #  ####   #      #####  #  #  #  #####   #  #  #####")
print ("#      #   #  #  #   #      #      #   #  #     #  #          #      #")
print ("#####  #####  ###    #####  #####  #   #  #     #  #          #      #\n")
Flag = raw_input('Introduzca la clave de desbloqueo del software: ')

valid_tam = valid_lenght(Flag)
if valid_tam == True:
    correct = 0
    correctFlag = ""
    answer = ""
    for i in range(0, len(Flag)+7, 7):
        mod = i/7
        aux = ""
        if mod == 0:
            aux = Flag[:5]
            index = 2
        if mod == 1:
            aux = Flag[6:-5]
            index = 0
        if mod == 2:
            aux = Flag[10:]
            index = 1
        answer = answer + hashlib.sha256(aux.encode()).hexdigest()
        correctFlag = correctFlag + SHA256[index]
        if index != 1:
            answer = answer + "_"
            correctFlag = correctFlag + "_"
    if correctFlag.upper() == answer.upper():
        print("\nLa clave es correcta.")
        Flag = Flag.replace("e","3")
        Flag = Flag.replace("o","0")
        print "La flag es: CodeCamp19{" + Flag+ "}"
        exit()
    else:
        print("\nEn algo te has equivocado, sigue intentando")
        exit()
else:
    exit()
