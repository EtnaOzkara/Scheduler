import schedule
import NAMEOFFILE

def test():
    print("Test")
    exec(open("NAMEOFFILE.py").read())


schedule.every(10).seconds.do(test)

while True:
    schedule.run_pending()
