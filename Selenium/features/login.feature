Feature: Login en The Internet
  Como usuario quiero hacer login en la aplicación
  para verificar que el flujo funciona correctamente.

  Scenario: Login exitoso con credenciales válidas
    Given el usuario abre la página de login
    When el usuario ingresa el usuario "tomsmith" y la contraseña "SuperSecretPassword!"
    And el usuario hace clic en el botón de login
    Then el usuario ve el mensaje de éxito "You logged into a secure area!"

  Scenario: Login fallido con credenciales inválidas
    Given el usuario abre la página de login
    When el usuario ingresa el usuario "invaliduser" y la contraseña "invalidpass"
    And el usuario hace clic en el botón de login
    Then el usuario ve el mensaje de error "Your username is invalid!"
