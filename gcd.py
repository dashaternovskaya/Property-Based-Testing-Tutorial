# 'given' is what we will use to tell 'Hypothesis' that a test function needs to be given data
# The submodule 'strategies' is the module that contains lots of tools that know how to generate data
from hypothesis import given, strategies as st


def gcd(n, m):
    """ Compute the GCD of two integers by Euclid's algorithm. """

    n, m = abs(n), abs(m)
    n, m = min(n, m), max(n, m)  # Sort their absolute values

    if not n:
        return m

    while m % n:         # While `n` doesn't divide into `m`:
        n, m = m % n, n  # update the values of `n` amd `m`
    return n


"""
A property-based test isn’t wildly different from a standard (pytest) test,
but there are some key differences. For example, instead of writing inputs
to the function gcd, we let Hypothesis generate arbitrary inputs.
Then, instead of hardcoding the expected outputs, we write assertions
that ensure that the solution satisfies the properties that it should satisfy.

Thus, to write a property-based test, you need to determine the properties
that your answer should satisfy.

If 'd' is the result of gcd(n, m), then it has the following properties:
    1) 'd' is positive;
    2) 'd' divides 'n';
    3) 'd' divides 'm'; and
    4) no other number larger than 'd' divides both 'n' and 'm'.
"""
@given(
    st.integers(min_value=1, max_value=100),
    st.integers(min_value=-500, max_value=500)
)  # The test function needs to be given one integer, and then another integer
def test_gcd(n, m):  # 'pytest' looks for functions that start with test_, so that is why our function is called test_gcd

    d = gcd(n, m)

    assert d > 0  # 1) `d` is positive
    assert n % d == 0  # 2) `d` divides `n`
    assert m % d == 0  # 3) `d` divides `m`

    # 4) No other number larger than `d` divides both `n` and `m`
    for i in range(d + 1, min(n, m)):
        assert (n % i) or (m % i)
