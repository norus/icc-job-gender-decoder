#!/usr/bin/env python3
from nltk.tokenize import word_tokenize
import json
import requests
from selectorlib import Extractor
from collections import Counter

class JobAdAnalyzer:
    def __init__(self, selector='selectors.yml', urls='urls.txt', masculine_words='masculine.txt', feminine_words='feminine.txt'):
        self.selector = selector
        self.urls = open(urls).read().splitlines()
        self.masculine_words = open(masculine_words).read().splitlines()
        self.feminine_words = open(feminine_words).read().splitlines()

    def scrape(self, url):
        extractor = Extractor.from_yaml_file(self.selector)
        headers = {
            'X-Staff': 'Says Hello!',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; .NET CLR 2.0.50727)',
            'Accept': 'text/html',
            'Accept-Language': 'en-US'
        }

        r = requests.get(url, headers=headers)

        return extractor.extract(r.text)


    def analyze(self):
            res = {}

            for url in self.urls:
                data = self.scrape(url)

                if data:
                    job_title = data['job_title']
                    # clean up job desc before checking
                    tokens = word_tokenize(data['job_desc'].lower())
                    job_desc_words = [word for word in tokens if word.isalpha()]
                    job_desc_counter = Counter(job_desc_words)

                masculine_coded_words_found = []
                feminine_coded_words_found = []

                for masculine_coded_word in self.masculine_words:
                    if masculine_coded_word in job_desc_counter:
                        masculine_coded_words_found.append({
                            'word': masculine_coded_word,
                            'count': job_desc_counter[masculine_coded_word]
                        })

                for feminine_coded_word in self.feminine_words:
                    if feminine_coded_word in job_desc_counter:
                        feminine_coded_words_found.append({
                            'word': feminine_coded_word,
                            'count': job_desc_counter[feminine_coded_word]
                        })

                if masculine_coded_words_found or feminine_coded_words_found:
                    res = {
                        'job_title': job_title,
                        'job_url': url.rstrip('\n'),
                        'masculine_coded_words': masculine_coded_words_found,
                        'feminine_coded_words': feminine_coded_words_found,
                        'masculine_coded_words_total': len(masculine_coded_words_found),
                        'feminine_coded_words_total': len(feminine_coded_words_found)}

                print(json.dumps(res, indent=4))

c = JobAdAnalyzer()
c.analyze()
