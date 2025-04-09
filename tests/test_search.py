from playwright.sync_api import Page, expect
import os

def test_search_empty(page:Page):
    print("Given the user visit search page")
    #Navegación, abrir la url en el navegador
    page.goto("https://www.accenture.com/es-es/search/results")

    print("And user accepts the cookies")
    if os.getenv("GITHUB_ACTIONS") == "true":
        # En GITHUB ACTIONS: cerrar el banner usando el aria-label
        page.get_by_role("button", name="Cerrar").click()
    else:
        # En local: aceptar cookies por texto exacto
        page.get_by_text("Aceptar todas las Cookies.", exact=True).click()
    print("And the user searches with empty value")
    page.get_by_placeholder("Type to search...", exact=True).click()
    page.get_by_placeholder("Type to search...", exact=True).press("Enter")

    print("Then user gets no results for empty value")
    expect(page.get_by_role("heading",name="No results for \"\"")).to_be_visible()

def test_search_valid_value(page:Page):
    print("Given the user visit search page")
    #Navegación, abrir la url en el navegador
    page.goto("https://www.accenture.com/es-es/search/results")

    print("And user accepts the cookies")
    if os.getenv("GITHUB_ACTIONS") == "true":
        # En GITHUB ACTIONS: cerrar el banner usando el aria-label
        page.get_by_role("button", name="Cerrar").click()
    else:
        # En local: aceptar cookies por texto exacto
        page.get_by_text("Aceptar todas las Cookies.", exact=True).click()
    print("And the user searches with empty value")
    page.get_by_placeholder("Type to search...", exact=True).click()
    page.get_by_placeholder("Type to search...", exact=True).fill("contact")
    page.get_by_placeholder("Type to search...", exact=True).press("Enter")

    print("Then user gets results for valid value")
    expect(page.get_by_role("heading", name="Resultados para \"contact\"")).to_be_visible()