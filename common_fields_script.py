# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 13:30:39 2021

@author: lakna
"""
import os
import parser

# nltk related libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tika import parser
from tika import unpack

# The function that creates the menu
def main():
    
    def menu():
        choice = -1
        while choice not in (0,1,2,3,4):
            choice = int(input('''
    1. Building Permit
    2. Business Licence 
    3. Boards and Commission 
    4. Dog Licence
    What document type do you want to find common fields for: ''').strip())
            if choice not in (0,1,2,3,4):
                print("\nOption not valid! Please select a valid option (0-6).")
        return choice
    
    def directory_change ():   
         choice=menu()
         if choice == 1:
             os.chdir("C:\\Users\\lakna\\OneDrive\\Desktop\\CityGrows\\common_fields\\building_permits")  
         elif choice == 2:
             os.chdir("C:\\Users\\lakna\\OneDrive\\Desktop\\CityGrows\\common_fields\\business_licence")  
         elif choice == 3:
             os.chdir("C:\\Users\\lakna\\OneDrive\\Desktop\\CityGrows\\common_fields\\boards_and_comissions")  
         elif choice == 4:
             os.chdir("C:\\Users\\lakna\\OneDrive\\Desktop\\CityGrows\\common_fields\\dog_licence")  
    
    directory_change()
    
    def data_clean():
        permitdict=dict()
        
        for permit in os.listdir():
            parsed = parser.from_file(permit)
            line=parsed["content"]
            try:
                tokens = nltk.word_tokenize(line)
                words_an=[word.lower() for word in tokens if word.isalpha()]
                words=[t for t in words_an if not t in stopwords.words("english")]
                permitdict[permit]=words
            except TypeError:
                print(permit)
        
        return(permitdict)        
    
    
    cleaned_permitdict = data_clean()
    
    ls=[]
    
    for i in cleaned_permitdict.values():
        ls.append(i)
        
        
    flat_list = [item for sublist in ls for item in sublist]    
    
    from collections import Counter
    Counter = Counter(flat_list)
    
    most_occur = Counter.most_common(10)
    
    
    for i in most_occur:
        print(i)
    
if __name__=='__main__':    
   main()
    
    
    






