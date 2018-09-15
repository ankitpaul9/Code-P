#!/usr/bin/env python


def testRun(llist):

  print "#------------------------------------------------#"
  print "# PRINT LIST                                     #"
  print "#------------------------------------------------#"
  print llist.items()
  print "#------------------------------------------------#\n"
  print "#------------------------------------------------#"
  print "# INSERT ELEMENT                                 #"
  print "#------------------------------------------------#"
  llist.insert(0, 12)
  llist.insert(1, 33)
  print llist.items()
  print "#------------------------------------------------#\n"
  print "#------------------------------------------------#"
  print "# APPEND ELEMENT                                 #"
  print "#------------------------------------------------#"
  llist.append(2)
  llist.append('w')
  llist.append("None")
  llist.append(3)
  llist.append(100)
  llist.append(200000)
  print """llist.append(2)
  llist.append('w')
  llist.append('None')
  llist.append(3)\n"""
  print llist.items()
  print "#------------------------------------------------#\n"
  print "#------------------------------------------------#"
  print "# LIST STRUCTURE                                 #"
  print "#------------------------------------------------#"
  print llist.items()
  print llist.list_tree()
  print "#------------------------------------------------#\n"
  print "#------------------------------------------------#"
  print "# LIST COUNT                                     #"
  print "#------------------------------------------------#"
  print llist.count()
  print llist.items()
  print "#------------------------------------------------#\n"
  print "#------------------------------------------------#"
  print "# GET ELEMENT                                    #"
  print "#------------------------------------------------#"
  print llist.items()
  print """llist.getelm(0)
           llist.getelm(6)\n"""
  print llist.getelm(0)
  print llist.getelm(3)
  print llist.getelm(5)
  print "#------------------------------------------------#\n"
  print "#------------------------------------------------#"
  print "# POP ELEMENT                                    #"
  print "#------------------------------------------------#"
  print llist.items()
  llist.popelm(3)
  print llist.items()
  llist.popelm(0)
  print llist.items()
  print "#------------------------------------------------#\n"



class Node(object):

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next_node

  def set_next(self, new_node):
    self.next_node = new_node


class Linkedlist(object):
  """
  # HEAD
  # Items
  # Insert
  # Append
  # Pop
  # get
  # count
  # Sort
  # Reverse
  """

  def __init__(self, head=None):
    self.head = head



  def list_tree(self):
    """
    This function return the linked list structure
    """
    current = self.head

    if current is None:
      return current

    item_s = ''
    while current:
      item_s += str(current.get_data()) + '-->'
      prev = current
      current = current.get_next()
      if not current:
        item_s += str(prev.get_next())
    return item_s


  def items(self):
    """
    This function return the linked list
    """
    current = self.head

    if current is None:
      return 0

    item = ''
    while current:
      item += str(current.get_data()) + ' '
      current = current.get_next()
    return item


  def append(self, node_data):
    """
    This function appends the data to the list
    """
    if not node_data:
      raise ValueError('Invalid Data provided')

    current = self.head
    prev = current

    while True:
      if current is None:
        new_node = Node(node_data)
        if self.head is None:
          self.head = new_node
          return
        prev.set_next(new_node)
        return

      prev = current
      current = current.get_next()


  def count(self):
    """
    This function returns the length of the list
    """
    current = self.head

    count = 0
    while current:
      count += 1
      current = current.get_next()

    return count


  def getelm(self, index):
    """
    This function to get element at a index
    """
    current = self.head
    count = self.count()

    if index >= count:
      raise IndexError('Invalid insert position provided')

    if not count:
      return None
    while True:
      if index == 0:
        return current.get_data()

      index -= 1
      current = current.get_next()

      if index < 0:
        print "No element found"
        return


  def insert(self, node_pos, node_data):
    """
    This function inserts the data to the list at a place
    """
    if self.head is None:
      count = 0
    else:
      count = self.count()

    if node_pos > count:
      raise IndexError('Invalid insert position provided')

    current = self.head
    prev = current

    while True:
      if node_pos == 0:
        new_node = Node(node_data)
        if self.head is None:
          self.head = new_node
          return
        prev.set_next(new_node)
        new_node.set_next(current)

      node_pos -= 1

      if node_pos < 0:
        break
      prev = current
      current = current.get_next()

    return


  def popelm(self, index):
    """
    This function to remove an element
    """
    current = self.head
    count = self.count()
    prev = None

    if index >= count:
      raise IndexError('Invalid insert position provided')

    if not count:
      print "The list is empty"
      return


    while True:
      if index == 0:
        item = current.get_data()
        current = current.get_next()
        if prev is not None:
          prev.set_next(current)
          return item
        self.head = current
        return item


      index -= 1
      prev = current
      current = current.get_next()

      if index < 0:
        print "No element found"
        return


  def sortls(self, reverse=False):
    count = self.count()
    if not count:
      print "The list is empty"
      return

    current = self.head

    while current:
      chk = current
      cnt = count - 1
      ls_current = current
      while ls_current:
        return


if __name__=='__main__':

  llist = Linkedlist()
  testRun(llist)
