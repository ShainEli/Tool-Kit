from threading import Thread
import argparse
import subprocess


def ping(ip):
    result = subprocess.call("ping -c2 %s &> /dev/null \n" % ip, shell=True)
    if result:
        print("%s:>> 不存活\n" % ip)
    else:
        print("%s:>> 存活\n" % ip)


def list_ip(file):
    with open(file, 'r') as f:
        ip_list = f.readlines()
        ip = []
        for i in ip_list:
            ip.append(i)
        return ip


def main_ip(file):
    ip_list = list_ip(file)
    j = 0
    length = len(ip_list)
    while j < length:
        for j in range(length):
            t = Thread(target=ping, args=(ip_list[j], ))
            t.start()
            j += 1
            if j == length:
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IP active scan')
    parser.add_argument("-f", "--file", help="指定文件", default='ip.txt')
    args = parser.parse_args()
    file = args.file
    main_ip(file)