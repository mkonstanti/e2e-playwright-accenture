from playwright.sync_api import Page, expect

def test_send_form_with_invalid_email(page:Page):
    print("Given user visit contact page")
    page.goto("https://www.accenture.com/es-es/about/contact-us")
    print("And user accepts the cookies")
    page.get_by_text("Aceptar todas las Cookies.", exact = True).click()
    page.wait_for_url("https://www.accenture.com/es-es/about/contact-us")

    print("When user opens contact form")
    page.get_by_text("Envíe una pregunta").click()

    print("And user fills name")
    page.get_by_role("textbox", name="* Nombre").click()
    page.get_by_role("textbox", name="* Nombre").fill("Maria")

    print("And user fills surname")
    page.get_by_role("textbox", name="* Apellido").click()
    page.get_by_role("textbox", name="* Apellido").fill("Konstantinidou")

    print("And user fills email with invalid email address")
    page.get_by_role("textbox", name="* Email").click()
    page.get_by_role("textbox", name="* Email").fill("testemail.com")

    print("And user fills company")
    page.get_by_role("textbox", name="* Compañía/Organización").click()
    page.get_by_role("textbox", name="* Compañía/Organización").fill("Testing company")

    print("And user selects relation with Accenture")
    page.get_by_role("combobox", name="* Relación con Accenture").click()
    page.get_by_role("option", name="Other").click()

    print("And user selects country Spain")
    page.get_by_role("combobox", name="* País/Región required").click()
    page.get_by_role("option", name="Spain").click()

    print("And user fills comment field")
    page.get_by_role("textbox", name="* Comentarios").click()
    page.get_by_role("textbox", name="* Comentarios").fill("Test comment")

    print("And user gives consent")
    page.get_by_role("group", name="* Accenture’s Privacy").locator("span").nth(3).click()

    print("Then the user should see error message for invalid email and send button is disabled")
    expect(page.get_by_text("Invalid email address. Please enter a different email address. Only letters, numbers, and non-consecutive dash ( - ), underscore ( _ ), and/or period ( . ) are allowed.")).to_be_visible()
    expect(page.get_by_role("button", name="ENVIAR")).to_be_disabled


def test_send_form_with_empty_email(page:Page):
    print("Given user visit contact page")
    page.goto("https://www.accenture.com/es-es/about/contact-us")
    print("And user accepts the cookies")
    page.get_by_text("Aceptar todas las Cookies.", exact = True).click()
    page.wait_for_url("https://www.accenture.com/es-es/about/contact-us")

    print("When user opens contact form")
    page.get_by_text("Envíe una pregunta").click()

    print("And user fills name")
    page.get_by_role("textbox", name="* Nombre").click()
    page.get_by_role("textbox", name="* Nombre").fill("Maria")

    print("And user fills surname")
    page.get_by_role("textbox", name="* Apellido").click()
    page.get_by_role("textbox", name="* Apellido").fill("Konstantinidou")

    print("And user fills company")
    page.get_by_role("textbox", name="* Compañía/Organización").click()
    page.get_by_role("textbox", name="* Compañía/Organización").fill("Testing company")

    print("And user selects relation with Accenture")
    page.get_by_role("combobox", name="* Relación con Accenture").click()
    page.get_by_role("option", name="Other").click()

    print("And user selects country Spain")
    page.get_by_role("combobox", name="* País/Región required").click()
    page.get_by_role("option", name="Spain").click()

    print("And user fills comment field")
    page.get_by_role("textbox", name="* Comentarios").click()
    page.get_by_role("textbox", name="* Comentarios").fill("Test comment")

    print("And user gives consent")
    page.get_by_role("group", name="* Accenture’s Privacy").locator("span").nth(3).click()

    print("And user clicks on ENVIAR button")
    page.get_by_role("button", name="ENVIAR").click()

    print("Then the user should see error message for empty email and no captcha")
    expect(page.get_by_text("Email field is required and cannot be empty")).to_be_visible()
    expect(page.get_by_text("Please verify that you are not a robot.")).to_be_visible()

def test_send_form_with_no_comment(page:Page):
    print("Given user visit contact page")
    page.goto("https://www.accenture.com/es-es/about/contact-us")
    print("And user accepts the cookies")
    page.get_by_text("Aceptar todas las Cookies.", exact = True).click()
    page.wait_for_url("https://www.accenture.com/es-es/about/contact-us")

    print("When user opens contact form")
    page.get_by_text("Envíe una pregunta").click()

    print("And user fills name")
    page.get_by_role("textbox", name="* Nombre").click()
    page.get_by_role("textbox", name="* Nombre").fill("Maria")

    print("And user fills surname")
    page.get_by_role("textbox", name="* Apellido").click()
    page.get_by_role("textbox", name="* Apellido").fill("Konstantinidou")

    print("And user fills email")
    page.get_by_role("textbox", name="* Email").click()
    page.get_by_role("textbox", name="* Email").fill("test@email.com")

    print("And user fills company")
    page.get_by_role("textbox", name="* Compañía/Organización").click()
    page.get_by_role("textbox", name="* Compañía/Organización").fill("Testing company")

    print("And user selects relation with Accenture")
    page.get_by_role("combobox", name="* Relación con Accenture").click()
    page.get_by_role("option", name="Other").click()

    print("And user selects country Spain")
    page.get_by_role("combobox", name="* País/Región required").click()
    page.get_by_role("option", name="Spain").click()

    print("And user gives consent")
    page.get_by_role("group", name="* Accenture’s Privacy").locator("span").nth(3).click()

    print("And user clicks on ENVIAR button")
    page.get_by_role("button", name="ENVIAR").click()

    print("Then the user should see error message for empty comment and no captcha")
    expect(page.get_by_text("Comments field is required and cannot be empty")).to_be_visible()
    expect(page.get_by_text("Please verify that you are not a robot.")).to_be_visible()