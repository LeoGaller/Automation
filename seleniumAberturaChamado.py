"""
Created on Mon Aug 27 10:22:24 2018

@author: Leonardo.Galler
"""
import time
import getpass
import geradorTextoGri_deploy_selenium as fun1
from selenium import webdriver

# Creating the text to deploy
text = fun1.generateText()

driver = webdriver.Chrome('C:/Users/leonardo.galler/Documents/WebDriver/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://atendimento.sicoob.com.br/tas/public/login/form')
time.sleep(3) # Let the user actually see something!

# Acessando a pagina
username = driver.find_element_by_id("loginname")
password = driver.find_element_by_id("password")

# Fazendo login
print("Entre com usuário e senha para o sistema de chamado.")
username.send_keys(input("Usuário: "))
password.send_keys(getpass.getpass("Senha: "))

driver.find_element_by_id("login").click()

time.sleep(3) # Let the user actually see something!
# Entra na diretoria
print('--> Tecnologia\n')
while True:
    try:
        driver.find_element_by_link_text("Tecnologia").click()
        time.sleep(3) # Let the user actually see something!
        
        break
    except:
        print('*** Página ainda carregando!\n')
        time.sleep(3)
        
#Entra na area
print('--> Área Operações de TI\n')
while True:
    try:
        driver.find_element_by_partial_link_text("de TI").click()
        time.sleep(3) # Let the user actually see something!
        
        # If its ok, break
        break
    except:
        print('*** Página ainda carregando!\n')
        time.sleep(3)
#
print('--> Suporte interno\n')
while True:
    try:
        driver.find_element_by_link_text("Suporte Interno").click()
        time.sleep(3) # Let the user actually see something!
        
        break
    except:
        print('*** Página ainda carregando!\n')
        time.sleep(3)
# 
print('--> Softwares\n')
while True:
    try:
        driver.find_element_by_link_text("Softwares").click()
        time.sleep(3) # Let the user actually see something!
        
        break
    except:
        print('*** Página ainda carregando!\n')
        time.sleep(3)
        
#
print('--> Cognos\n')
while True:
    try:
        driver.find_element_by_link_text("COGNOS").click()
        time.sleep(3) # Let the user actually see something!
        
        break
    except:
        print('*** Página ainda carregando!\n')
        time.sleep(3)
#
print('--> Abertura de chamado\n')
while True:
    try:
        driver.find_element_by_link_text("Abertura de Chamado").click()
        time.sleep(3) # Let the user actually see something!
        
        break
    except:
        print('*** Página ainda carregando!\n')
        time.sleep(3)
#
print('--> Preenchendo detalhes do chamado!')

## Finding the field element
element1 = driver.find_element_by_id('ssp-form-parent')
time.sleep(2)

# Finding the IFrame
iframe = element1.find_elements_by_class_name('form-frame')[0]
time.sleep(2)
driver.switch_to_frame(iframe)

# Testing to know if we are inside the iframe
form2 = driver.find_element_by_class_name('xfgForm')
time.sleep(2)

# Browsing through the fieldsets
fieldset = form2.find_element_by_id('ssdform6b3b18c3dc394aaa86187bffb0a2d9c2_selection1')
time.sleep(2)

# looking for the input selector
radio = fieldset.find_element_by_class_name('input')

# clicking the 'Adicionar button'
radio.find_element_by_class_name('option').click()

# Finding the 'Assunto' text box
assuntoTextBox = form2.find_element_by_id('ssdform6b3b18c3dc394aaa86187bffb0a2d9c2_description')
time.sleep(2)

# Defining the environment
# Find the part of text where the date begins


envText = text[text.find('2019')+13:text.find('2019')+16]

if(envText == 'PRD'):
    envText = 'PRODUÇÃO'
elif(envText == 'HML'):
    envText = 'HOMOLOGAÇÃO'    

# Filling the 'Assunto' text box
textBox = assuntoTextBox.find_element_by_tag_name('input')
textBox.send_keys('Deploy '+envText+' Cognos')
time.sleep(2)

# Browsing through the fieldsets
textBox = form2.find_element_by_id('ssdform6b3b18c3dc394aaa86187bffb0a2d9c2_openquestion2_openquestion_openquestion')
textBox.send_keys(text)
time.sleep(2)

searchBox = form2.find_element_by_id('ssdform6b3b18c3dc394aaa86187bffb0a2d9c2_impact_impact_impact')
searchBox.send_keys('Meu Departamento Inteiro')
time.sleep(2)

# Sending
i = 1
while True:
    try:
        form2.find_element_by_id('button_submit').click()
        break
    except:
        print('*** Botão não encontrado, aguardando para buscar novamente!\n')
        time.sleep(3)
    i+= 1
    if(i == 10):
        print("Máximo de tentativas de envio alcançadas. Envie o chamado manualmente.")
        break
    else:
        continue

print('\nChamado Enviado!')

while True:
    try:
        nrCham = driver.find_element_by_class_name('backLinkDiv')
        break
    except:
        print('*** Página ainda carregando!')

nrCham.find_element_by_tag_name('a')

print("Verifique o email de confirmação!")
time.sleep(6)
driver.quit()
# =============================================================================