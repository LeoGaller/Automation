'''
Text generator for GRI
Author: Leonardo Galler

Date:10/08/2017 11:15
Vs: 0.1

Updates:
Date:16/07/2018 12:16
Vs: 0.2
What: Removing the necessity to press enter to close the program

Date: 07/02/2019
What: Updating contact data
'''

#Importing the function that creates the name of the package
import packageNameGenerator as png
import datetime, time, os

def generateText():
#defining control variables
    pkg_name = png.package_name()

    #Defining the environment of deploy based on the name of the package
    #capturing the environment tag
    env = pkg_name[13:16].strip()
    
    #defining the environment
    
    while True:
        if(env != 'PRD' and env != 'HML'):
            countToBreak = countToBreak + 1
            print('O ambiente digitado '+ env +' não existe, refaça a operação.')
            print('')
            if(countToBreak == 5):
                print('Numero máximo de repetições alcançado, reinicie a operação.')
                print('')
                break
            else:
                continue
        else:
            break


    #generating the name of the file
    today2 = time.strftime('%d%m%Y')
    
    #Defining the objective of the deploy
    print('')
    objectives = input('Objetivo do deploy: ')
    
    #Defining salutation
    now = datetime.datetime.now()
    if (now.time() >= datetime.time(12) and now.time() < datetime.time(18)):
        salutation = 'Boa tarde'
    elif(now.time() >= datetime.time(18)):
        salutation = 'Boa noite'
    else:
        salutation = 'Bom dia'
        
    #defining text of environment
    if(env == 'PRD'):
        environment = 'PRODUÇÃO'
        env_homol = 'HOMOLOGAÇÃO e PRODUÇÃO'
    elif(env == 'HML'):
        environment = 'HOMOLOGAÇÃO'
        env_homol = 'HOMOLOGAÇÃO'
    
    print('')
    print('Gerando texto para deploy! \n')
    
    text = ''
    text += salutation+'!\n'+'\n'+'Solicito aplicar no COGNOS de '+env_homol+' o arquivo para deploy '+pkg_name+'.zip . \n'
    text +=('Objetivo deste deploy: \n')
    text +=('Subir para '+env_homol+' '+objectives+'.\n\n')
    text +=('Att. \nLeonardo Galler \nGESIC I - Ramal 5857')
    
    return text