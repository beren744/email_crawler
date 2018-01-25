# This is a template for a simple email crawler
# including some code snippets below that you should find helpful

from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
