import json
import random


if __name__ == '__main__':
    with open('adjective.json') as f:
        adjective = json.loads(f.read())
    with open('noun.json') as f:
        noun = json.loads(f.read())

    for i in range(5):
        print(adjective[random.randrange(len(adjective))]+'的'+noun[random.randrange(len(noun))])
