import girg_sampling


def test_generate_weights():
    w = girg_sampling.generateWeights(11, 1.5)
    assert len(w) == 11
