@ui @smoke
Feature: Login de usuarios

  Background:
    Given el usuario está en la página de login

  Scenario: Login exitoso con credenciales válidas
    When el usuario ingresa usuario "standard_user" y contraseña "secret_sauce"
    Then el usuario es redirigido al inventario

  @regression
  Scenario: Login con usuario bloqueado
    When el usuario ingresa usuario "locked_out_user" y contraseña "secret_sauce"
    Then se muestra un mensaje de error

  @regression
  Scenario: Login con contraseña incorrecta
    When el usuario ingresa usuario "standard_user" y contraseña "wrong_pass"
    Then se muestra un mensaje de error

  @regression
  Scenario Outline: Login con campos vacíos
    When el usuario ingresa usuario "<usuario>" y contraseña "<password>"
    Then se muestra un mensaje de error

    Examples:
      | usuario | password |
      |         |          |
