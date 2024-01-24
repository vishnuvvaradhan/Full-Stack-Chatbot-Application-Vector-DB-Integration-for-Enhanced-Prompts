from database import WWGSDataScraper

#Deployed on Lambda

WWGSDataScraper_test = WWGSDataScraper()
WWGSDataScraper_test.scrape_catelog_page()
WWGSDataScraper_test.scrape_individual_product()
WWGSDataScraper_test.upsert_product_data()
