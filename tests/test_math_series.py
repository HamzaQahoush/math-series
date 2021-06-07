from math_series import __version__
from math_series.math_series import fibonacci
from math_series.math_series import lucas
from math_series.math_series import sum_series

def test_version():
    assert __version__ == '0.1.0'



def test_Allfibonacci():
    a=[10,0,4,6,8]
    excepted = [55,0,3,8,21]
    for i in range (len(a)):
        assert fibonacci(a[i]) == excepted[i]



def test_fibonacci1():
    excepted=1
    actual= fibonacci(1)
    assert excepted==actual




def  test_lucas2():
 excepted= 3 
 actual = lucas(2)
 assert excepted== actual


def  test_lucas1():
  excepted= 1 
  actual = lucas(1)
  assert excepted== actual


def test_sum_fibonacci():  #0 1 1 2 3
  excepted =1
  actual= sum_series(2)
  assert excepted==actual


 # 3 4 7 11  lucas
def test_sum_Locas(): #2 1 3 4  fab
   
   excepted = 3
   actual= sum_series(2,2,1)
   assert excepted==actual


  

def test_sum_New(): #2 1 3 4 
    # 3 4 7 11 
   excepted = 7
   actual= sum_series(2,3,4)
   assert excepted==actual