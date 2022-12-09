
from pprint import pprint

def dict(n):
    return{'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)}

pprint([dict(i) for i in range(16)])
#