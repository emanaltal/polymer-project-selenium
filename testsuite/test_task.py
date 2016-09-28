from testframework.base import *
import uuid


class TaskTest(BaseTest):

    def test001_task(self):
        """ TestCase-1: Test case for the task.*
        **Test Scenario:**
        #. Go to Men's Outerwear page, should succeed
        #. Verify Men's Outerwear items, should succeed
        #. Go to Ladies Outerwear page, should succeed
        #. Verify Ladies Outerwear items, should succeed
        #. Go to Ladies Outerwear page, should succeed
        #. Add Ladies Colorblock Wind Jacket to the Cart, should succeed
        #. Go to Men's T-Shirt page, should succeed
        #. Add Inbox - Subtle Actions T-shirt to the Cart, should succeed
        #. Checkout The cart by filling in with some fake details and Place order, should succeed                
        """    	
        self.lg('%s STARTED' % self._testID)
        
        self.lg("Go to Men's Outerwear page, should succeed")
        self.click('home_mens_page')
        items = config['mens']
        
        self.lg("Verify Men's Outerwear items, should succeed")
        self.lg("Checking page lable")
        self.get_text('mens_lable', "Men's Outerwear")
        self.lg("Checking page sub-lable")
        self.get_text('mens_sub_lable', "(%s items)" % len(items.keys()))
        self.lg("Checking page url")
        self.assertEqual(self.driver.current_url, 
                         self.environment_url + "/list/mens_outerwear",
                         "Men's page url error [%s]" % self.driver.current_url)
        self.lg("Checking page title")
        self.assertEqual(self.driver.title, 
                         "Men's Outerwear - SHOP",
                         "Men's Outerwear title error [%s]" % self.driver.title)

        self.lg("Checking items pages")
        for item in items.keys():
            item_xpath = self.elements['items'] % item
            self.wait_until_element_located_and_has_text(item_xpath,
                                                         items[item].split(',')[0])
            
            price_xpath = self.elements['prices'] % item
            self.wait_until_element_located_and_has_text(price_xpath,
                                                         items[item].split(',')[1])
            self.click_link(item_xpath)

            self.get_text('item_lable', items[item].split(',')[0])
            self.get_text('item_price', items[item].split(',')[1])
           
            self.assertEqual(self.driver.title, 
                             items[item].split(',')[0] + " - SHOP",
                             "Men's Outerwear title error [%s]" % self.driver.title)

            self.click('home_mens_page')
            self.get_text('mens_lable', "Men's Outerwear")
            self.get_text('mens_sub_lable', "(%s items)" % len(items.keys()))

        self.lg("Go to Ladies Outerwear page, should succeed")
        self.click('home_ladies_page')
        items = config['ladies']
        
        self.lg("Verify Ladies Outerwear items, should succeed")
        self.lg("Checking page lable")
        self.get_text('mens_lable', "Ladies Outerwear")
        self.lg("Checking page sub-lable")
        self.get_text('mens_sub_lable', "(%s items)" % len(items.keys()))
        self.lg("Checking page url")
        self.assertEqual(self.driver.current_url, 
                         self.environment_url + "/list/ladies_outerwear",
                         "Ladies page url error [%s]" % self.driver.current_url)
        self.lg("Checking page title")
        self.assertEqual(self.driver.title, 
                         "Ladies Outerwear - SHOP",
                         "Ladies Outerwear title error [%s]" % self.driver.title)
        
        self.lg("Checking items pages")
        for item in items.keys():
            item_xpath = self.elements['items'] % item
            self.wait_until_element_located_and_has_text(item_xpath,
                                                         items[item].split(',')[0])
            
            price_xpath = self.elements['prices'] % item
            self.wait_until_element_located_and_has_text(price_xpath,
                                                         items[item].split(',')[1])    
            
            self.click_link(item_xpath)

            self.get_text('item_lable', items[item].split(',')[0])
            self.get_text('item_price', items[item].split(',')[1])
            self.assertEqual(self.driver.title, 
                             items[item].split(',')[0] + " - SHOP",
                             "Ladies Outerwear title error [%s]" % self.driver.title)

            self.click('home_ladies_page')
            self.get_text('mens_lable', "Ladies Outerwear")
            self.get_text('mens_sub_lable', "(%s items)" % len(items.keys()))

        self.lg("Go to Ladies Outerwear page, should succeed")
        self.click('home_ladies_page')
        items = config['ladies']
        self.get_text('mens_lable', "Ladies Outerwear")
        self.get_text('mens_sub_lable', "(%s items)" % len(items.keys()))

        self.lg("Add Ladies Colorblock Wind Jacket to the Cart, should succeed")
        ladies_item = ('Ladies Colorblock Wind Jacket', '$45.90')
        item = 2
        item_xpath = self.elements['items'] % item
        self.click_link(item_xpath)
        self.get_text('item_lable', ladies_item[0])
        self.get_text('item_price', ladies_item[1])        
        self.click('add_to_cart')

        self.lg("Go to Men's T-Shirt page, should succeed")
        self.click('home_mens_tshirt_page')  
        self.get_text('mens_lable', "Men's T-Shirts")
        self.get_text('mens_sub_lable', "(40 items)")

        self.lg("Add Inbox - Subtle Actions T-shirt to the Cart, should succeed")
        mens_item = ('Inbox - Subtle Actions T-Shirt', '$17.05')
        self.click_link(item_xpath)
        self.get_text('item_lable', mens_item[0])
        self.get_text('item_price', mens_item[1])     
        self.click('add_to_cart')

        self.lg("Checkout The cart by filling in with some fake details "
                "and Place order, should succeed")
        self.click('view_cart')
        self.get_text('cart_items_number', "2 items")
        self.assertEqual(self.driver.title, 
                         "Your cart - SHOP",
                         "Your cart title error [%s]" % self.driver.title)        
        
        self.lg("Checking cart items")
        collected_items = [ladies_item, mens_item] 
        for i, item in zip([1, 2], collected_items):
            item_xpath = self.elements['cart_items'] % i
            self.wait_until_element_located_and_has_text(item_xpath,
                                                         item[0])  

            price_xpath = self.elements['cart_prices'] % i
            self.wait_until_element_located_and_has_text(price_xpath,
                                                         item[1])         

        total = float(mens_item[1].replace('$', '')) + \
                float(ladies_item[1].replace('$', ''))
        self.get_text('cart_total', '$' + str(total))

        self.lg("Checkout The cart by filling in with some fake details and "
                "Place order, should succeed")
        self.click('checkout')

        fake_str = str(uuid.uuid4()).replace('-', '')[0:10]
        fake_int = 9999
        self.set_text('email', fake_str + '@gmail.com')
        self.set_text('phone', str(fake_int) * 3)
        self.set_text('address', fake_str)
        self.set_text('city', fake_str)
        self.set_text('state', fake_str)
        self.set_text('zip', fake_int)
        self.set_text('name', fake_str)
        self.set_text('number', str(fake_int) * 4)
        self.set_text('cctv', fake_int)

        self.lg("Checking collection items")
        for i, item in zip([4, 5], collected_items):
            item_xpath = self.elements['summery_items'] % i
            self.wait_until_element_located_and_has_text(item_xpath,
                                                         item[0])  

            price_xpath = self.elements['summery_prices'] % i
            self.wait_until_element_located_and_has_text(price_xpath,
                                                         item[1])          

        total_xpath = self.elements['summery_prices'] % (i + 1)
        self.wait_until_element_located_and_has_text(total_xpath,
                                                     '$' + str(total))
        self.click('place_order')

        self.get_text('end_lable', "Thank you")
        self.get_text('end_sub_lable', "Demo checkout process complete.")
        self.assertEqual(self.driver.title, 
                         "Checkout - SHOP",
                         "Checkout title error [%s]" % self.driver.title)

        self.click('finish')

        self.lg('%s ENDED' % self._testID)                        