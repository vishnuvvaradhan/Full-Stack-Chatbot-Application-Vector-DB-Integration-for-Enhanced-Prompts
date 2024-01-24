from chatbot_framework import chatbot
from config import PINECONE_API_KEY
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import hashlib
import spacy
from sentence_transformers import SentenceTransformer
import pinecone
from pinecone import Pinecone


class WWGSDataScraper: 
    embedding_model_scraper = SentenceTransformer('all-MiniLM-L6-v2')
    pinecone_api = PINECONE_API_KEY
    nlp = spacy.load('en_core_web_sm')

    
    def __init__(self, url = None, product_url_list = [], product_name = None, product_description = None, product_color = None, product_price = None, product_info_list = None, index = None):
        self.product_url_list = product_url_list
        self.url = url 
        self.product_name = product_name
        self.product_description = product_description
        self.product_color = product_color
        self.product_price = product_price
        self.product_info_list = product_info_list
        self.index = index
    

    def initialize_pinecone(self):
        api_key = WWGSDataScraper.pinecone_api
        pc = Pinecone(api_key = api_key)
        index_name = 'golf-sim-data'
        self.index = pc.Index(index_name)
        
    
    def scrape_catelog_page(self):
        #scrape catelog url and retrieve all indiviudal product urls
        #Use selenium to deal with dynamic webpage -- HTML Loads as page is scrolled

        driver = webdriver.Chrome()
        driver.get('https://www.worldwidegolfshops.com/gps---tech/other-technology/launch-monitors')
        for i in range(0,3):
            driver.execute_script('window.scrollBy(0, 400)')
            time.sleep(1)
        page_source = driver.page_source
        base_url = 'https://www.worldwidegolfshops.com/'
        #Using beautiful soup to grab all product links
        soup = BeautifulSoup(page_source, 'lxml')
        product_list = soup.find_all('section', class_='vtex-product-summary-2-x-container vtex-product-summary-2-x-container--search vtex-product-summary-2-x-containerNormal vtex-product-summary-2-x-containerNormal--search overflow-hidden br3 h-100 w-100 flex flex-column justify-between center tc')
        for item in product_list:
            for link in item.find_all('a', href=True):
                self.product_url_list.append(base_url + link['href'])

    def scrape_individual_product(self):
        print('scraping product data')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        self.product_info_list = []

        for product_link in self.product_url_list:
            r = requests.get(product_link, headers= headers)
            soup = BeautifulSoup(r.content, 'lxml')
            self.product_name = soup.find('span', class_='vtex-store-components-3-x-productBrand').text.strip()
            self.product_description = soup.find('div', class_ = 'worldwidegolf-worldwidegolfstore-10-x-desciptionData mv4').text.strip()
            self.product_color = soup.find('div', class_='available-product').get('id') if soup.find('div', class_='available-product') else 'None'
            self.product_price = soup.find('meta', property='product:price:amount').get('content') if soup.find('meta', property='product:price:amount') else 'None'
        
            information = "Description/Key Features: " + self.product_description + " Product Color or Size - (if number): " + self.product_color + " Product Price: " + self.product_price
            cleaned_information = information.replace('\n', " ")
            self.golf_lanucher_product = {
                'Product Name': self.product_name,
                'Product Information': cleaned_information
            }

            #print(self.golf_lanucher_product)

            self.product_info_list.append(self.golf_lanucher_product)
        print(len(self.product_info_list))


    def chunk_data(self, product_dict, chunk_size = 3):
        #seperate scraped data into chunks, maybe paragraphs or sentences idkk
        doc = WWGSDataScraper.nlp(product_dict['Product Information'])
        sentences = [sentence.text.strip() for sentence in doc.sents]
        chunks = []
        for i in range(0, len(sentences), chunk_size):
            chunk = ' '.join(sentences[i:i+chunk_size])
            chunks.append(f"{product_dict['Product Name']}: {chunk}")
        return chunks
    


    def get_product_content_hash(self, chunk):
        #for the future to check if database needs to be updated.
        hash_object = hashlib.sha256(chunk.encode())
        return hash_object.hexdigest()
    

    def database_contains(self, id): 
            test = self.index.fetch(ids=[id])
            return test['namespace'] == ''


    def upsert_product_data(self, batch_size = 15):
        #for each chunk vectorize it and then upsert it in the database with its hash -- hash | vector atm, will upsert in batches to improve performance
        self.initialize_pinecone()
        vectors = []
        for product in self.product_info_list:
            product_chunk_list = self.chunk_data(product)
            for chunk in product_chunk_list:
                chunk_hash = str(self.get_product_content_hash(chunk))
                if self.database_contains(chunk_hash):
                    chunk_embedding = WWGSDataScraper.embedding_model_scraper.encode(chunk)
                    vectors.append({'id': chunk_hash, "values": chunk_embedding.tolist(), 'metadata': {'text': chunk}})
                    if len(vectors) >= batch_size:
                        #upsert batch into pinecone db
                        self.index.upsert(vectors=vectors)
        if len(vectors) > 0:
            #upsert remaining items
             print('upserting remaining items')
             self.index.upsert(vectors=vectors)
    


