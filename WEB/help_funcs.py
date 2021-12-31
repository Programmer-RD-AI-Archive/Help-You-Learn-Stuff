def send_sms(msg: str, number: int) -> str:
    account_sid = "ACbeeb34a0326adf707ec9a68902be68dc"
    auth_token = "09aee4b52484eb7218008642c35388f3"
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=msg, from_="+13132468800", to=number)
    return message.sid
    return "Testing"


def log_ip_address(url_trying_to_access: str, ip_address: str) -> None:
    db = cluster["ips"]
    collection = db["ips"]
    collection.insert_one(
        {
            "ip_address": ip_address,
            "url_trying_to_access": url_trying_to_access,
            "time": datetime.datetime.now(),
        }
    )


def two_fac_auth(user_name: str, email: str, phone_numer: str) -> list:
    time = (
        str(datetime.datetime.now().year)
        + " "
        + str(datetime.datetime.now().month)
        + " "
        + str(datetime.datetime.now().day)
        + " "
        + str(datetime.datetime.now().hour)
        + " "
        + str(datetime.datetime.now().minute)
    )
    db = cluster["2FACAUTH"]
    collection = db["2FACAUTH"]
    email_random = random.randint(0, 10000000)
    sms_random = random.randint(0, 10000000)
    collection.insert_one(
        {
            email: email_random,
            phone_numer: sms_random,
            "user_name": user_name,
            "time": time,
        }
    )
    send_sms(
        f"{sms_random} - EmoPro Code for 2Auth \n\n\n\n\n Only for 5 Min",
        "+" + str(decode(phone_numer)),
    )
    send_email(
        f"EmoPro 2Auth Code",
        decode(email),
        f"{email_random} EmoPro Code for 2Auth \n\n\n\n\n Only for 5 Min",
    )
    return [sms_random, email_random]


def get_id(db_name, collection_name):
    db = cluster[db_name]
    collection = db[collection_name]
    idx = 0
    for collection_iter in collection.find():
        collection_iter = collection_iter["_id"]
        # print(collection_iter,idx)
        if collection_iter >= idx:
            idx = collection_iter + 1
            print(collection_iter, idx)
    return idx
