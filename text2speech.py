
import pyphen
import syllable
import os
from  AppKit import NSSpeechSynthesizer
import sys
import Foundation
import nltk
import time
from nltk.corpus import cmudict
import re
import shutil

arpabet = cmudict.dict()


dic = pyphen.Pyphen(lang='en')

##split text into syllables list
def get_syllables_list(text):
    l=[]
    for word in text.split():
        syl=dic.inserted(word).split('-')
        if len(syl)==1:
            w=syl
        elif arpabet.get(word)==None:
            w=dic.inserted(word).split('-')
        else: 
            w=arpabet[word][0]                
            for i in range(len(w)-1,0,-1):
                if (i!=0 and len(w[i-1])==1) or len(set('aeiouy') - set(w[i-1].lower()))==6:
                    w[i-1]=w[i-1]+w[i]
                    del(w[i])
                    continue
                if len(w[i])==1 or len(set('aeiouy') - set(w[i].lower()))==6:
                    w[i-1]=w[i-1]+w[i]
                    del(w[i])
                        
             
        for i in w:
            if(len(i)>2 and re.sub('[^a-zA-Z]+', '', i.lower())[-1] in 'aeiouy' and
               re.sub('[^a-zA-Z]+', '', i.lower())[-1] in 'aeiouy'
               and re.sub('[^a-zA-Z]+', '', i.lower())[-1]==re.sub('[^a-zA-Z]+', '', i.lower())[-2]):
                i=i[:-2]
            if re.sub('[^a-zA-Z]+', '', i.lower()).endswith("iy"):
                i=i[:-3]+'ee'
            l.append(i.lower())
    l=[re.sub('[^a-zA-Z]+', '', x) for x in l]        
    return l

##Function get text and save speech syllables as separate mp3 files
def text2speech(text):
    dirname=str(time.time())
    os.mkdir('./save/'+dirname)
    ls=get_syllables_list(text)
    print(ls)
    for i in range(len(ls)):
        #os.system('say '+ls[i])
        save_speech(ls[i],'./save/'+dirname+'/'+str(i)+'.mp3')

##send text to only hear it speech syllables
def say_text(text):
    n=get_syllables_list(text)
    print(n)
    for i in n:
        os.system('say '+i)
        
def save_speech(text,fileSavePath):
    ##Save Speech Syllables
    nssp = NSSpeechSynthesizer
    ve = nssp.alloc().init()
    ve.setRate_(200)
    url = Foundation.NSURL.fileURLWithPath_(fileSavePath)
    ve.startSpeakingString_toURL_(text,url)

