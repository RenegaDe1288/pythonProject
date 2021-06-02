server_data = {

    "server": {

        "host": "127.0.0.1",

        "port": "10"

    },

    "configuration": {

        "access": "true",

        "login": "Ivan",

        "password": "qwerty"

    }

}

for key, object in server_data.items():
    print(key, ':')
    for name, value in object.items():
        print('\t', name, ': ', value)
