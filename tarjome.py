from typing import Dict

def neveshtan():
        new_kalame = ''
        for i in range(len(kalameS)):
                english = kalameS[i]['english']
                farsi = kalameS[i]['farsi']
                new_kalame ='\n'+ english + '\n' + farsi
        file = open('translate.txt' , 'a')
        myfile = file.write(new_kalame)

def kalame_jadid():
        f=0
        english_jadid = input('Lotfan kalame jadid englisi ro vared konid: ')
        for i in range(len(kalameS)):
                if kalameS[i]['english'] == english_jadid :
                        print('kalame vojod darad')
                        f=0
                else:
                        new_kalame_farsi = input('mani kalame ro vared konid: ')
                        dict = {}
                        dict['english'] = english_jadid
                        dict['farsi'] = new_kalame_farsi
                        kalameS.append(dict)
                        neveshtan()
                        break
                if f == 0:
                        break
        
def tarjome_english_farsi():
        jomle_ha = input('kalame : ')
        tarjome_be_farsi = ''
        jomle = jomle_ha.split('.')
        for i in range(len(jomle)):
                kalame = jomle[i].split(' ')
                for z in range(len(kalame)):
                        for j in range(len(kalameS)):
                                if kalameS[j]['english'] == kalame[z]:
                                        if z == len(kalame)-1:
                                                tarjome_be_farsi += kalameS[j]['farsi'] + '.'
                                        else:
                                                tarjome_be_farsi += kalameS[j]['farsi'] + ' '  
        print('Tarjome: ' , tarjome_be_farsi)

def tarjome_farsi_english():
        jomle_ha = input('jomle farsi: ')
        tarjome_be_english = ''
        jomle = jomle_ha.split('.')
        for i in range(len(jomle)):
                kalame = jomle[i].split(' ')
                for z in range(len(kalame)):
                        for j in range(len(kalameS)):
                                if kalameS[j]['farsi'] == kalame[z]:
                                        if z == len(kalame)-1:
                                                tarjome_be_english += kalameS[j]['english'] + '.'
                                        else:
                                                tarjome_be_english += kalameS[j]['english'] + ' '  
        print('tarjome: ' , tarjome_be_english)

def show_menu():
        print('1- kalame jadid')
        print('2- tarjome english be farse ')
        print('3- tarjome farsi be english ')
        print('4- khoroj ')

def afzodan_be_file():
        try:
                file = open('translate.txt' , 'r')
                kalame_haye_man = file.read().split('\n')
                for i in range(len(kalame_haye_man)):
                        #dict = {}
                        if i % 2 == 0:
                                dict = {}
                                dict['english'] = kalame_haye_man[i]
                        else:
                                dict['farsi'] = kalame_haye_man[i]
                                kalameS.append(dict)
        except:
                print('peyda nashod :/ ')        

kalameS = []

while True:
        show_menu()
        afzodan_be_file()
        choice = int(input('entekhab kon: '))
        if choice == 1:
                kalame_jadid()
        elif choice == 2:
                tarjome_english_farsi()
        elif choice == 3:
                tarjome_farsi_english()
        elif choice == 4:
                exit()
        else:
                print('Dobare entehan kon ')