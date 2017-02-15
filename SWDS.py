import requests

def BruteForce(host):
    GotResponse = [301,200,302,403] #What httpStatus want to print
    mydict = []
    try:
        with open('dictionary.txt', 'r') as dictionary:
            mydict = [_.strip() for _ in dictionary.readlines()]
    except OSError as e:
        print(e)
    result = []
    for dic in mydict:
        try:
            response = requests.get(host+dic)
            if response.status_code in GotResponse:
                print(response,dic)
        except OSError as e:
            print(e)
            break
            
if __name__=='__main__':
    print ("===Python Web Directories and Files Scanner By BeeeeeMo===\n")
    target = input('Enter target Url:')
    BruteForce(target)
    print('Done!')