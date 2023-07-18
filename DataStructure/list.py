def merge(list1:list[int],list2:list[int]):
    return list1 + list2


class MyClass:
    def __init__(self) -> None:
        self.__capacity:int =10 #列表容量
        self.__nums :list[int] = [0]*self.__capacity
        self.__size:int = 0 # 列表长度
        self.__extend_ratio:int =2 # 每次列表扩容的倍数

    def size(self)->int:
        return self.__size
    
    def capacity(self)->int:
        return self.__capacity
    
    def get(self,index:int)->int:
        if index<0 or index>=self.__size:
            raise IndexError("索引越界")
        return self.__nums[index]
    
    def set(self,num:int,index:int)->None:
        if index<0 or index>=self.__size:
            raise IndexError("索引越界")
        self.__nums[index] = num

    def add(self,num:int)->None:
        # 尾部添加元素
        if self.size() == self.capacity():
            self.extend_capacity()
        self.__nums[self.__size] = num
        self.__size+=1
        
    def insert(self,num:int,index:int)->None:
        # 中间插入
        if index<0 or index>=self.__size:
            raise IndexError("索引越界")
        if self.size() == self.capacity():
           self.extend_capacity()

        for j in range(self.__size-1,index-1,-1):
            self.__nums[j+1] = self.__nums[j]
        self.__nums[index] = num
        self.__size +=1

    def remove(self,index:int)->int:
        if index<0 or index>=self.__size:
            raise IndexError("索引越界")
        num = self.__nums[index]

        for j in range(index, self.__size - 1):
            self.__nums[j] = self.__nums[j + 1]
        self.__size -= 1
        return num
    
    def extend_capacity(self)->None:
        self.__nums = self.__nums + [0]*self.capacity() * (self.__extend_ratio-1)

    def to_array(self)->list[int]:
        return self.__nums[:self.__size]

        
     
        