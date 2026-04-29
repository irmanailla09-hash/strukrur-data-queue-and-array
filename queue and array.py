import random

# --- IMPLEMENTASI ADT DASAR (Untuk mendukung simulasi) ---

class Array:
    def __init__(self, size):
        self._items = [None] * size
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        self._items[index] = value
    def __len__(self):
        return len(self._items)

class Queue:
    def __init__(self):
        self._qList = list()
    def isEmpty(self):
        return len(self._qList) == 0
    def __len__(self):
        return len(self._qList)
    def enqueue(self, item):
        self._qList.append(item)
    def dequeue(self):
        assert not self.isEmpty(), "Queue kosong"
        return self._qList.pop(0)

# --- CLASS PEMBANTU UNTUK SIMULASI ---

class TicketAgent:
    def __init__(self, id):
        self._id = id
        self._passenger = None
        self._stopTime = -1

    def isFree(self):
        return self._passenger is None

    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    def isFinished(self, curTime):
        return self._passenger is not None and curTime >= self._stopTime

    def stopService(self):
        passenger = self._passenger
        self._passenger = None
        return passenger

class Passenger:
    def __init__(self, id, arrivalTime):
        self._id = id
        self._arrivalTime = arrivalTime
    def arrivalTime(self):
        return self._arrivalTime

# --- JAWABAN NOMOR 4 & 5: IMPLEMENTASI CLASS SIMULASI ---

class TicketCounterSimulation:
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # Menggunakan probabilitas kedatangan berdasarkan waktu rata-rata [cite: 33]
        self._arriveProb = 1.0 / betweenTime 
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    # Implementasi metode yang tersisa (Nomor 4)
    def _handleArrival(self, curTime):
        if random.random() < self._arriveProb:
            self._numPassengers += 1
            p = Passenger(self._numPassengers, curTime)
            self._passengerQ.enqueue(p)

    def _handleBeginService(self, curTime):
        for i in range(len(self._theAgents)):
            if self._theAgents[i].isFree() and not self._passengerQ.isEmpty():
                passenger = self._passengerQ.dequeue()
                self._totalWaitTime += (curTime - passenger.arrivalTime())
                stopTime = curTime + self._serviceTime
                self._theAgents[i].startService(passenger, stopTime)

    def _handleEndService(self, curTime):
        for i in range(len(self._theAgents)):
            if self._theAgents[i].isFinished(curTime):
                self._theAgents[i].stopService()

    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed if numServed > 0 else 0.0
        print(f"Number of passengers served = {numServed}")
        print(f"Number of passengers remaining in line = {len(self._passengerQ)}")
        print(f"The average wait time was {avgWait:4.2f} minutes.")

# --- JAWABAN NOMOR 6: REVERSE QUEUE ---

def reverseQueue(q):
    stack = []
    while not q.isEmpty():
        stack.append(q.dequeue())
    while len(stack) > 0:
        q.enqueue(stack.pop())

# --- EKSEKUSI SEMUA NOMOR ---

if __name__ == "__main__":
    # Nomor 2: Eksekusi Manual 1
    print("--- Jawaban Nomor 2 ---")
    v2 = Queue()
    for i in range(16):
        if i % 3 == 0: v2.enqueue(i)
    print("Isi Queue:", v2._qList) # Output: [3, 6, 9, 12, 15]

    # Nomor 3: Eksekusi Manual 2
    print("\n--- Jawaban Nomor 3 ---")
    v3 = Queue()
    for i in range(16):
        if i % 3 == 0: v3.enqueue(i)
        elif i % 4 == 0: v3.dequeue()
    print("Isi Queue:", v3._qList) # Output: [3, 6, 9, 12, 15] (0 di-dequeue saat i=4, 8&12 tidak trigger elif karena i%3)

    # Nomor 4 & 5: Menjalankan Simulasi
    print("\n--- Jawaban Nomor 4 & 5 (Contoh Simulasi) ---")
    sim = TicketCounterSimulation(2, 100, 2, 3)
    sim.run()
    sim.printResults()

    # Nomor 6: Membalik Queue
    print("\n--- Jawaban Nomor 6 (Reverse Queue) ---")
    testQ = Queue()
    for x in [1, 2, 3, 4, 5]: testQ.enqueue(x)
    print("Original:", testQ._qList)
    reverseQueue(testQ)
    print("Reversed:", testQ._qList)