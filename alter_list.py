#!/usr/bin/env python

import string


def slice_non_recursive(string, size=1):
  if not size:
    return string
  return [string[idx:idx+size] for idx in range(0, len(string), size)]

def slice_recursive(string, size=1):
  lst_item = []
  if not size:
    return string
  def dice_lst(string, size):
    if not len(string):
      return

    lst_item.append(string[:size])
    return dice_lst(string[size:], size)

  dice_lst(string, size)

  return lst_item

def slice_recursiveV2(string, size=1, lst_item=None):
  if not size:
    return string

  if lst_item is None:
    lst_item = []

  if len(string):
    lst_item.append(string[:size])
    return slice_recursiveV2(string[size:], size, lst_item)
  else:
    return lst_item

def speed_test(cmd):
  from datetime import datetime

  a = datetime.now()
  ia = cmd
  b = datetime.now()
  c = b - a
  print str(c.seconds) + " seconds, " + str(c.microseconds) + " micoseconds"
  return ia

def getMatches(alphaMap, number, match_lst=None):
  """
  input = 12
  output = ad, ae,af,bd,be,bf,cd,ce,cf

  input = 239
  output = dgy, dgz, dg$, dhy, dhz, dh$, diy, diz ,.........

  input = 3
  output = g, h, i
  """
  import itertools
  if match_lst is None:
    match_lst = []
  order = list(str(number))
  cart = [list(alphaMap[int(x)-1]) for x in order]
  #iresult = list(itertools.product(*cart) )
  #print iresult
  r = [[]]
  for x in cart:
    sl = []
    for j in x:
      for i in r:
        sl.append(i + [j])
    r = sl

  return ["".join(x) for x in r]

alphaString = string.ascii_lowercase + '$'
# speed_test(slice_non_recursive(alphaString, 3))

alphaMap = slice_recursiveV2(alphaString, 3)

num = 12
#getMatches(alphaMap, num
print speed_test(getMatches(alphaMap, num))
num = 239
#getMatches(alphaMap, num)
a = speed_test(getMatches(alphaMap, num))
a.sort()
print a
