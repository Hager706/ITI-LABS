class queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def insert(self, value):
        self.items.append(value)  
    def pop(self):
        if self.is_empty():
            return None  
        return self.items.pop(0)  


#####################task2######################
class QueueOutOfRangeException(Exception):
    pass

class NamedQueue:
    all_queues = {}  
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.queue = []
        NamedQueue.all_queues[name] = self 
    
    def insert(self, value):
        if len(self.queue) >= self.size:
            raise QueueOutOfRangeException("Queue is full!")
        self.queue.append(value)
    
    def pop(self):
        if self.is_empty():
            print("Warning: Queue is empty")
            return None
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    @classmethod
    def get_queue(cls, name):
        return cls.all_queues.get(name)


if __name__ == "__main__":

    q1 = NamedQueue("queue1", 2)
    q2 = NamedQueue("queue2", 3)

    q1.insert("a")
    q1.insert("b")
    
  
    try:
        q1.insert("c")  
    except QueueOutOfRangeException:
        print("Queue is full!")
    

    print(q1.pop())  
    print(q1.pop()) 
    print(q1.pop()) 
    
    found_queue = NamedQueue.get_queue("queue1")
    print(f"Found queue: {found_queue.name}")


#####################task3######################

import urllib.request
import json

class WeatherClient:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_current_temperature(self, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data['current']['temp_c']
    
    def get_temperature_after(self, city, days, hour=None):
        url = f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={city}&days={days}"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        
        last_day = data['forecast']['forecastday'][-1]
        
        if hour is None:
            temps = []
            for h in last_day['hour']:
                temps.append(h['temp_c'])          
            return sum(temps) / len(temps)
        else:
            for h in last_day['hour']:
                if f"{hour:02d}:00" in h['time']:
                    return h['temp_c']
    
    def get_lat_and_long(self, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data['location']['lat'], data['location']['lon']
    
api_key = "c42dbde5b58b4d1f9d7112010251008"  
client = WeatherClient(api_key)

print(client.get_current_temperature("Cairo"))

print(client.get_temperature_after("Cairo", days=2, hour=14))

lat, lon = client.get_lat_and_long("Cairo")
print(f"Latitude: {lat}, Longitude: {lon}")