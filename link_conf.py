config = {}

with open('config.txt', 'r')as f:
    for i in f:
        key, value = i.strip().split('=')
        config[key] = value

print(config)

