import urllib
import requests
import random
from unittest import TestCase

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def pad(words,max_len):

  for x in range(len(words)):
    if(isinstance(words[x],str)):
      words[x] = str.encode(words[x])
    words[x] += bytes(max_len-len(words[x]))

def countsort(words, pos, max_len):

  counts = [0] * 128
  out = [0] * len(words)
  for i in words:
    counts[i[pos]] += 1
  for y in range(1,len(counts)):
    counts[y] = counts[y] + counts[y-1]
  for x in reversed(words):
    out[counts[x[pos]]-1] = x 
    counts[x[pos]] -= 1
  return out

def radixsort(words):
  max_len = max([len(i) for i in words])
  pad(words,max_len)

  for i in range(max_len-1,-1,-1):
    words = countsort(words, i, max_len)

  words = [w.decode("utf-8").rstrip('\x00').encode('ascii','replace') for w in words]
  return words


def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    bookwords = book_to_words()
    bookwords = radixsort(bookwords)
    return bookwords


################################################################################
# TEST CASES
################################################################################

tc = TestCase()

################################################################################
# RADIX SORT TEST CASE:
################################################################################

print("Starting radix sort test....\n")
samplelist = [str(random.randint(1,10000000)).encode() for _ in range(1000000)]
tc.assertEqual(sorted(samplelist), radixsort(samplelist))
print("RADIX SORT SUCCESS!!!!!!!!!\n\n\n")

################################################################################
# RADIX BOOK SORT TEST CASE:
################################################################################

print("Starting radix sort book test....\n")
samplebook = book_to_words()
tc.assertEqual(sorted(samplebook), radix_a_book())
print("RADIX SORT BOOK SUCCESS!!!!!!!!!\n\n")
print("#############################\nEVERYTHING WORKS!!!!!!!!!!!!!!!!!!!\n#############################")
