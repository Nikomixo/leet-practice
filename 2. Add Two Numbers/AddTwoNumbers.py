#linked list node def
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

#create linked list from array
def createLinkedList(values: list[int]) -> ListNode:
    init_node = ListNode(val=values[0])
    head = init_node
    for i in range(1, len(values)):
        head.next = ListNode(val=values[i])
        head = head.next
    return init_node

# print linked list as in array notation
def printLinkedList(head: ListNode):
    strArr = "["

    while head.next != None:
        strArr += str(head.val) + ","
        head = head.next
    strArr += str(head.val) + "]"

    print(strArr)

# Initial solution: digit-wise addition
def AddTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # add first digit together
    
    digit = (l1.val + l2.val) % 10
    print(f"{l1.val} + {l2.val} = {digit}")
    carryover = (l1.val + l2.val) / 10
    l1, l2 = l1.next, l2.next

    #create head node
    tail = ListNode(val=digit)
    head = tail

    # loop through rest of digits until one list runs out
    while l1 is not None and l2 is not None:
        digit = int((l1.val + l2.val + carryover) % 10)
        carryover = (l1.val + l2.val + carryover) / 10

        tail.next = ListNode(val=digit)
        tail = tail.next

        l1, l2 = l1.next, l2.next

    # add l1 until depleted
    while l1 is not None:
        digit = int((l1.val + carryover) % 10)
        carryover = (l1.val + carryover) / 10

        tail.next = ListNode(val=digit)
        tail = tail.next
        l1 = l1.next

    # add l2 until depleted
    while l2 is not None:
        digit = int((l2.val + carryover) % 10)
        carryover = (l2.val + carryover) / 10

        tail.next = ListNode(val=digit)
        tail = tail.next
        l2 = l2.next

    # check carryover
    if int(carryover) > 0:
        tail.next = ListNode(val=int(carryover))

    # return head
    return head


# 327 + 9824 = 10151
# sol = [1,5,1,0,1]
l1 = createLinkedList([7,2,3])
l2 = createLinkedList([4,2,8,9])

printLinkedList(AddTwoNumbers(l1, l2))


