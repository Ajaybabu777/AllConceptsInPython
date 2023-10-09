class PrintSpooling:
    def __init__(self):
        self.print_queue = []

    def addPrintJObs(self, job):
        self.print_queue.append(job)
        print(f"print job {job} added to the queue")

    def printThePrintJobs(self):
        while self.print_queue:
            job = self.print_queue.pop(0)
            print(f"Printing: {job}")
            print(f"Print JOb {job} complted")

p = PrintSpooling()

p.addPrintJObs("resume.txt")
p.addPrintJObs("nature.jpg")
p.addPrintJObs("report.txt")
p.addPrintJObs("data.csv")

print("printing The Print Jobs: ")
p.printThePrintJobs()