from hypothesis import given, strategies as st


@given(st.integers())
def test_int_str_roundtripping(x):
    assert x == int(str(x))
