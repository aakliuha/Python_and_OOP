class NotOnlyStringException(Exception):
    pass



def get_elements(*args):
    els = list(args)
    assert 'b' in els

    for i in els:
        if type(i) is not str:
            raise NotOnlyStringException("Invalid input type. Should by string only")


get_elements('t', 'y', 'z', 'a', 'w', 'b', 1)