try: 
    from a02 import netIncome
except: 
    pass 

def test_netIncome():
    assert netIncome(20000,1)==19800.0
def test_netIncome2():
    assert type(netIncome(20000))==float
def test_netIncome3():
    assert netIncome(2234,0.23)==2228.8618
    
