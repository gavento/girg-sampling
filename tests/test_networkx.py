from girg_sampling import girgs, hypergirgs


def test_generate_networkx_girg():
    alpha = 100
    dim = 4
    n = 135
    deg = 4.2
    g = girgs.generate_networkx_girg(n, 1.5, dim, deg, alpha, seed=41)
    assert g.order() == n
    assert g.size() > 0.8 * (n * deg / 2)
    assert g.size() < 1.2 * (n * deg / 2)


def test_generate_networkx_hrg():
    n = 1001
    alpha = 0.75
    t = 0.0
    deg = 2.2
    g = hypergirgs.generate_networkx_hrg(n, alpha=alpha, T=t, deg=deg, seed=42)
    # Note: HRG have lower than expected degree even for medium N
    assert g.order() == n
    assert g.size() > 0.65 * (n * deg / 2)
    assert g.size() < 1.2 * (n * deg / 2)
