from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

import requests


class Response:
    def __init__(self, Status, Description, Data):
        self.Status = Status
        self.Description = Description
        self.Data = Data
    
    def GetData(self):
        ResponseData = {}

        ResponseData['Status'] = self.Status
        
        if self.Status == 'failed':
            ResponseData['Description'] = self.Description

        ResponseData['Data'] = self.Data

        return ResponseData


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():

    linkToSift = request.args.get('SiteLink', type=str)

    if linkToSift is None or linkToSift == "":
        return jsonify(Response=Response('failed', 'missing "/SiteLink"/ parameter', []).GetData()), 400

    try:
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

    except Exception as e:
        return jsonify(Response=Response('failed', 'Invalid Link is Passed', []).GetData()), 400

    return jsonify(Response=Response('success', '', table_list).GetData()), 200

if __name__ == '__main__':
    app.run()
