from handypy.parallel import parallel, parallel_tqdm


def _mul2(x):
    return x * 2


def test_parallel():
    mul2p = parallel(_mul2)
    inp = [(i,) for i in range(100)]
    res = mul2p(inp)
    for i, j in zip(inp, res):
        assert i[0] * 2 == j, i

    mul2p = parallel_tqdm(_mul2)
    res = mul2p(inp)
    for i, j in zip(inp, res):
        assert i[0] * 2 == j, i
