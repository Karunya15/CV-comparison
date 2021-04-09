# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:00:23 2020

@author: 3kt
"""

import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

def read_documents(path):
    filenames = os.listdir(path) 
    resumes = []
    for filename in filenames:
        name = os.path.join(path,filename)
        resume = docx2txt.process(name)
        resumes.append(resume)
    return resumes



def find_similarity(resume,jd):
    text = [resume,jd]
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(text)
    matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
    matchPercentage = round(matchPercentage, 2)
    return matchPercentage
    
    
def main():
    input1 = r"C:\Users\3kt\Desktop\Similarity\CV"
    input2 = r"C:\Users\3kt\Desktop\Similarity\JD"
    read_resume = read_documents(input1)
    read_JD = read_documents(input2)
    for i in range(len(read_resume)):
        for j in range(len(read_JD)):
            sim = find_similarity(read_resume[i],read_JD[j])
            print(sim)
            
if __name__ == '__main__':
    main()