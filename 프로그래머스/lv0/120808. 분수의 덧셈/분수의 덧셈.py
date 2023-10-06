from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    
    bunmo=denom1*denom2
    bunza1=numer1*denom2
    bunza2=numer2*denom1
    bunza=bunza1+bunza2
    bunsu=Fraction(bunza, bunmo)
    
    answer = [bunsu.numerator, bunsu.denominator]
    
    return answer