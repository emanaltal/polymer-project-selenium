from testframework.base import *
import time


class LadiesTests(BaseTest):

    def test001_ladies_outerwear_page_items(self):
        """ TestCase-2: Test case for check Ladies Outerwear page items.*
        **Test Scenario:**
        #. Go to Ladies Outerwear page, should succeed
        #. Verify Ladies Outerwear items, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        
        self.lg("Go to Ladies Outerwear page, should succeed")
        self.click('home_ladies_page')
        time.sleep(10)
        
        self.lg("Verify Ladies Outerwear items, should succeed")
        label = self.get_text('mens_lable')
        self.assertEqual(label, 
                         "Ladies Outerwear",
                         "Ladies Outerwear label error [%s]" % label)
        self.assertEqual(self.driver.current_url, 
                         self.environment_url + "/list/ladies_outerwear",
                         "Ladies page url error [%s]" % self.driver.current_url)
        self.assertEqual(self.driver.title, 
                         "Ladies Outerwear - SHOP",
                         "Ladies Outerwear title error [%s]" % self.driver.title)
        
        sub_label = self.get_text('mens_sub_lable')
        self.assertEqual(sub_label, 
                         "(6 items)",
                         "Ladies Outerwear sub label error [%s]" % sub_label)  

        items = {
        1: ("Ladies Modern Stretch Full Zip", "$41.60"),
        2: ("Ladies Colorblock Wind Jacket", "$45.90"),
        3: ("Ladies Voyage Fleece Jacket", "$48.00"),
        4: ("Ladies Pullover L/S Hood", "$36.50"),
        5: ("Ladies Sonoma Hybrid Knit Jacket", "$84.85"),
        6: ("Ladies Yerba Knit Quarter Zip", "$64.20")}
        
        for item in items.keys():
            item_xpath = self.elements['mens_items'] % item
            item_lable = self.get_element_text(item_xpath)
            self.assertEqual(item_lable, 
                             items[item][0],
                             "Ladies Outerwear item [%s] label error [%s]" % (items[item][0], 
                                                                             item_lable))
            
            price_xpath = self.elements['mens_prices'] % item
            item_price = self.get_element_text(price_xpath)
            self.assertEqual(item_price, 
                             items[item][1],
                             "Ladies Outerwear item [%s] price error [%s]" % (items[item][0], 
                                                                             item_price))      
            
            self.click_element(item_xpath)

            label = self.get_text('mens_item_lable')
            self.assertEqual(label, 
                             items[item][0],
                             "Ladies Outerwear item [%s] label error [%s]" % (items[item][0], 
                                                                             item_lable))

            self.assertEqual(self.driver.title, 
                             items[item][0] + " - SHOP",
                             "Ladies Outerwear title error [%s]" % self.driver.title)

            sub_label = self.get_text('mens_item_price')
            self.assertEqual(sub_label, 
                             items[item][1],
                             "Ladies Outerwear item [%s] price error [%s]" % (items[item][0], 
                                                                             item_price))            
            
            self.click('home_ladies_page')
            time.sleep(5)
            label = self.get_text('mens_lable')
            self.assertEqual(label, 
                             "Ladies Outerwear",
                             "Ladies Outerwear label error [%s]" % label)
            
        self.lg('%s ENDED' % self._testID)
