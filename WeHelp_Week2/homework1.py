# h1
print("hw1")
def find_and_print(messages, current_station):
    # 定義綠線 (greenLine) 的地鐵站索引
    green_line = {
        "Songshan": 0, "Nanjing Sanmin": 1, "Taipei Arena": 2, "Nanjing Fuxing": 3,
        "Songjiang Nanjing": 4, "Zhongshan": 5, "Beimen": 6, "Ximen": 7,
        "Xiaonanmen": 8, "Chiang Kai-Shek Memorial Hall": 9, "Guting": 10,
        "Taipower Building": 11, "Gongguan": 12, "Wanlong": 13, "Jingmei": 14,
        "Dapinglin": 15, "Qizhang": 16, "Xindian City Hall": 17, "Xindian": 18
    }

    # 定義其他捷運線的索引 (小碧潭線)
    rest_line = {"Qizhang": 0, "Xiaobitan station": 1}

    # 建立一個字典來存放每個人所在的車站
    person_stations = {}
    
    # 遍歷 messages，找出每個人提到的車站
    for name, message in messages.items():
        for station in {**green_line, **rest_line}:  # 合併兩條線的車站
            if station in message: #如果 station 合併後的字典裡的key值對得上station，則人名:位置傳給person_stations = {}
                 person_stations[name] = station# 比如"Bob" : "Ximen" 也就是說把合併後字典的key（位置）給他轉換成value

    # 計算每個人的距離
    distances = {}
    for name, person_station in person_stations.items():
        # 2. (1)都在綠 (2) 兩人都在支線 (3)我在綠他在支線 (4)我在支線他在綠
        if current_station in green_line and person_station in green_line:
            distances[name] = abs(green_line[current_station] - green_line[person_station])
        elif current_station in rest_line and person_station in rest_line:
            distances[name] = abs(rest_line[current_station] - rest_line[person_station])
        elif current_station in green_line and person_station in rest_line:
            distances[name] = abs(green_line[current_station] - green_line["Qizhang"]) + rest_line[person_station]
        elif current_station in rest_line and person_station in green_line:
            distances[name] = abs(rest_line[current_station] - rest_line["Qizhang"]) + abs(green_line["Qizhang"] - green_line[person_station])

    # 找出距離最小值
    min_distance = min(distances.values())
    
    # 找出對應的名稱
    for name, distance in distances.items():
        if distance == min_distance:
            print(name)
            return

# 測試資料
messages = {
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Leslie": "I'm at home near Xiaobitan station.",
    "Vivian": "I'm at Xindian station waiting for you.",
}

# 測試函式
find_and_print(messages, "Wanlong")  # print Mary
find_and_print(messages, "Songshan")  # print Copper
find_and_print(messages, "Qizhang")  # print Leslie
find_and_print(messages, "Ximen")  # print Bob
find_and_print(messages, "Xindian City Hall")  # print Vivian
print("-----------------------------")
# h2
print("hw2")
def book(consultants, hour, duration, criteria):
    # 初始化 schedule 字典，每個顧問的名字對應到一個空列表（儲存預訂時間）
    if not hasattr(book, "schedule"):
        book.schedule = {c["name"]: [] for c in consultants}

    # 按 criteria 排序顧問列表
    if criteria == "price":
        consultants = sorted(consultants, key=lambda c: c["price"])
    elif criteria == "rate":
        consultants = sorted(consultants, key=lambda c: c["rate"], reverse=True)

    # 檢查顧問是否可用
    for consultant in consultants:
        name = consultant["name"]
        booked_times = book.schedule[name]
        new_time_range = set(range(hour, hour + duration))  # 新預約時間的範圍

        # 確保沒有時間重疊
        if all(new_time not in booked_times for new_time in new_time_range):
            # 預訂成功，更新顧問的時間表
            book.schedule[name].extend(new_time_range)
            print(name)
            return

    # 若無法預訂，輸出 "No Service"
    print("No Service")


# 測試案例
consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}
]

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John
print("-----------------------------")

# hw3
print("hw3")
def func(*data):
# your code here
    name＿list= []
    # step1抓出子元素中間名       
    for name in data:
        # 判斷名字長度並切出中間名
        if len(name) == 2 or len(name) == 3:
            middle_name = name[1:2]  # 切出index1（不包含尾）
            # 把中間名加入到name_list[]有序陣列
            name_list.append(middle_name)
        elif len(name) == 4 or len(name) == 5:
            # 把中間名加入到name_list[]有序陣列
            middle_name = name[2:3]  # 取出index2(不包含尾)
            name_list.append(middle_name)
    # print(name_list)
    # step2 找出不重複的中間名索引
    middleName_index = []
    # emumerate方法基本用法
    # enumerate(name_list)會將個name_list每個元素和對應的索引（index）一起返回

    for i, middle_name in enumerate(name_list):
    # for i in range(len(name_list)):
    #     middle_name= name_list[i] 
        # print(i, middle_name) #也等於print(list(enumerate(name_list)))
        #name_list.count(middle_name) 是全局的檢查：
        #它不在意目前是在哪個索引（i），而是直接遍歷整個列表，找出所有與 middle_name 相同的元素，並返回總次數。
        count = name_list.count(middle_name);
        if(count == 1): #在只出現一次的情況下把它儲存下來
            middleName_index.append(i)
    

    #step3把獨一無二的中間名，其全名儲存在另外一個陣列，印出來
    resultArray =[]
    if middleName_index !=[]:
        #查找除存在middleName_index陣列中 每個子元素索引標籤的序號
        # in 是關鍵字，用於指定要從哪個可迭代對象（如列表、字典等）中取出元素
        for indexValue in middleName_index:
            #把data[對應的索引標籤序號]的值印出來，儲存在resultArray[]
            resultArray.append(data[indexValue])
        print(resultArray)
    else:
        print("沒有")


# func("彭大牆", "陳王明雅", "吳明", "韓國瑜"); # print 彭大牆"韓國瑜"
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有 
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
print("-----------------------------")

# hw4
print("hw4")
def getNumber(index):
    if index == 0:
        print(0)
        return

    result = 0
    for i in range(1, index + 1):#1~index
        #被3整除的前一項數字，否則前項數字加4
        if i % 3 == 0:
            result -= 1
        else:
            result += 4
    print(result)


getNumber(0)  # print 0
getNumber(1)  # print 4
getNumber(5) # print 15
getNumber(10) # print 25
getNumber(30)# print 70