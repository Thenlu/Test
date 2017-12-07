import requests
import json

def run():
    # url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': None,
        'X-Requested-With': 'XMLHttpRequest',
    }
    data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python',
    }
    r = requests.post(
        # 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0',
        'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0',
        headers=headers, data=data)
    # retulet = r.content.decode()
    rettee = r.content.decode()
    dict_response = json.loads(rettee)
    # print(dict_response)
    result = dict_response['content']['positionResult']['result'][0]
    print(result)
    # line = json.dumps(result, ensure_ascii=False)

    # with open('line.json', 'w') as f:
    #     f.write(line)


if __name__ == '__main__':
    run()
