import requests
import random
from pytube import extract

class Cekilis():
    def __init__(self):
        self.API_KEY = "AIzaSyCcPSNA_4IuMQAnvYjhdr5oD5rXttJReJo"
    
    def requestVideo(self,url,num):
        videoId=extract.video_id(url)
        request1 = dict(requests.get("https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&videoId={}&key={}".format(videoId,self.API_KEY)).json())

        nextPageToken = request1["nextPageToken"]
        cekilisSnippet = set()
        winners = []
        while (True):
            request2 = dict(requests.get(
                "https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&pageToken={}&textFormat=plainText&videoId={}&key={}".format(nextPageToken, videoId, self.API_KEY)).json())
            try:
                nextPageToken = request2["nextPageToken"]
            except:
                break
            for comment in request2["items"]:
                cekilisSnippet.add(str(comment['snippet']["topLevelComment"]["snippet"]["authorDisplayName"]))
        for i in range(num):
            winners.append(random.choice(list(cekilisSnippet)))
        return winners