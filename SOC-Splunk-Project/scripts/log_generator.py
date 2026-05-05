import json, random, time, datetime

users = ["vinayak", "user2", "admin"]
actions = ["login", "failed_login", "powershell", "file_access"]

while True:
    log = {
        "user": random.choice(users),
        "action": random.choice(actions),
        "ip": "192.168.1." + str(random.randint(1,50)),
        "device": random.choice(["laptop", "mobile"]),
        "location": random.choice(["India", "US", "Germany"]),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open("soc_logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")

    time.sleep(2)
