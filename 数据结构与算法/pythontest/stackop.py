"""
    test Stack
"""
from pythonds.basic.stack import Stack


def test_stack():
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())


def par_checker(symbol_string):
    """
        输入的括号是否匹配，可以检测([{的匹配
    """
    def matches(left_symbol, right_symbol):
        """
            输入的参数必须是([{}])之一
        """
        left = '([{'
        right = ')]}'
        return left.index(left_symbol) == right.index(right_symbol)

    s = Stack()
    for symbol in symbol_string:
        if symbol in '([{':
            s.push(symbol)
        elif symbol in ')]}':
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False
    if s.is_empty():
        return True
    else:
        return False


def main():
    sym_str = "((([]){}(ji))j())"
    print(par_checker(sym_str))


if __name__ == "__main__":
    main()
