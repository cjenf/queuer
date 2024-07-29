"""
Module to create a simple queue.
"""

from typing import List, Any


class queue:
    def __init__(self) -> None: 
        """
        Initializes a new instance of the Queue class.

        Returns:
            None
        """
        self.queue: List= []

    def push(self, item:Any) -> None:
        """Add an item to the queue"""
        self.queue.append(item)

    def get(self) -> Any:
        """Return the first item in the queue"""
        return self.queue.pop(0)
    
    def replace(self, item, new) -> None:
        """
        Exchange an item with another in the queue.

        Args:
            item (Any): The item to be exchanged.
            new (Any): The new item to replace the existing item.

        Raises:
            AssertionError: If the item is not found in the queue.

        Returns:
            None
        """
        assert item in self.queue, "Item not in queue"
        self.queue[self.queue.index(item)] = new

    def rotate(
            self, 
            *, 
            time:int=1
        ) -> None:
        """
        Rotates the queue by a given number of positions.

        Args:
            time (int, optional): The number of positions to rotate the queue by. Defaults to 1.

        Returns:
            None
        """
        match time:
            case _ if time>0:
                for _ in range(time):
                    last=self.queue.pop()
                    self.queue.insert(0,last)

            case _ if time<0:
                for _ in range(-time):
                    first=self.queue.pop(0)
                    self.queue.insert(len(self.queue)-1,first)

    def embed(self, index, item:Any) -> None:
        """Embed an item in the queue"""
        self.queue.insert(index, item)
        
    def current(self) -> Any:
        """Return the first item in the queue"""
        return self.queue[0]
    
    def is_empty(self) -> bool:
        """Return True if the queue is empty"""
        return len(self.queue) == 0
    
    def size(self) -> int:
        """Return the length of the queue"""
        return len(self.queue)
    
    def peak(self) -> Any:
        """Return the last item in the queue"""
        return self.queue[-1] if self.queue else None

    def delete(
            self, 
            *, 
            item:Any
        ) -> None:
        """Delete an item from the queue"""
        assert item in self.queue, "Item not in queue"
        self.queue.remove(self.queue.index(item))

    def clear(self) -> None:
        """Clear the queue"""
        self.queue.clear()

    def __repr__(self) -> str:
        """Return a string representation of the queue"""
        return f"queue({self.queue})"
    
    def __iter__(self):
        """Return an iterator for the queue"""
        return iter(self.queue)
