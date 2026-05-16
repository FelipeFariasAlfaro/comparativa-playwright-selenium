from behave import given, when, then
from selenium.webdriver.common.by import By


@given('el usuario abre la página de login')
def step_open_login_page(context):
    context.driver.get("https://the-internet.herokuapp.com/login")


@when('el usuario ingresa el usuario "{username}" y la contraseña "{password}"')
def step_enter_credentials(context, username, password):
    context.driver.find_element(By.ID, "username").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)


@when('el usuario hace clic en el botón de login')
def step_click_login(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


@then('el usuario ve el mensaje de éxito "{message}"')
def step_verify_success(context, message):
    flash = context.driver.find_element(By.ID, "flash").text
    assert message in flash, f"Esperado: '{message}', Obtenido: '{flash}'"


@then('el usuario ve el mensaje de error "{message}"')
def step_verify_error(context, message):
    flash = context.driver.find_element(By.ID, "flash").text
    assert message in flash, f"Esperado: '{message}', Obtenido: '{flash}'"


@then('el usuario ve el mensaje esperado "{tipo}" con texto "{message}"')
def step_verify_message(context, tipo, message):
    flash = context.driver.find_element(By.ID, "flash").text
    assert message in flash, f"[{tipo}] Esperado: '{message}', Obtenido: '{flash}'"
