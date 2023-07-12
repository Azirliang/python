from typing import Optional


class ListNode:
    def __init__(self,val: int):
        self.val:int = val
        self.next:Optional[ListNode]=None

def init() ->None:
    # 初始化链表 1-> 3 -> 2 -> 5 ->4
    # 初始化各个节点
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(5)
    n4 = ListNode(4)

    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4


def insert(a: ListNode,p:ListNode)->None:
    # 在链表的节点a之后插入节点p
    aNext = a.next
    p.next = aNext
    a.next = p

def remove(a:ListNode) -> None:
    # 删除链表的节点 a之后的首个节点
    if not a.next:
        return
    # a -> p -> b
    p = a.next
    b = p.next
    a.next = b

def access(head:ListNode,index:int )->Optional[ListNode]:
    # 访问链表中索引为index的节点
    for _ in range(index):
        if not head:
            return None
        head = head.next
        return head
    
def find(head:ListNode,target:int)->int:
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index +=1
    return -1
    
