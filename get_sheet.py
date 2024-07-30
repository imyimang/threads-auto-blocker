import requests as rs  
import csv  
import re

def get_user_list(sheet):
    # 定義正則表達式  
    pattern = r'https://www\.threads\.net/@\w+'
    
    if re.match(r'https://docs\.google\.com/spreadsheets/.+', sheet):
        csv_url = sheet.replace('/edit?gid=', '/export?format=csv&gid=').split('#')[0]
        res = rs.get(csv_url)

        if res.status_code == 200:
            with open('sheet.csv', 'wb') as file:
                file.write(res.content)
        else:
            print("無法獲取CSV檔案，請檢查URL。")
            return set()  # 返回空集合以避免後續處理
            
        matching_ids = set()
        with open('sheet.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    first_cell = row[0]
                    matches = re.findall(pattern, first_cell)
                    for match in matches:
                        user_name = match.replace("https://www.threads.net/@", "")
                        matching_ids.add(user_name)
    
    else:
        matching_ids = set()
        with open(sheet, 'r', newline='', encoding='utf-8') as file:
            for line in file:
                if re.match(pattern, line):
                    line = match.replace("https://www.threads.net/@", "")
                matching_ids.add(line)

    print(f"獲取完畢，共 {len(matching_ids)} 筆資料")
    return matching_ids