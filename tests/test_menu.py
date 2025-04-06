from playwright.sync_api import Page, expect
import re
import utils

def test_visit_menu_links(page:Page):
    print("Given the user visits homepage accenture")
    #Navegación, abrir la url en el navegador
    page.goto("https://www.accenture.com/es-es")

    print("When the user accepts the cookies")
    #Localizamos el elemento por texto.
    page.get_by_text("Aceptar todas las Cookies.", exact = True).click()
    page.wait_for_url("https://www.accenture.com/es-es")

    print("And clicks on Servicios menu button")
    if(utils.is_mobile(page)):
        page.get_by_role("button", name="menu", exact=True).click()
        page.get_by_role("button", name="Servicios", exact=True).click()
        page.locator("button.rad-global-nav__l2-button", has_text="Servicios").click()
    else:
        page.get_by_role("button", name="Servicios", exact=True).click()
    #Localizamos el elemento de la categoria por rol (button, link, heading) y por texto exacto
    
    print("And clicks on Automation link in Servicios submenu")
    page.get_by_role("link", name="Automation", exact=True).click()

    print("Then user should be on Automation page")
    #Comprobamos que la url de la pagina contiene la url exacta
    expect(page).to_have_url("https://www.accenture.com/es-es/services/intelligent-automation-index")
    #Comprobamos que la url de la pagina contiene la palabra automation
    expect(page).to_have_url(re.compile("automation"))
    #Comprueba que el titulo de la pagina tiene el texto exacto Intelligent Business Process Automation Services | Accenture
    expect(page).to_have_title("Intelligent Business Process Automation Services | Accenture")
    #Localizamos el elemento con titulo heading (h1) que tenga el texto exacto Intelligent Automation
    expect(page.get_by_role("Intelligent Automation", name="", exact=True)).to_be_visible

    #Volvemos a la homepage para hacer click al siguiente link
    page.goto("https://www.accenture.com/es-es")
    print("And clicks on Quiénes somos menu button")
    if(utils.is_mobile(page)):
        page.get_by_role("button", name="menu", exact=True).click()
        page.get_by_role("button", name="Quiénes somos", exact=True).click()
        page.locator("button.rad-global-nav__l2-button", has_text="Quiénes somos").click()
    else:
        page.get_by_role("button", name="Quiénes somos", exact=True).click()
    print("And clicks on Quiénes somos link in Quiénes somos submenu")
    page.get_by_role("link", name="Quiénes somos", exact=True).click()
    
    print("Then user should be on Quiénes somos page")
    expect(page).to_have_url("https://www.accenture.com/es-es/about/company-index")
    expect(page).to_have_title("Sobre nuestra empresa | Accenture")
    expect(page.get_by_role("Nuestro propósito:", name="", exact=True)).to_be_visible

    #Volvemos a la homepage para hacer click al siguiente link
    page.goto("https://www.accenture.com/es-es")
    print("And clicks on Incorpórate menu button")
    if(utils.is_mobile(page)):
        page.get_by_role("button", name="menu", exact=True).click()
        page.get_by_role("button", name="Incorpórate", exact=True).click()
        page.locator("button.rad-global-nav__l2-button", has_text="Únete a nuestro equipo").click()
    else:
        page.get_by_role("button", name="Incorpórate", exact=True).click()

    print("And clicks on Buscador de ofertas link in Incorpórate submenu")
    page.get_by_role("link", name="Buscador de ofertas", exact=True).click()

    print("Then user should be on Buscador de ofertas page")
    expect(page).to_have_url("https://www.accenture.com/es-es/careers/jobsearch?jk=&sb=1&vw=0&is_rj=0&pg=1")
    expect(page).to_have_title("Search Jobs | Accenture")
    expect(page.get_by_role("Busca ofertas en Accenture", name="", exact=True)).to_be_visible