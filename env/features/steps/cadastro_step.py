
from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import os

@given(u'que eu estou na página de cadastro de produto')
def step_impl(context):
    context.browser = Firefox()
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
    input_email = context.browser.find_element(By.ID,'mui-1').send_keys('l7u7c7@gmail.com')
    input_password = context.browser.find_element(By.NAME,'password').send_keys('123456789')
    button_submit = context.browser.find_element(By.XPATH, '/html/body/div/main/form/button').submit()


@given(u'eu aperto no botão "+ Adicionar"')
def step_adicionar(context):
    time.sleep(3)
    button_adicionar = context.browser.find_element(By.XPATH, '/html/body/div/header/section[2]/div/header/button').click()

@when(u'eu preencher o formulário com os dados do produto')
def step_impl(context):
    input_name = context.browser.find_element(By.NAME, 'name').send_keys('camiseta')
    input_description = context.browser.find_element(By.NAME, 'description').send_keys('Camiseta de algodão com proteção UV')
    input_category = context.browser.find_element(By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[1]').click()
    input_price = context.browser.find_element(By.NAME, 'price').send_keys('300,00')
    input_shipment = context.browser.find_element(By.NAME,'shipment').send_keys("30,00")
    # input_image = context.browser.find_element(By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/div[5]/div/div').click()

    # image_path = os.path.abspath('C:\\Users\\Lilian\\project\\env\\features\\images\\cami.png')  
    # WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.ID, 'mui-5'))).send_keys(image_path)
    context.browser.find_element(By.XPATH, '//*[@id="mui-5"]').send_keys('C:\\Users\\Lilian\\project\\env\\features\\images\\calças2.jpg')
   
    time.sleep(2)
   

@when(u'apertar no botão de "ENVIAR NOVO PRODUTO"')
def step_buttom(context):
    button_submit = context.browser.find_element(By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/button').submit()
    
@then(u'eu devo ver a mensagem de sucesso "Produto cadastrado com sucesso"')
def step_impl(context):
    time.sleep(2)
    success_message = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="status" and contains(text(), "Produto enviado com sucesso")]'))
    )
    
    # Verifica se a mensagem de sucesso está presente
    assert success_message is not None, "Mensagem de sucesso não encontrada"

    # Verifica se a mensagem ainda está presente (espera 2 segundos e verifica novamente)
    time.sleep(2)
    still_present = len(context.browser.find_elements(By.XPATH, '//div[@role="status" and contains(text(), "Produto enviado com sucesso")]')) > 0
    
    # Mensagem desapareceu após aparecer rapidamente
    assert not still_present, "Mensagem de sucesso desapareceu rapidamente, mas foi capturada"
    
    context.browser.quit()
   