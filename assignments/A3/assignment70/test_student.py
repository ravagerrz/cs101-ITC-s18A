try: 
    from a04 import uniqueEntries
except: 
    pass 


def test_uniqueEntries1():
    assert len(uniqueEntries([12, 24, 35, 24, 88, 120, 155, 88, 120, 155]))==2

def test_uniqueEntries2():
    
    assert uniqueEntries([12, 24, 35, 24, 88, 120, 155, 88, 120, 155])==([12, 24, 35, 88, 120, 155],[24, 88, 120, 155]) or [24, 88, 120, 155],[12, 24, 35, 88, 120, 155]
    
def test_uniqueEntries3():
    assert uniqueEntries('Morning')==(['M', 'o', 'r', 'n', 'i', 'g'], ['n']) or uniqueEntries('Morning')==(['n'],['M', 'o', 'r', 'n', 'i', 'g'])
def test_uniqueEntries4():
    assert uniqueEntries('Bubble Gum')==(['b', 'u'], ['B', 'u', 'b', 'l', 'e', ' ', 'G', 'm']) or (['B', 'u', 'b', 'l', 'e', ' ', 'G', 'm'], ['b', 'u'])

def test_uniqueEntries5():
    assert uniqueEntries('I love Python')== ([' ', 'o'], ['I', ' ', 'l', 'o', 'v', 'e', 'P', 'y', 't', 'h', 'n']) or (['I', ' ', 'l', 'o', 'v', 'e', 'P', 'y', 't', 'h', 'n'], [' ', 'o'])	

def test_uniqueEntries6():
    assert uniqueEntries(['a',12,'a','bb','b',12,'12'])==(['a', 12, 'bb', 'b', '12'], ['a', 12])

def test_uniqueEntries():
    try:
        uniqueEntries(None) == None
        assert False
    except TypeError:
        return

    assert False



# output capturing decorator
def capture_output(fn):
    def wrapper(*args, **kwargs):
        import StringIO
        import sys
        orig_stdout = sys.stdout
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput

        v = fn(*args, **kwargs)

        sys.stdout = orig_stdout # don't rely on __stdout__

        # print 'Captured', capturedOutput.getvalue()
        output_val = capturedOutput.getvalue()
        return v, output_val

    return wrapper



