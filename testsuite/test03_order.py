from testframework.base import *
import time
import uuid


class OrderTests(BaseTest):

    def test001_order_and_checkout(self):
        """ TestCase-3: Test case for order and checkout.*
        **Test Scenario:**
        #. Go to Ladies Outerwear page, should succeed
        #. Add Ladies Colorblock Wind Jacket to the Cart, should succeed
        #. Go to Men's T-Shirt page, should succeed
        #. Add Inbox - Subtle Actions T-shirt to the Cart, should succeed
        #. Checkout The cart by filling in with some fake details and Place order, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        
        self.lg("Go to Ladies Outerwear page, should succeed")
        self.click('home_ladies_page')
        time.sleep(10)

        self.lg("Add Ladies Colorblock Wind Jacket to the Cart, should succeed")
        item = 2
        item_xpath = self.elements['mens_items'] % item
        self.click_element(item_xpath)
        time.sleep(5)
        self.click('add_to_cart')

        self.lg("Go to Men's T-Shirt page, should succeed")
        self.click('home_mens_tshirt_page')
        time.sleep(30)        

        self.lg("Add Inbox - Subtle Actions T-shirt to the Cart, should succeed")
        self.click_element(item_xpath)
        time.sleep(5)
        self.click('add_to_cart')

        self.lg("Checkout The cart by filling in with some fake details "
                "and Place order, should succeed")
        self.click('home_cart')
        #check items
        self.click('checkout')
        #fill
        fake_str = str(uuid.uuid4()).replace('-', '')[0:10]
        fake_int = 9999
        self.set_text('email', fake_str)
        self.set_text('phone', fake_int)
        self.set_text('address', fake_str)
        self.set_text('city', fake_str)
        self.set_text('state', fake_str)
        self.set_text('zip', fake_int)
        self.set_text('name', fake_str)
        self.set_text('number', fake_int)
        self.set_text('cctv', fake_int)

        #check summery
        self.click('checkout')

        self.lg('%s ENDED' % self._testID)