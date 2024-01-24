from database import WWGSDataScraper

#test_dict = {'Product Name': 'SkyTrak Personal Launch Monitor w/ Basic Practice Range Package', 'Product Information': 'key_information: SkyTrak Personal Launch Monitor w/ Basic Practice Range Package Golf’s first portable and affordable Launch Monitor and Golf Simulator The first personal launch monitor of its kind, SkyTrak Personal Launch Monitor is a realistic and real-time golf practice and play system. Keep your golf game sharp with a SkyTrak Launch Monitor and Golf Simulator. This compact, portable unit wirelessly connects to your compatible device and provides immediate shot launch data and ball flight visual feedback as soon as you hit the ball. SkyTrak accurately measures ball speed, launch angle, back spin, club speed, side spin and side angle and displays carry distance, offline and total distance to simulate practice and play as if you were on the course or practice tee. Now integrated with four different Golf Course Simulation Partners: World Golf Tour, TruGolf E6, Jack Nicklaus Perfect Golf and The Golf Club Game. Each functionality allows users to play at some of the world’s top golf courses, all from the comfort of home. Golf Course Simulation Partners require an additional fee on top of the SkyTrak Game Improvement Software Package. Open up a new world of game improving practice and hours of entertaining away from the course. SkyTrak App Features included:  Launch monitor and golf simulator combination designed to act as a game improvement tool while you practice or play virtual golf High-speed photography captures the golf ball and provides an accurate reading with measurable parameters that include ball speed, distance (carry and total), launch angle, club speed, spin rates and more Driving Range functionality allows golfers to practice on a virtual driving range with real-time data and accuracy with instant 3D visualization of the ball flight Simulator wirelessly connects to compatible device and displays data as soon as you hit the ball Built-in rechargeable lithium-ion battery last up to 5 hours of continuous use SkyTrak measures 5.75” x 6.75” x 2.5” and weighs approximately 1.7lbs SkyTrak requires compatible hardware and 3D graphics support (please see below for more details)  In the Box:  SkyTrak Unit SkyTrak Companion App USB Charging Cable   Hardware Compatibility iOS: SkyTrak requires 3D graphics support. The following passed compatibility testing with the latest software version:  iPad Air 2 or newer iPad Mini 3 or newer iPad Pro iPhone 6s or newer (iPhone 6 and iPhone 6+ are not supported)  Android: The following Android devices have been tested in-house and are officially approved for use with SkyTrak. In general, we have seen best results with newer Android devices containing Octa-core (or dual quad-core) processors. We will continue to test more devices and will update this list accordingly.  Google Pixel C Samsung Galaxy Tab S3 Samsung Galaxy S6 Samsung Galaxy Tab S2 Samsung Galaxy S8  PC:  Windows 7, 8, or 10 Intel Core 2 Duo @ 2.0GHz or higher 2GB RAM or higherProduct Color or Size - (if number): BlackProduct Price: 1995'}

WWGSDataScraper_test = WWGSDataScraper()
WWGSDataScraper_test.scrape_catelog_page()
WWGSDataScraper_test.scrape_individual_product()
WWGSDataScraper_test.upsert_product_data()





'''
def scrape_catelog_page(self):
        #scrape catelog url and retrieve all indiviudal product urls
        base_url = 'https://www.worldwidegolfshops.com/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        r = requests.get('https://www.worldwidegolfshops.com/gps---tech/other-technology/launch-monitors')
        soup = BeautifulSoup(r.content, 'lxml')
        product_list = soup.find_all('section', class_='vtex-product-summary-2-x-container vtex-product-summary-2-x-container--search vtex-product-summary-2-x-containerNormal vtex-product-summary-2-x-containerNormal--search overflow-hidden br3 h-100 w-100 flex flex-column justify-between center tc')
        for item in product_list:
            for link in item.find_all('a', href=True):
                self.product_url_list.append(link['href'])
        print(self.product_url_list)
'''


'''
base_url = 'https://www.worldwidegolfshops.com/'
        driver = webdriver.Chrome()
        driver.get('https://www.worldwidegolfshops.com/gps---tech/other-technology/launch-monitors')
        product_html = driver.find_elements(by= 'vtex-product-summary-2-x-container vtex-product-summary-2-x-container--search vtex-product-summary-2-x-containerNormal vtex-product-summary-2-x-containerNormal--search overflow-hidden br3 h-100 w-100 flex flex-column justify-between center tc')
        for product in product_html:
            product_link = product.find_elements('By.XPATH', '/html/body/div[2]/div/div[1]/div/div[4]/div/div/section/div[2]/div/d
            '''

