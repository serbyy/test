import xlsxwriter,requests,json

txt='''
8.8.8.8
140.82.121.3
8.8.8.8
140.82.121.3
'''


workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for ip in txt.split():
    url = "https://freegeoip.app/json/"+ip
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
    }
    r=requests.get(url, headers=headers)
    print(r.text)
    country_name=json.loads(r.text)['country_name']
    region_code=json.loads(r.text)['region_code']
    city=json.loads(r.text)['city']

    worksheet.write(row, col,     ip)
    worksheet.write(row, col + 1, country_name)
    worksheet.write(row, col + 2, region_code)
    worksheet.write(row, col + 3, city)
    row += 1

workbook.close()