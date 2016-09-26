# -*- coding: utf-8 -*-
import logging
import os
from base import BaseTest


# Initiate testsuite logger
logger = logging.getLogger('portal_testsuite')
if not os.path.exists('logs/portal_testsuite.log'):os.mkdir('logs')
handler = logging.FileHandler('logs/portal_testsuite.log')
formatter = logging.Formatter('%(asctime)s [%(testid)s] [%(levelname)s] %(message)s',
                              '%d-%m-%Y %H:%M:%S %Z')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

#element paths we use during test
BaseTest.elements = {
'home_mens_page': ".//*[@id='container']/shop-tab[1]/shop-ripple-container/a",
'home_ladies_page': ".//*[@id='container']/shop-tab[2]/shop-ripple-container/a",
'home_mens_tshirt_page': ".//*[@id='container']/shop-tab[3]/shop-ripple-container/a",
'home_ladies_tshirt_page': ".//*[@id='container']/shop-tab[4]/shop-ripple-container/a",
'home_cart': ".//*[@id='icon']",

'mens_lable': "html/body/shop-app/iron-pages/shop-list/header/h1",
'mens_sub_lable': "html/body/shop-app/iron-pages/shop-list/header/span",
'mens_items': "html/body/shop-app/iron-pages/shop-list/ul/li[%d]/a/shop-list-item/div",
'mens_prices': "html/body/shop-app/iron-pages/shop-list/ul/li[%d]/a/shop-list-item/span",
'mens_item_lable': ".//*[@id='content']/div/h1",
'mens_item_price': ".//*[@id='content']/div/div[1]",

'add_to_cart': ".//*[@id='content']/div/shop-button/button",
'checkout': "html/body/shop-app/iron-pages/shop-cart/div/div[2]/div[2]/shop-button/a",
'checkout_items': "html/body/shop-app/iron-pages/shop-cart/div/div[2]/div[1]/shop-cart-item[%d]/div/div[1]/a",

'email': ".//*[@id='accountEmail']",
'phone': ".//*[@id='accountPhone']",
'address': ".//*[@id='shipAddress']",
'city': ".//*[@id='shipCity']",
'state': ".//*[@id='shipState']",
'zip': ".//*[@id='shipZip']",
'name': ".//*[@id='ccName']",
'number': ".//*[@id='ccNumber']",
'cctv': ".//*[@id='ccCVV']",

'place_order': ".//*[@id='submitBox']/input",


}