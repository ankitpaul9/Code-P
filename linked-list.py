from nose.tools import assert_equal

def testRun(llist):
  start_temp = \
  """
  #------------------------------------------------#
  # %s                                     #
  #------------------------------------------------#
  """
  end_temp = \
  """
  #------------------------------------------------#\n
  """

  print(start_temp % 'PRINT LIST')
  llist.print_list()
  print(end_temp)

  print(start_temp % 'INSERT ELEMENT')
  print("""
  llist.insert_to_front(12)
  llist.insert_to_front('a')""")
  llist.insert_to_front(12)
  llist.insert_to_front('a')
  llist.print_list()
  print(end_temp)
  
  print(start_temp % 'APPEND ELEMENT')
  print("""
  llist.append(2)
  llist.append('w')
  llist.insert_to_front('BB')
  llist.append('None')
  llist.append(3)\n""")
  llist.append(2)
  llist.append('w')
  llist.insert_to_front('BB')
  llist.append("None")
  llist.append(3)
  llist.append(100)
  llist.append(200000)
  llist.print_list()
  print(end_temp)

  print(start_temp % 'GET DATA')
  print(llist.get_all_data())
  print(end_temp)

  print(start_temp % 'FIND ELEMENT')
  print("""
  llist.find('w')
  llist.find('hello')""")
  llist.print_list()
  print(llist.find('w'))
  print(llist.find('hello'))
  print(end_temp)

  print(start_temp % 'LIST COUNT')
  llist.print_list()
  print('len =\t%s' % str(len(llist)))
  print(end_temp)

  print(start_temp % 'DELETE ELEMENT')
  print("""
  llist.delete('heelo')
  llist.delete('BB')
  llist.delete(3)
  llist.delete(200000)""")
  llist.print_list()
  llist.delete('heelo')
  llist.print_list()
  llist.delete('BB')
  llist.print_list()
  llist.delete(3)
  llist.print_list()
  llist.delete(200000)
  llist.print_list()
  print(end_temp)

class TestRemoveDupes(object):

    def test_remove_dupes(self, linked_list):
        print('Test: Empty list')
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One element list')
        linked_list.insert_to_front(2)
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [2])

        print('Test: General case, duplicates')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [1, 3, 2])

        print('Test: General case, no duplicates')
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [1, 3, 2])

        print('Success: test_remove_dupes\n')



class TestLinkedList(object):

    def test_insert_to_front(self):
        print('Test: insert_to_front on an empty list')
        linked_list = LinkedList(None)
        linked_list.insert_to_front(10)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(None)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: insert_to_front general case')
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        assert_equal(linked_list.get_all_data(), ['bc', 'a', 10])

        print('Success: test_insert_to_front\n')

    def test_append(self):
        print('Test: append on an empty list')
        linked_list = LinkedList(None)
        linked_list.append(10)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: append a None')
        linked_list.append(None)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: append general case')
        linked_list.append('a')
        linked_list.append('bc')
        assert_equal(linked_list.get_all_data(), [10, 'a', 'bc'])

        print('Success: test_append\n')

    def test_find(self):
        print('Test: find on an empty list')
        linked_list = LinkedList(None)
        node = linked_list.find('a')
        assert_equal(node, None)

        print('Test: find a None')
        head = Node(10)
        linked_list = LinkedList(head)
        node = linked_list.find(None)
        assert_equal(node, None)

        print('Test: find general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        node = linked_list.find('a')
        assert_equal(str(node), 'a')

        print('Test: find general case with no matches')
        node = linked_list.find('aaa')
        assert_equal(node, None)

        print('Success: test_find\n')

    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = LinkedList(None)
        linked_list.delete('a')
        assert_equal(linked_list.get_all_data(), [])

        print('Test: delete a None')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.delete(None)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: delete general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        linked_list.delete('a')
        assert_equal(linked_list.get_all_data(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete('aa')
        assert_equal(linked_list.get_all_data(), ['bc', 10])

        print('Success: test_delete\n')

    def test_len(self):
        print('Test: len on an empty list')
        linked_list = LinkedList(None)
        assert_equal(len(linked_list), 0)

        print('Test: len general case')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        assert_equal(len(linked_list), 3)

        print('Success: test_len\n')

class Node(object):

    def __init__(self,data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
    
    def __len__(self):
        curr_node = self.head
        count = 0
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next_node
        return count

    def append(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        curr_node = self.head
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node
        curr_node.next_node = node
        return

    def insert_to_front(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        curr_node = self.head
        node.next_node = curr_node
        self.head = node
        return
        
    
    def find(self, data):
        if data is None:
            return None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next_node         
        return None

    def delete(self, data):
        if data is None:
            return None
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next_node
            return
        prev_node = self.head
        curr_node = self.head.next_node
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next_node = curr_node.next_node
                return
            prev_node = curr_node
            curr_node = curr_node.next_node
    
    def print_list(self):
        curr_node = self.head
        lst = ''
        while curr_node is not None:
            lst += str(curr_node.data) + ' '
            curr_node = curr_node.next_node
        if self.head is not None:
            print(lst)

    def get_all_data(self):
        curr_node = self.head
        data = []
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next_node
        
        return data
        
class MyLinkedList(LinkedList):

    def remove_dupes(self):
            
        pass

if __name__=='__main__':
    llist = LinkedList()
    testRun(llist)
    test = TestLinkedList()
    test.test_insert_to_front()
    test.test_append()
    # test.test_find()
    test.test_delete()
    test.test_len()