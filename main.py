from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import xlrd

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
excel_data_df = pandas.read_excel('wine.xlsx', sheet_name='Лист1', encoding='cp1251-sig')
wines = excel_data_df.to_json(orient='records')
print(wines)
year = datetime.datetime.now().year

rendered_page = template.render(
    age=str(year - 1920),
    wines=wines,
)




with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
