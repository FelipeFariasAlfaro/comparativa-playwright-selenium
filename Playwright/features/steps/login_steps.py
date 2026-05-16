from behave import given, when, then


@given('el usuario abre la página de login')
def step_open_login_page(context):
    context.page.goto("https://the-internet.herokuapp.com/login")


@when('el usuario ingresa el usuario "{username}" y la contraseña "{password}"')
def step_enter_credentials(context, username, password):
    context.page.fill("#username", username)
    context.page.fill("#password", password)


@when('el usuario hace clic en el botón de login')
def step_click_login(context):
    context.page.click("button[type='submit']")


@then('el usuario ve el mensaje de éxito "{message}"')
def step_verify_success(context, message):
    flash = context.page.inner_text("#flash")
    assert message in flash, f"Esperado: '{message}', Obtenido: '{flash}'"


@then('el usuario ve el mensaje de error "{message}"')
def step_verify_error(context, message):
    flash = context.page.inner_text("#flash")
    assert message in flash, f"Esperado: '{message}', Obtenido: '{flash}'"


@then('el usuario ve el mensaje esperado "{tipo}" con texto "{message}"')
def step_verify_message(context, tipo, message):
    flash = context.page.inner_text("#flash")
    assert message in flash, f"[{tipo}] Esperado: '{message}', Obtenido: '{flash}'"
