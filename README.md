# Table API


## Description

An API that fetches all the tables in a site, assuming that they are inside of a table tag


## Dependencies

- Python3
- Flask


## Installation

> Download Repository

```
git clone <url> or download from github
```

> Install all dependencies

```
pip3 install -r requirements.txt
```

> Run from command prompt
```
flask run
```

## Response Objects

1. Add Path to the url to specify site to find manga
2. Always Include ```SiteLink``` as parameter

<br>

Response object Format

For a successful request:
> {  
    "Status":"success",  
    "Data":[<TABLE LIST>]  
}  

For a failed request:
> {  
    "Status":"failed",  
    "Description":"<ERROR DESCRIPTION>",  
    "Data":[]  
}


## Examples

Assuming that you have 127.0.0.1:5000 as the url

```
http://127.0.0.1:5000
```

Should have a response of

```
{"Response":{"Data":[],"Description":"missing \"/SiteLink\"/ parameter","Status":"failed"}}
```

<br><br>


```
http://127.0.0.1:5000/?SiteLink=samplelink.com
```

Should have a response of

```
{"Response":{"Data":[],"Description":"Invalid Link is Passed","Status":"failed"}}
```

<br><br>


```
http://127.0.0.1:5000/?SiteLink=https://www.w3schools.com/html/html_tables.asp
```

Should have a response of

```
{"Response":{"Data":[{"Company":["Alfreds Futterkiste","Centro comercial Moctezuma","Ernst Handel","Island Trading","Laughing Bacchus Winecellars","Magazzini Alimentari Riuniti"],"Contact":["Maria Anders","Francisco Chang","Roland Mendel","Helen Bennett","Yoshi Tannamuri","Giovanni Rovelli"],"Country":["Germany","Mexico","Austria","UK","Canada","Italy"]},{"Description":["Defines a table","Defines a header cell in a table","Defines a row in a table","Defines a cell in a table","Defines a table caption","Specifies a group of one or more columns in a table for formatting","Specifies column properties for each column within a <colgroup> element","Groups the header content in a table","Groups the body content in a table","Groups the footer content in a table"],"Tag":["<table>","<th>","<tr>","<td>","<caption>","<colgroup>","<col>","<thead>","<tbody>","<tfoot>"]}],"Status":"success"}}
```

## Support

All application bugs, problems, etc. can be placed on the issues tab.

## Contributing

Pull requests are welcome. For all changes, please open an issue first to discuss what you would like to change.

## License

[Unlicensed](https://unlicense.org)