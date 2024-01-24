from config import OPENAI_API_KEY
from config import PINECONE_API_KEY
from config import user_prompt
import os
import pandas as pd
import time
from openai import OpenAI
import bardapi
from sentence_transformers import SentenceTransformer
import pinecone
from pinecone import Pinecone


class chatbot:
    #place NLP Processors
    client = OpenAI(api_key=OPENAI_API_KEY)
    #ChatGPT model -- interchangable with 4
    gpt_model="gpt-3.5-turbo"
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    pincone_api_key = PINECONE_API_KEY
    
    def __init__(self, user_query = None, enclosed_prompt = None, context_list = []):
        self.user_query = user_query
        self.enclosed_prompt = enclosed_prompt
        self.context_list = context_list
    
    def initialize_pinecone(self):
        api_key = chatbot.pincone_api_key
        pc = Pinecone(api_key = api_key)
        index_name = 'golf-sim-data'
        self.index = pc.Index(index_name)

    #prompts and recieves user query
    def recieve_query(self, query):
        self.user_query = query
        self.context_list.append(self.user_query)
        

    #vectorizes user query, also retrieves closed prompt that will aid in provdiing a hyper accurate answer. 
    def process_query(self):
        self.enclosed_prompt = []

        user_query_embedding = chatbot.embedding_model.encode(self.user_query).tolist()
        print('Processing: ')
        self.initialize_pinecone()
        print('Initialized Pinecone')
        result = self.index.query(vector=user_query_embedding, top_k=10, include_metadata= True)
        for result in result['matches']:
            self.enclosed_prompt.append(f"{round(result['score'], 2)}: {result['metadata']['text']}")
        self.enclosed_prompt = 'Closed Prompt: ' + str(self.enclosed_prompt) + 'context:' + str(self.context_list) + '\n' + user_prompt + self.user_query
        print(self.enclosed_prompt)


    #prompts user question to ChatGPT
    def chatGPT(self):
       
        response = chatbot.client.chat.completions.create(
        model= chatbot.gpt_model,
        max_tokens = 250,
        messages=[
            {"role": "user", "content": self.enclosed_prompt},
                ])
        response_message = response.choices[0].message.content
        return str(response_message)
   

  



