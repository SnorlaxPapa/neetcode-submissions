"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        given a head, we must produce a deep copy of the list, that is no node in 
        the copied list must be referencing the original list

        for a linked list without a random pointer, this is simple enough
        create a new dummy node for each next pointer, and connect it to the next one

        however, for a random list, it is pointing to a random pointer. we must make sure 
        that the same node isn't being created because there is no sequence in random connections
        e.g. 
        3 2  1 4

        we can preserve the random index and the linked list in a list, and actively draw on this
        to get random index, need to set up a position lookup in the list
        we can create a non-random linked list copy first, store it in a list, then do a second pass through where we match the random indexes

        to deep copy a normal linked list, at each position, we copy the val first
        we  iterate to the next node, ini new node with only val, then set prev.next = curr node
        """
        if head is None: return None
        
        newHead = Node(head.val, None, None)
        curr = head.next
        currNew = newHead
        newList = [newHead]
        position = 1
        positionLookup = {head: 0}

        #deep copy non random array and save random indexes and set up position lookup
        while curr != None:
            newNext = Node(curr.val, None, None)
            currNew.next = newNext
            
            positionLookup[curr] = position
            newList.append(newNext)

            curr = curr.next
            currNew = currNew.next
            position += 1

        #find the position of the random indexes
        curr = head
        randomIndex = []
        while curr != None:
            if curr.random == None: randomIndex.append(None)
            else: randomIndex.append(positionLookup[curr.random])
            curr = curr.next

        #attach random to new linked list
        for index, node in enumerate(newList):
            randomNode = randomIndex[index]
            if randomNode == None: node.random = None
            else:
                # print(newList[randomNode].val)
                node.random = newList[randomNode]

        return newHead
        

