import requests
from bs4 import BeautifulSoup
import cv2
import os
import pdb


output = "images"
SEARCH_URL = "https://www.google.com/search?safe=active&hl=EN&tbm=isch&sxsrf=ALeKk01FuWXGeG6ZhO96ZpZA10Ym4TTlNg%3A1606830727832&source=hp&biw=1536&bih=731&ei=h0rGX_qQMJLD3LUPj_2X-AM&q="
if not os.path.exists(output):
    os.mkdir(output)
class ImageSearch:
    def download_image(self, url, filename = "test"):
        flag = True
        try:
            # pdb.set_trace()
            p = os.path.sep.join([output, "{}.jpg".format(
                str(filename).zfill(8))])
            # try to download the image
            r = requests.get(url, timeout=60)
            # save the image to disk
            
            f = open(p, "wb")
            f.write(r.content)
            f.close()
            # update the counter
            # print("[INFO] downloaded: {}".format(p))            
        # handle if any exceptions are thrown during the download process
        except:
            flag = False
            print("[INFO] error downloading {}...skipping".format(p))
        return flag, p

    def find_weburls(self, query):
        source_code = requests.get(SEARCH_URL + query)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="lxml")

        rows = []        
        for link in soup.find_all('img'):
            href = link.get('src')
            
            is_downloaded, image_path = self.download_image(href, query)            
            print(is_downloaded, image_path)
            if is_downloaded:                
                break
        return image_path

class DisplayImage:
    def show(self, image_path):
        frame = cv2.imread(image_path)
        cv2.imshow("Story Teller", frame)
        # cv2.imshow("image2", frame)
        # k = cv2.waitKey(0)
    def destroy(self):
        cv2.destroyAllWindows()
            
def show_image():
    for img in os.listdir(output):
        path = os.path.join(output, img)
        frame = cv2.imread(path)
        cv2.imshow("image", frame)
        # cv2.imshow("image2", frame)
        k = cv2.waitKey(0)
        if k == 27: # esc key
            cv2.destroyAllWindows()
# download_image()
#show_image()
