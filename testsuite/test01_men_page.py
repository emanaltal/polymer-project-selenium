from testframework.base import *
import time


class MenTests(BaseTest):

    def test001_mens_outerwear_page_items(self):
        """ TestCase-1: Test case for check Men's Outerwear page items.*
        **Test Scenario:**
        #. Go to Men's Outerwear page, should succeed
        #. Verify Men's Outerwear items, should succeed
        """
        self.lg('%s STARTED' % self._testID)
        
        self.lg("Go to Men's Outerwear page, should succeed")
        self.click('home_mens_page')
        time.sleep(10)
        
        self.lg("Verify Men's Outerwear items, should succeed")
        label = self.get_text('mens_lable')
        self.assertEqual(label, 
                         "Men's Outerwear",
                         "Men's Outerwear label error [%s]" % label)
        self.assertEqual(self.driver.current_url, 
                         self.environment_url + "/list/mens_outerwear",
                         "Men's page url error [%s]" % self.driver.current_url)
        self.assertEqual(self.driver.title, 
                         "Men's Outerwear - SHOP",
                         "Men's Outerwear title error [%s]" % self.driver.title)
        sub_label = self.get_text('mens_sub_lable')
        self.assertEqual(sub_label, 
                         "(16 items)",
                         "Men's Outerwear sub label error [%s]" % sub_label)  

        items = {
        1: ("Men's Tech Shell Full-Zip", "$50.20"),
        2: ("Anvil L/S Crew Neck - Grey", "$22.15"),
        3: ("Green Flex Fleece Zip Hoodie", "$45.65"),
        4: ("Android Nylon Packable Jacket", "$33.60"),
        5: ("YouTube Ultimate Hooded Sweatshirt", "$32.35"),
        6: ("Grey Heather Fleece Zip Hoodie", "$38.85"),
        7: ("Vastrm Hoodie", "$200.00"),
        8: ("Recycled Plastic Bottle Hoodie - Green", "$60.95"),
        9: ("Rowan Pullover Hood", "$60.85"),
        10: ("Men's Voyage Fleece Jacket", "$48.00"),
        11: ("Eco-Jersey Chrome Zip Up Hoodie", "$37.75"),
        12: ("Android Colorblock Hooded Pullover", "$50.20"),
        13: ("Tri-blend Full-Zip Hoodie", "$52.20"),
        14: ("Fleece Full-Zip Hoodie", "$45.65"),
        15: ("Jacquard-Knit Full-Zip Fleece", "$74.90"),
        16: ("YouTube Unisex Flex Fleece Zip Hoodie", "$45.25")}
        
        for item in items.keys():
            item_xpath = self.elements['mens_items'] % item
            item_lable = self.get_element_text(item_xpath)
            self.assertEqual(item_lable, 
                             items[item][0],
                             "Men's Outerwear item [%s] label error [%s]" % (items[item][0], 
                                                                             item_lable))
            
            price_xpath = self.elements['mens_prices'] % item
            item_price = self.get_element_text(price_xpath)
            self.assertEqual(item_price, 
                             items[item][1],
                             "Men's Outerwear item [%s] price error [%s]" % (items[item][0], 
                                                                             item_price))      

        self.lg('%s ENDED' % self._testID)
