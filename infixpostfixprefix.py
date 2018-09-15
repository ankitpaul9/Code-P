# from stack import Stack
from nose.tools import assert_equal

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

def parChecker(symbolString):
    # return True
    pass

def baseConverter(decNumber,base):
    pass

def infixToPostfix(infixexpr):
    pass

class TestStack(object):

    def testParCheckerMain(self):
        print('Test: ((()))')
        assert_equal(parChecker('((()))'), True)

        print('Test: (()')
        assert_equal(parChecker('(()'), False)
        print('Success: testParCheckerMain\n')

    def testBaseConverterMain(self):
        print('Test: 25,2')
        assert_equal(baseConverter(25,2), '11001')

        print('Test: 25,16')
        assert_equal(baseConverter(25,16), '19')
        print('Success: testBaseConverterMain\n')

    def testInfixToPostfixMain(self):
        print('Test: A * B + C * D')
        assert_equal(infixToPostfix("A * B + C * D"), 'A B * C D * +')

        print('Test: ( A + B ) * C - ( D - E ) * ( F + G )')
        assert_equal(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"), 'A B + C * D E - F G + * -')
        print('Success: testInfixToPostfixMain\n')


def main():
    test = TestStack()
    # test.testParCheckerMain()
    # test.testBaseConverterMain()
    # test.testInfixToPostfixMain()

if __name__ == '__main__':
    main()