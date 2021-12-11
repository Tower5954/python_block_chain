from backend.util.crypto_hash import crypto_hash


def test_crypto_hash():
    """
    This should create the same hash with arguments of different data types in any order
    """
    assert crypto_hash(1, [2], 'three') == crypto_hash('three', 1, [2])
    assert crypto_hash('data') == '519b3ed503c6a825347f28dfd269c0a422e3b923858410e3abbab2d2a99837f2'