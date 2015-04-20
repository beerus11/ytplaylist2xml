__author__ = 'Anurag'
import urllib2
from BeautifulSoup import BeautifulSoup
#Youtube Link Here
website = urllib2.urlopen("https://www.youtube.com/watch?v=8PzDfykGg_g&list=PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G")
soup = BeautifulSoup(website)
list2= soup.findAll("li","yt-uix-scroller-scroll-unit")
fout=open('youtube_dump.xml','w')
for i in range(0,len(list2)):
    mystring='<link id="'+str(i+1)+'" name="'+str(list2[i]["data-video-title"])+'">'+str(list2[i]["data-video-id"])+"</link>"
    fout.write(mystring+'\n')
fout.close()


