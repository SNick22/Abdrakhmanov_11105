import typing
from functools import partial


def calculate(a1: int, a2: str, a3: int, a4: str, a5: int, a6: str, a7: int, a8: str, a9: int) -> float or int:
    return eval(str(a1) + a2 + str(a3) + a4 + str(a5) + a6 + str(a7) + a8 + str(a9))


def cur_calculate(a1: int) -> typing.Callable:
    def calc2(a2: str) -> typing.Callable:
        def calc3(a3: int) -> typing.Callable:
            def calc4(a4: str) -> typing.Callable:
                def calc5(a5: int) -> typing.Callable:
                    def calc6(a6: str) -> typing.Callable:
                        def calc7(a7: int) -> typing.Callable:
                            def calc8(a8: str) -> typing.Callable:
                                def calc9(a9: int) -> int or float:
                                    return eval(str(a1) + a2 + str(a3) + a4 + str(a5) + a6 + str(a7) + a8 + str(a9))
                                return calc9
                            return calc8
                        return calc7
                    return calc6
                return calc5
            return calc4
        return calc3
    return calc2


if __name__ == '__main__':
    print(calculate(2, '/', 3, '+', 4, '+', 5, '*', 6))
    print(cur_calculate(2)('/')(3)('+')(4)('+')(5)('*')(6))
    new_func = partial(calculate, a1=2, a3=5, a5=1, a7=8, a9=0)
    print(new_func(a2='+', a4='+', a6='+', a8='+'))
    print(new_func(a2='-', a4='+', a6='/', a8='*'))
    print(new_func(a2='-', a4='-', a6='-', a8='-'))

