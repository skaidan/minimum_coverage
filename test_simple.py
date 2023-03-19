import file1
import file2

def test1():
    assert(file1.is_zero(3) == False)
    assert(file1.is_zero_wrapper(3) == False)

def test2():
    assert(file2.is_zero(0) == True)