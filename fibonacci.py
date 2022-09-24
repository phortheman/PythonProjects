"""
Fibonacci sequence function with caching

Author: phortheman
"""
import time
from functools import cache
from statistics import fmean

@cache
def fibonacci( n: int ) -> int:
    if n < 2:
        return n
    return fibonacci( n - 1 ) + fibonacci( n - 2 )

def main() -> None:

    values = []
    times = []
    for i in range( 0, 20000 ):
        tick = time.time()
        fibo = fibonacci( i )
        tock = time.time()
        milliseconds = ( tock - tick ) * 1000
        values.append( fibo )
        times.append( milliseconds )

    print( f"The Fibonacci Sequence was ran {len( times )} times" )
    print( f"The average time to peform was {fmean( times ):2f} milliseconds" )
    print( f"The longest time was {max( times ):2f} milliseconds" )
    print( f"The shortest time was {min( times ):2f} milliseconds" )

if __name__ == "__main__":
    main()