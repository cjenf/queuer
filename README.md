# queuer
Easily create queues.
## Install
```py
pip install queuer
```
## Usage
```py
import queuer

queue=queuer.queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)

print(queue) # output: queue(1, 2 ,3, 4 ,5)
```
## get the value of queue
```py
print(queue.get()) # output: 1
print(queue) ## output: queue(2, 3, 4, 5)
```
## Others
```py
queue.replace(2,6)
print(queue) # output: queue(6, 3, 4, 5)

queue.rotate(time=2)
print(queue) # output: queue(2, 5, 6, 3)

queue.embed(2,1)
print(queue) ## output: queue(2, 5, 1, 6, 3)

print(queue.current()) # output: 2

print(queue.is_empty()) # output : False

print(queue.size()) # output: 5

print(queue.peak()) # output: 3

queue.delete(item=2)
print(queue) # output: queue(5, 1, 6, 3)

queue.clear()
print(queue) # output: queue()
```
