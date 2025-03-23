from playwright.sync_api import Page, expect
import re

def is_mobile(page:Page):
    escritorio = 1024
    is_mobile = False
    #Si el tamaño de la pantalla es menor a 1024 is_mobile es True
    if(page.viewport_size['width']<escritorio):
        is_mobile = True

    return is_mobile