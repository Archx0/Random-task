import random
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def worklist(day):
    people = ['omar','moayd','meshare','khiled']
    tasks = ['room','bathroom','kitchen ','dinnerroom']
    print(colors.OKBLUE+ f"===== {day} ====="+colors.ENDC)

    for i in range(4):
        whois = random.choice(people)
        work = random.choice(tasks)
        tasks.remove(work)
        people.remove(whois)
        print(colors.FAIL+"=>"+ colors.ENDC+ f" {whois} : {work}")
        
weekday = ['sun','mon','the','wed','thu','fri','sat']
for day in weekday:
    worklist(day)