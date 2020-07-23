from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import xlrd
import pprint
from collections import defaultdict

LIST_OF_WINES_NAME = 'wine3.xlsx'

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
excel_data_df = pandas.read_excel(LIST_OF_WINES_NAME)
wines_json_string = excel_data_df.to_json(orient='records')
wines = pandas.read_json(wines_json_string).to_dict(orient='records')

wines_by_category = defaultdict(list)
for wine in wines:
  wines_by_category[wine['Категория']].append(wine)

printer = pprint.PrettyPrinter()
printer.pprint(wines_by_category)

categories = list(wines_by_category.keys())
year = datetime.datetime.now().year
age = str(year - 1920)

rendered_page = template.render(
    age=age,
    wines=wines,
    categories=categories,
)

pp = pprint.PrettyPrinter(indent=4)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
