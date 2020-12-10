from nltk.tokenize import sent_tokenize
from image_search import ImageSearch, DisplayImage
import yake
from datetime import datetime, timedelta
from time import sleep
import pdb
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
from text_speech import Audio

FILE_NAME = "doc.txt"
class StoryTeller:  
    def find_keywords(self, doc):
        kw_extractor = yake.KeywordExtractor()
        keywords = kw_extractor.extract_keywords(doc)
        result = ""
        for kw in keywords:
            result = kw[1]
        return result

    def story(self):
        # 1. read doc file
        doc = open(FILE_NAME, 'r', encoding='utf-8')
        doc = doc.read()
        # 2. itrate each sentence
        for sentance in sent_tokenize(doc):
            # 3. find keywords
            print(sentance)
            keyword = self.find_keywords(sentance)
            # print(keyword)
            # 4. search image and # 5. save image
            image_path = ImageSearch().find_weburls(keyword)
            
             # 6. text to audio cretion
            audio_file = Audio().text2audio(sentance, keyword)

            # 7. get duration of audio
            duration = Audio().get_audio_duration(audio_file)

            
            
            # 8. display image ||
            frame = cv2.imread(image_path)         
            cv2.imshow("Story teller", frame)
            # print("[+] waiting photo")
            cv2.waitKey(duration)

            # 8. play audio ||
            Audio().play_audio(duration, audio_file)
            
                   

# 7. text to speech sentance 

StoryTeller().story()
