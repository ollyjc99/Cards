from threading import Thread


class Test(Thread):
    def __init__(self, no):
        Thread.__init__(self)
        self.daemon = True
        self.no = no
        self.start()

    def run(self):
        while True:
            self.no += 1
            print(self.no)


def main():
    number = 10
    test = Test(number)
    while True:
        print(number)


if __name__ == '__main__':
    main()