print("======Task 1======")
#We just received messages from 5 friends in JSON format, and we want to take the green
#line, including Xiaobitan station, of Taipei MRT to meet one of them. Write code to find out
#the nearest friend and print name, based on any given station currently located at and
#station count between two stations.

def find_and_print(messages, current_station):
    green_line = ["Songshan","Nanjing Sanming","Taipei Arena","Nanjing Fuxing","Songjian Nanjing","Zhongshan","Beimen","Ximen", "Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xiaobitan","Xindian City Hall","Xindian"
    ]
    green_line.insert(green_line.index("Qizhang") + 1, "Xiaobitan")

    current_station_index = green_line.index(current_station)
    closest_friend = ""
    first_distance = 1000

    for friend, message in messages.items():
        friend_station_index = -1
        for station in green_line:
            if station in message:
                friend_station_index = green_line.index(station)
                break

        if friend_station_index != -1:
            distance = abs(friend_station_index - current_station_index)
            if distance < first_distance:
                first_distance = distance
                closest_friend = friend

    print(closest_friend)

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

print("======Task 2======")
#Assume we have consultants for consulting services. Help people book the best matching
#consultant in a day, based on hours, service durations, and selection criteria.
#1. Booking requests are one by one, order matters.
#2. A consultant is only available if there is no overlapping between already booked time
#and an incoming request time.
#3. If the criteria is "price", choose the available consultant with the lowest price.
#4. If the criteria is "rate", choose the available consultant with the highest rate.
#5. If every consultant is unavailable, print "No Service".

JohnSchedule = [0] * 24
BobSchedule = [0] * 24
JennySchedule = [0] * 24

def book(consultants, hour, duration, criteria):
    if criteria == "price":
        criteria_select = sorted(consultants, key=lambda x:x["price"])
    else:
        criteria_select = sorted(consultants, key=lambda x:x["rate"], reverse=True)

    for criteria_priority in criteria_select:
        if criteria_priority["name"] == "Bob":
            schedule = BobSchedule
        elif criteria_priority["name"] == "John":
            schedule = JohnSchedule
        elif criteria_priority["name"] == "Jenny":
            schedule = JennySchedule

        overlap = True
        for app in range(hour, hour + duration):
            if schedule[app] == 1:
                overlap = False
                break

        if overlap:
            for i in range(hour, hour + duration):
                schedule[i] = 1
            print(f"{criteria_priority['name']}")
            return

    print("No Service")

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]


book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

print("======Task 3======")
#Find out whose middle name is unique among all the names, and print it. You can assume
#every input is a Chinese name with 2 ~ 5 words. If there are only 2 words in a name, the
#middle name is defined as the second word. If there are 4 words in a name, the middle name
#is defined as the third word.
#Note: Never change existing code.

def func(*data):
    middle_names = {}
    flag=0
    for name in data:
        middleIndex = len(name) // 2
        middle_name =name[middleIndex]

        if middle_name in middle_names:
            middle_names[middle_name].append(name)
        else:
            middle_names[middle_name] = [name]
    for names in middle_names.values():
        if len(names) == 1:
            print("".join(names))
            flag=1
            break
    if flag==0:
        print("沒有")


func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

print("======Task 4======")
#There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
#Find out the nth term in this sequence.
#Note: Never change existing code.
def get_number(index):
   total = 0
   for i in range(index):
        if (i + 1) % 3 == 0:
            total -= 1
        else:
            total += 4
   print(total)

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70