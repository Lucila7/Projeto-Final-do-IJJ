from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time

faker = Faker()

@given(u'eu clico em \'Clique aqui e registre-se\'')
def step_impl(context):
    time.sleep(5)
    create_user = context.browser.find_element(By.CLASS_NAME, 'register').click()

@when(u'eu preencho os campos com os dados')
def step_impl(context):
    email = faker.email()
    input_email = context.browser.find_element(By.NAME, 'email').send_keys(email)

    password = faker.password()
    input_password = context.browser.find_element(By.NAME, 'password').send_keys(password)
    input_password = context.browser.find_element(By.NAME, 'confirmPassword').send_keys(password)
    time.sleep(3)
@when(u'clicar em \'Criar conta\'')
def step_impl(context):
    buttom = context.browser.find_element(By.XPATH, '/html/body/div/div/form/button').submit()

@then(u'será exibido \'Usuário cadastrado com sucesso\'')
def step_impl(context):
    
    element = WebDriverWait(context.browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Usuário cadastrado com sucesso')]")))   
    assert "Usuário cadastrado com sucesso" in element.text

    context.browser.quit()