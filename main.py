from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import xlrd
from collections import defaultdict
import argparse
import os

parser = argparse.ArgumentParser(description='Elite wines')
parser.add_argument('--winetable', help='Your path to test table of wines xls file', default='wine_example.xlsx')
test_xls_path = parser.parse_args().winetable

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
excel_data_df = pandas.read_excel(test_xls_path, keep_default_na=False)
wines_json_string = excel_data_df.to_json(orient='records')
wines = pandas.read_json(wines_json_string).to_dict(orient='records')

wines_by_category = defaultdict(list)
for wine in wines:
  wines_by_category[wine['Категория']].append(wine)

year = datetime.datetime.now().year
age = str(year - 1920)

rendered_page = template.render(
    age=age,
    wines=wines_by_category,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
