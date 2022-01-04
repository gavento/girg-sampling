from girg_sampling import girgs, hypergirgs


def test_generate_girg():
    alpha = 100
    dim = 4
    n = 135
    deg = 4.2

    w = girgs.generateWeights(n, 1.5, seed=41)
    assert len(w) == n

    p = girgs.generatePositions(n, dim, seed=42)
    assert len(p) == n
    assert len(p[0]) == dim

    ws = girgs.scaleWeights(w, deg, dim, alpha)
    w = [x * ws for x in w]

    e = girgs.generateEdges(w, p, alpha, seed=43)
    assert len(e) > 0.8 * (n * deg / 2)
    assert len(e) < 1.2 * (n * deg / 2)


def test_generate_hypergirg():
    n = 1001
    alpha = 0.75
    t = 0.0
    deg = 2.2

    _ = hypergirgs.calculateRadiusLikeNetworKit(n, alpha, t, deg)
    r = hypergirgs.calculateRadius(n, alpha, t, deg)

    _radii = hypergirgs.sampleRadii(n, alpha, r, seed=22)
    _angles = hypergirgs.sampleAngles(n, seed=23)
    radii, angles = hypergirgs.sampleRadiiAndAngles(n, alpha, r, seed=42)
    assert len(_radii) == n
    assert len(_angles) == n
    assert len(radii) == n
    assert len(angles) == n

    e = hypergirgs.generateEdges(radii, angles, t, r, seed=43)
    # Note: HRG have lower than expected degree even for medium N
    assert len(e) > 0.65 * (n * deg / 2)
    assert len(e) < 1.2 * (n * deg / 2)
