# n개의 원소, w의 넓이를 가지는 창문
import heapq
import queue, copy
from collections import deque

#  Basic
class Basic:
  cnt = 0

  def __init__(self, elements: [], w: int):
    self.els = elements
    self.w = w

    Basic.cnt += 1
    self._id = Basic.cnt

  def __call__(self):

    # for i in range(end, len(self.els)):
    #   temp = []
    #   for j in range(i-self.w, i):
    #     temp.append(j)
    #   print(temp)
    #   start += 1
    
    q = deque([])
    for i in self.els:
      q.append(i)
      if len(q) >self.w:
        q.popleft()
      
      print(q)

  def show(self):
    print('===== 기초 - %d/%d ====='%(self._id, Basic.cnt))
    print('n개의 원소: %s, 윈도우 크기: %d'%(self.els, self.w))
    self()

# 구간합 - O(원소갯수)
class SubSum:
  cnt = 0

  def __init__(self, elements: [], w: int):
    self.els = elements
    self.w = w
    self.answer = []
    
    SubSum.cnt += 1
    self._id = SubSum.cnt

  def __call__(self):
    q = deque([])
    s = 0
    sums = []
    for i in self.els:
      q.append(i)
      s += i
      if len(q) >self.w:
        removed_v = q.popleft()
        s -= removed_v
      sums.append(s)
    self.answer = sums

  def show(self):
    print('===== 구간합 - %d/%d ====='%(self._id, SubSum.cnt))
    print('n개의 원소: %s, 윈도우 크기: %d'%(self.els, self.w))
    print('정답: %s'%(self.answer))
    print('')


# 아나그램(Anagram) - O(원소갯수)
#   한 단어를 구성하는 글자의 개수를 그대로 유지하면서 순서만 바꾼 단어
#   예) listen-silent, aab-baa
class Anagram:
  cnt = 0
  def __init__(self, s1: str, s2: str):
    self.els = s1
    self.w = s2

    Anagram.cnt += 1
    self._id = Anagram.cnt

    self.word_map = self.set_word_map()
    self.answer = 0

    print(self.word_map)

  def set_word_map(self):
    temp = {}
    cnt = 0

    for word in self.w:
      temp.setdefault(word, 0)
      temp[word] += 1
      cnt += 1
    
    temp.update({'total_cnt': cnt})
    return temp

  def __call__(self):
    q = deque([])
    result = 0
    for word in self.els:
      q.append(word)
      self.decrese(word)
      
      if len(q) > len(self.w):
        removed_v = q.popleft()
        self.increse(removed_v)

      if not self.word_map['total_cnt']:
        result += 1

    self.answer = result

  def increse(self, word):
    try:
      self.word_map[word] += 1
      self.word_map['total_cnt'] += 1
    except:
      pass
  
  def decrese(self, word):
    try:
      self.word_map[word] -= 1
      self.word_map['total_cnt'] -= 1
    except:
      pass

  def show(self):
    print('===== 아나그램 - %d/%d ====='%(self._id, Anagram.cnt))
    print('문자열 1: %s'%(self.els))
    print('문자열 2: %s'%(self.w))
    print('정답: %d'%(self.answer))
    print()

# 구간 최소값 - O(원소갯수)
class SumMin:
  cnt = 0

  def __init__(self, els: list, w: int):
    self.els = els
    self.w = w
    self.answer = []
    
    SumMin.cnt += 1
    self._id = SumMin.cnt

  def __call__(self):
    end = 0
    start= end - self.w + 2
    result = []
    q=deque([])

    while end < len(self.els):
      prev_el = self.get_el(start-1)
      added_el = self.get_el(end)

      if len(q) and prev_el == q[0]:
        q.popleft()

      if len(q) == 2 and added_el < q[1]:
        q.pop()

      if len(q) < 2:
        q.append(added_el)

      m_v = self.get_min(q)

      result.append(m_v)
      end += 1
      start += 1

    self.answer = result

  def get_min(self, q):
    if not len(q):
      return -1

    if len(q) == 1:
      return q[0]
    else:
      return q[0] if q[0] < q[1] else q[1]

  def get_el(self, idx):
    return 0 if idx < 0 else self.els[idx]

  def show(self):
    print('===== 구간 최소값 - %d/%d ====='%(self._id, SumMin.cnt))
    print('n개의 원소: %s, 윈도우 크기: %d'%(self.els, self.w))
    print('정답: %s'%(self.answer))
    print('')

if __name__ == "__main__":
  
  sw0 = SubSum([1,2,3,4,5,6,7,8,9], 4)
  sw0()
  
  sw1 = SubSum([1,2,4,5,6,7,8,9, 3, 11], 2)
  sw1()
  
  a0 = Anagram("listen", "silent")
  a0()

  a1 = Anagram("lisrten", "silent")
  a1()
  
  a2 = Anagram("Only lower alphabet characters are allowed", "a")
  a2()
  
  sm0 = SumMin([9, 8, 7, 6, 8, 1], 4)
  sm0()


  sw0.show()
  sw1.show()

  a0.show()
  a1.show()
  a2.show()

  sm0.show()

  b0 = Basic([1,2,3,4,5,6,7], 1)
  b1 = Basic([1,2,3,4,5,6,7], 2)
  b2 = Basic([1,2,3,4,5,6,7], 3)
  
  b0.show()
  b1.show()
  b2.show()