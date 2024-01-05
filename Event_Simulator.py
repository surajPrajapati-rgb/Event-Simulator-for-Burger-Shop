from linked_queue import *
from linked_stack import *
import circular_queue as C

class Error(BaseException):
    pass

class Customer:
    def __init__(self, id, t, numb):
        self.id = id
        self.arrival = t
        self.burgers = numb
        self.waitingtime = 0
        self.queue = None
        self.state = None

class Simulator():
    def __init__(self):
        self._statusK = False
        self._statusM = False
        self._k = 0
        self._max_burger = 0
        self.billing_queue = []
        self._clock = 0
        self._customers = []

    def isEmpty(self):
        if self:
            return 1    
        return 
    
    def setK(self, k):
        if self._statusK:
            return Error("Can't modify further")
        self._statusK = True
        self._k = k
        for i in range(k):
            Q = C.CircularQueue()
            self.billing_queue.append(Q)

    def setM(self, m):
        if self._statusM:
            return Error("Cant be modified")
        else:
            self._statusM = True
            self._max_burger = m
        
    def advanceTime(self, t):
        """Runs the simulation forward simulating all events upto (including) time t"""
        if t < self._clock:
            return Error("Time can not move backward")

        for i in range(self._clock, t):
            self._clock += 1
            self.remove_customer()
            for i in range(len(self._customers)):
                if self._clock >= self._customers[0].arrival:
                    self.addCustomer(self._customers[0])
                    self._customers.remove(self._customers[0])
                   
    def addCustomer(self, customer):
        min_queue = 0
        min_len = len(self.billing_queue[0])
        for i in range(1, self._k):
            if len(self.billing_queue[i]) < min_len:
                min_queue = i
                min_len = len(self.billing_queue[i])

        if min_len == 0:
            customer.waitingtime = customer.arrival + min_queue + 1
        else:
            customer.waitingtime = customer.arrival + (min_queue+1)*min_len + self.billing_queue[min_queue].first().waitingtime - self._clock
        self.billing_queue[min_queue].enqueue(customer)
        print(f"Customer {customer.id}: Counter : {min_queue+1}; {customer.arrival}/{customer.waitingtime}")


    def remove_customer(self):
        for counter in self.billing_queue:
            if len(counter) != 0:
                customer = counter.first()
                if self._clock >= customer.waitingtime:
                    counter.dequeue()
                    # print(f"Customer {customer.id}: {self.billing_queue.index(counter)}/{self._clock}")
        
    def arriveCustomer(self, id, t, numb):
        """
        A customer with ID = id arrives at time t and orders numb number of burgers. The function
        returns with appropriate error messages in the following scenarios:
            ● the arrival time of a customer is lower than that of a previous customer
            ● numb is negative
            ● the IDs are not consecutive
        """

        if t < self._clock:
            return Error("The arrival time is lower than that of a previous customer")
        
        if numb < 0:
            return Error("Number of burgers cant be negative")
        
        if id in self._customers:
            return Error("already exists")
        
        customer = Customer(id, t, numb)
        self._customers.append(customer)


    def customerState(self, id,  t):
        """
        Prints the state of the customer with ID = id at time t. Outputs 0 if the customer has not yet
        arrived; the queue number k (between 1 and K) if the customer is waiting in the kth billing queue;
        k+1 if the customer is waiting for food; k+2 if the customer has received her order by time t. The
        function returns with an appropriate error message if the value of t is smaller than that in the
        previous command
        """
        pass

    def griddleState( t):
        pass
    def griddleWait(t):
        pass

    def customerWaitTime(id):
        pass
    def avgWaitTime():
        pass


# s = Simulator()
# s.setK(3)
# s.setM(6)
# s.arriveCustomer(1,0,2)
# s.arriveCustomer(2,0,1)
# s.arriveCustomer(3,0,3)
# s.arriveCustomer(4,1,3)
# s.advanceTime(1)


# s = Simulator()
# s.setK(3)
# s.setM(5)
# s.arriveCustomer(1,5,2)
# s.arriveCustomer(2,10,1)
# s.arriveCustomer(3,11,3)
# s.arriveCustomer(4,12,1)
# s.advanceTime(5)
# s.advanceTime(8)
# s.advanceTime(11)
# s.advanceTime(18)


s = Simulator()
s.setK(2)
s.setM(5)
s.arriveCustomer(1,1,1)
s.arriveCustomer(2,1,1)
s.arriveCustomer(3,1,3)
s.arriveCustomer(4,2,1)
s.arriveCustomer(5,2,1)
s.arriveCustomer(6,3,1)
s.arriveCustomer(7,3,1)
s.advanceTime(1)
s.advanceTime(2)
# s.advanceTime(3) 
# s.advanceTime(4)
# s.advanceTime(5)
# s.advanceTime(6)
# s.advanceTime(7) 





