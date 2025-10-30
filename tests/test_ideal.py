from rocket_relations import c_star, c_f

def test_c_star_nominal():
    val = c_star(1.2, 350.0, 3500.0)
    assert 500 < val < 700

def test_c_f_nominal():
    val = c_f(1.2, 0.4, 0.2, 10.0)
    assert 2 < val < 3
