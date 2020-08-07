import pytest
import rlp
from rlp import decode
from rlp.codec import encode_raw
from target.release import rusty_rlp


@pytest.mark.parametrize(
    'input',
    (
        b'',
        b'asdf',
        b'fds89032#$@%',
        b'dfsa',
        [b'dfsa', b''],
        [],
        [b'fdsa', [b'dfs', [b'jfdkl']]],
        # https://etherscan.io/block/400000
        [b'\x1ew\xd8\xf1&sH\xb5\x16\xeb\xc4\xf4\xda\x1e*\xa5\x9f\x85\xf0\xcb\xd8S\x94\x95\x00\xff\xac\x8b\xfc8\xba\x14', b'\x1d\xccM\xe8\xde\xc7]z\xab\x85\xb5g\xb6\xcc\xd4\x1a\xd3\x12E\x1b\x94\x8at\x13\xf0\xa1B\xfd@\xd4\x93G', b'*e\xac\xa4\xd5\xfc[\\\x85\x90\x90\xa6\xc3M\x16A59\x82&', b'\x0b^C\x86h\x0fC\xc2$\xc5\xc07\xef\xc0\xb6E\xc8\xe1\xc3\xf6\xb3\r\xa0\xee\xc0rr\xb4\xe6\xf8\xcd\x89', b'V\xe8\x1f\x17\x1b\xccU\xa6\xff\x83E\xe6\x92\xc0\xf8n[H\xe0\x1b\x99l\xad\xc0\x01b/\xb5\xe3c\xb4!', b'V\xe8\x1f\x17\x1b\xccU\xa6\xff\x83E\xe6\x92\xc0\xf8n[H\xe0\x1b\x99l\xad\xc0\x01b/\xb5\xe3c\xb4!', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x05zA\x8a|>', b'\x06\x1a\x80', b'/\xef\xd8', b'', b'V"\xef\xdc', b'\xd5\x83\x01\x02\x02\x84Geth\x85go1.5\x85linux', b'?\xbe\xa7\xafd*N \xcd\x93\xa9E\xa1\xf5\xe2;\xd7/\xc5&\x11S\xe0\x91\x02\xcfq\x89\x80\xae\xff8', b'j\xf2<\xaa\xe9V\x92\xef'],
    )
)
def test_foo(input):
    pyrlp_encoded = encode_raw(input)
    pyrlp_decoded = decode(pyrlp_encoded)
    rustyrlp_decoded = rusty_rlp.decode_raw(pyrlp_encoded)

    assert pyrlp_decoded == input
    assert rustyrlp_decoded == input