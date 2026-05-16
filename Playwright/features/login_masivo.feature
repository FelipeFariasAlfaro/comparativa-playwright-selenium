Feature: Login masivo - Scenario Outline con 30 casuísticas
  Prueba de carga para comparativa de velocidad ejecutando
  múltiples combinaciones de credenciales.

  Scenario Outline: Intento de login con diferentes credenciales
    Given el usuario abre la página de login
    When el usuario ingresa el usuario "<username>" y la contraseña "<password>"
    And el usuario hace clic en el botón de login
    Then el usuario ve el mensaje esperado "<tipo>" con texto "<mensaje>"

    Examples: Credenciales válidas
      | username | password              | tipo   | mensaje                          |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |
      | tomsmith | SuperSecretPassword!  | exito  | You logged into a secure area!   |

    Examples: Credenciales con usuario inválido
      | username      | password              | tipo  | mensaje                      |
      | invalid1      | SuperSecretPassword!  | error | Your username is invalid!    |
      | wronguser     | SuperSecretPassword!  | error | Your username is invalid!    |
      | admin         | SuperSecretPassword!  | error | Your username is invalid!    |
      | test          | SuperSecretPassword!  | error | Your username is invalid!    |
      | user123       | SuperSecretPassword!  | error | Your username is invalid!    |
      | nobody        | SuperSecretPassword!  | error | Your username is invalid!    |
      | fake_user     | SuperSecretPassword!  | error | Your username is invalid!    |
      | random        | SuperSecretPassword!  | error | Your username is invalid!    |
      | hacker        | SuperSecretPassword!  | error | Your username is invalid!    |
      | guest         | SuperSecretPassword!  | error | Your username is invalid!    |

    Examples: Credenciales con contraseña inválida
      | username | password       | tipo  | mensaje                        |
      | tomsmith | wrongpass      | error | Your password is invalid!      |
      | tomsmith | 123456         | error | Your password is invalid!      |
      | tomsmith | password       | error | Your password is invalid!      |
      | tomsmith | qwerty         | error | Your password is invalid!      |
      | tomsmith | letmein        | error | Your password is invalid!      |
      | tomsmith | abc123         | error | Your password is invalid!      |
      | tomsmith | monkey         | error | Your password is invalid!      |
      | tomsmith | dragon         | error | Your password is invalid!      |
      | tomsmith | master         | error | Your password is invalid!      |
      | tomsmith | trustno1       | error | Your password is invalid!      |
