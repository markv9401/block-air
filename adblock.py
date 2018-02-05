import requests
import json


config = json.load(open('config.json'))
sources = config['adblock_sources']


def unify(input):
    if '#' in input:
        return None

    temp = input.replace('\t', ' ').replace('\r', '')
    temp = temp.split(' ')[-1]
    temp = '0.0.0.0 ' + temp

    return temp


def getAll(sources):
    hosts = []
    s = requests.session()

    i = 1
    rawarr = []
    for source in sources:
        print('Sourcing ' + source + ' (' + str(i) + '/' + str(len(sources)) + ')')
        raw = s.get(source).text
        rawarr += raw.split('\n')
        i += 1

    i = 1
    lenrawarr = len(rawarr)
    for entry in rawarr:
        print('process: ' + str(i/lenrawarr*100) + '%')
        temp = unify(entry)
        if temp and temp not in hosts:
            hosts.append(temp)
        i = i + 1

    return hosts


if __name__ == '__main__':
    hosts = getAll(sources)

    with open('hosts', 'w') as f:
        for host in hosts:
            print(host)
            f.write(host + '\n')

    print('--------------------------------')
    print('total nr. of hosts: ' + str(len(hosts)))






