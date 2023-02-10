class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, time1, time2):
        self.hours = time1.hours + time2.hours
        self.minutes = time1.minutes + time2.minutes
        return self.hours, self.minutes

    def displayMinute(self):
        print(f"{self.hours * 60 + self.minutes} minutes")


time1 = Time(10, 30)
time2 = Time(20, 30)
time3 = Time(0, 0)
time3.addTime(time1, time2)
time3.displayMinute()
