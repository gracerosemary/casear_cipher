from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt, decrypt, word_check, crack

def test_version():
    assert __version__ == '0.1.0'

def test_encrpyt_oneAlpha_smallShift():
    key = 1
    plain = 'a'
    actual = encrypt(plain, key)
    expected = 'b'
    assert actual == expected

def test_encrpyt_multAlpha_medShift():
    key = 12
    plain = 'abc'
    actual = encrypt(plain, key)
    expected = 'mno'
    assert actual == expected

def test_encrpyt_multAlpha_bigShift():
    key = 25
    plain = 'abc'
    actual = encrypt(plain, key)
    expected = 'zab'
    assert actual == expected

def test_encrpyt_multAlpha_Upper():
    key = 25
    plain = 'AbCdEf'
    actual = encrypt(plain, key)
    expected = 'ZaBcDe'
    assert actual == expected

def test_decrpyt_oneAlpha_smallShift():
    key = 1
    plain = 'b'
    actual = decrypt(plain, key)
    expected = 'a'
    assert actual == expected

def test_decrpyt_multAlpha_medShift():
    key = 12
    plain = 'mno'
    actual = decrypt(plain, key)
    expected = 'abc'
    assert actual == expected

def test_decrpyt_multAlpha_bigShift():
    key = 25
    plain = 'zab'
    actual = decrypt(plain, key)
    expected = 'abc'
    assert actual == expected

def test_decrpyt_multAlpha_Upper():
    key = 25
    plain = 'AbCdEf'
    actual = decrypt(plain, key)
    expected = 'BcDeFg'
    assert actual == expected

def test_crack_best_worst():
    check_word = 'kv ycu vjg dguv qh vkogu, kv ycu vjg yqtuv qh vkogu.'
    actual = crack(check_word)
    expected = 'it was the best of times, it was the worst of times.'
    assert actual == expected

def test_crack_one_word():
    check_word = 'tbe'
    actual = crack(check_word)
    expected = 'sad'
    assert actual == expected

def test_crack_song():
    check_word = 'vykpmng vykpmng nkvvng uvct'
    actual = crack(check_word)
    expected = 'twinkle twinkle little star'
    assert actual == expected