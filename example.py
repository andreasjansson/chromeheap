import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import chromeheap

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.add_argument('--user-data-dir=/tmp/jsleakcheck') # assumes logged in
    chrome_options.add_argument('--js-flags=--stack_trace_limit=-1')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('http://www.thisismyjam.com')

    stats = chromeheap.stats()
    print 'heap size: %s, node count: %d\n' % stats
