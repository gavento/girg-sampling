from girg_sampling import girgs, hypergirgs


def test_generate_weights():
    w = girgs.generateWeights(11, 1.5)
    assert len(w) == 11
