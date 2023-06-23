from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

brown_dwarfs_url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(brown_dwarfs_url)
