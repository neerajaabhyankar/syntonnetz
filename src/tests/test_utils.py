import pytest
from synthoor.sound import key2freq, freq2key

TOL = 1e-6

def test_key2freq():
    assert abs(key2freq(60) - 261.63) < TOL  # Middle C
    assert abs(key2freq(57) - 220.003729) < TOL  # Middle A
    assert abs(key2freq(69) - 440.007458) < TOL # A4

def test_freq2key():
    assert abs(freq2key(261.63) - 60) < TOL  # Middle C
    assert abs(freq2key(220.003729) - 57) < TOL  # Middle A
    assert abs(freq2key(440.007458) - 69) < TOL # A4