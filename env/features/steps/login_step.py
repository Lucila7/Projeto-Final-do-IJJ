from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'que eu estou na página do Instituto')
def step_login(context):
    context.browser = Firefox()
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')

@when(u'eu preencher os campos de login, já tendo um cadastro')
def step_data(context):
    input_email = context.browser.find_element(By.ID,'mui-1').send_keys('l7u7c7@gmail.com')
    input_password = context.browser.find_element(By.NAME,'password').send_keys('123456789')
    
@when(u'apertar o botão \'Iniciar sessão\'')
def step_buttom(context):
    button_submit = context.browser.find_element(By.XPATH, '/html/body/div/main/form/button').submit()
    import time; time.sleep(3)
    
@then(u'a tela de cadastro de produtos é mostrada.')
def step_end(context):    
    context.browser.quit()

#<div role="status" aria-live="polite" class="go3958317564">logado com sucesso</div>

# @then(u'eu devo logar com sucesso')
# def step_impl(context):
#     div_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='status' and @aria-live='polite']"))
# )

# # Verifica se a mensagem de sucesso está presente no texto do elemento
#     assert "logado com sucesso" in div_element.text
#     wait = WebDriverWait(context.browser, 10)
#     alert = context.browser.find_element(By.CLASS_NAME, 'go3958317564')
#     # alert = wait.until(EC.visibility_of_element_located(By.CLASS_NAME, 'go3958317564'))
#     # alert = wait.until(EC.alert_is_present())
#     # alert = wait.until(EC.visibility_of_element_located(By.XPATH,'/html/body/div/header/div[1]/div/div/div[2]'))
#     print(alert.text)
    # assert 'logado com sucesso' in alert.text, "Falha ao logar"
   
    # context.browser.quit()

@given(u'que eu estou logado na página do Instituto')
def step_impl(context):
    context.browser = Firefox()
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
    input_email = context.browser.find_element(By.ID,'mui-1').send_keys('l7u7c7@gmail.com')
    input_password = context.browser.find_element(By.NAME,'password').send_keys('123456789')
    button_submit = context.browser.find_element(By.XPATH, '/html/body/div/main/form/button').submit()
    

@when(u'clicar em \'Perfil\'')
def step_impl(context):
   
    button = WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="radix-7-trigger-radix-0"]')))
    context.browser.execute_script("arguments[0].click();", button)
    

@when(u'em \'LogOut\'')
# def step_impl(context):
#     # Espera até que o item "LogOut" esteja visível no dropdown
#     logout_button = WebDriverWait(context.browser, 30).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "LogOut") or contains(text(), "Sair")]')))
#     ActionChains(context.browser).move_to_element(logout_button).click().perform()
def step_impl(context):
    try:
        # Verifique se o botão está dentro de um iframe
        if context.browser.find_elements(By.TAG_NAME, 'iframe'):
            context.browser.switch_to.frame(context.browser.find_element(By.TAG_NAME, 'iframe'))

        # Espera até que o item "LogOut" esteja visível e interativo
        logout_button = WebDriverWait(context.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "LogOut") or contains(text(), "Sair")]'))
        )
        
        # Usa ActionChains para mover para o elemento e clicar
        actions = ActionChains(context.browser)
        actions.move_to_element(logout_button).click().perform()

    except Exception as e:
        print(f"Erro ao clicar em 'LogOut': {e}")
        # Captura uma imagem para ajudar no debugging
        context.browser.save_screenshot('screenshot.png')
        # Tenta novamente após esperar um curto período
        time.sleep(3)
        logout_button = WebDriverWait(context.browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "LogOut") or contains(text(), "Sair")]'))
        )
        actions = ActionChains(context.browser)
        actions.move_to_element(logout_button).click().perform()  

@then(u'retorno para a página inicial do Insituto')
def step_impl(context):
    pass