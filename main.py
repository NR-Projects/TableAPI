import enum
from importlib.resources import contents
from bs4 import BeautifulSoup
from dataclasses import dataclass
from flask import Flask, request, jsonify

import requests

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():

    linkToSift = request.args.get('SiteLink', type=str)

    if linkToSift is None:
        return "Missing Parameters", 400

    print(linkToSift)

    response = requests.get(
        linkToSift,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
        )
    
    full_site_content = BeautifulSoup(response.content, 'html.parser')

    tables_list = full_site_content.findAll('table')

    table_list = []

    for table in tables_list:
        table_obj = {}
        rows = table.findAll('tr')
        for ind, row in enumerate(rows):
            if ind == 0:
                tmp_header_list = []
                headers = row.findAll('th')
                for ind, header in enumerate(headers):
                    table_obj[header.text] = []
                    tmp_header_list.append(header.text)
            else:
                contents = row.findAll('td')
                for ind, content in enumerate(contents):
                    try:
                        curr_header = tmp_header_list[ind]
                        table_obj[curr_header].append(content.text)
                    except IndexError:
                        continue
        
        table_list.append(table_obj)
    
    return jsonify(tables=table_list), 200

if __name__ == '__main__':
    app.run()
