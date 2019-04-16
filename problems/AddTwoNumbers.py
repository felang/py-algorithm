# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class GuaList(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    @classmethod
    def create(cls, elements):
        node = GuaList(None)
        print('elements ', elements, len(elements),)

        for i in range(len(elements)):
            # print('value ', i)

            value = elements[len(elements)-i-1]
            print('value ', value)
            gua_list = GuaList(value)
            gua_list.next = node.next
            node.next = gua_list
        return node.next

    @staticmethod
    def printList(gua_list):
        list = gua_list
        while list != None:
            print(list.value)
            list = list.next
        print('\n')

    def sum(self):
        multi = 1
        list = self
        sum1 = 0
        while list != None:
            value = list.value * multi
            multi *= 10
            sum1 += value
            list = list.next
        return sum1

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return l1.sum() + l2.sum()


if __name__ == "__main__":
    list1 = GuaList.create([1, 2, 3])
    list2 = GuaList.create([4, 5, 6])
    # GuaList.printList(list1)
    a = list1.sum()
    s = Solution()
    print('sss', s.addTwoNumbers(list1, list2))
    # print(a)

    # print(c)
