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

print(queue) # output: queue(1, 2 ,3)
```
## get the value of queue
```py
print(queue.get()) # output: 1
print(queue) ## output: queue(2, 3)
```
