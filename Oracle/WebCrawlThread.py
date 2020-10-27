from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from collections import deque

class WebCrawl:
    def __init__(self):
        self.lock = Lock()
        self.queue = deque()
        self.visited = set()
    def extractHostname(self, url):
        """get domain of url"""
        return url.split("http://")[1].split('/')[0]
    def downloadUrl(self, url):

        nexturls = self.htmlParser.getUrls(url)
        # Use Lock to protect shared states.
        with self.lock:
            for url in nexturls:
                if url not in self.visited and self.curname == self.extractHostname(url):
                    self.queue.append(url)
                    self.visited.add(url)


    def crawl(self, startUrl, htmlParser):
        self.queue.append(startUrl)
        self.curname = self.extractHostname(startUrl)
        self.visited.add(startUrl)
        self.htmlParser = htmlParser
        # Limit to 10 worker threads
        executor = ThreadPoolExecutor(max_workers=10)

        while self.queue:
            url = self.queue.popleft()
            urllist = list()
            urllist.append(url)

            # if still urls in the queue, add to the list
            while self.queue:
                cururl = self.queue.popleft()
                urllist.append(cururl)

            # start execute
            executorlist = list()
            # Execute this batch of threads with threadpool
            for i in range(len(urllist)):
                executorlist.append(executor.submit(self.downloadUrl, (urllist[i])))

            # Main thread waiting for the above threads to finish
            for future in executorlist:
                future.result()
        executor.shutdown()

        return  list(self.visited)