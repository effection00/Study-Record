from sprint_challenge import Part_1
import hashlib


def test_part1():
    answer = Part_1.env_of_sc31()
    result = hashlib.md5(answer.encode())

    assert result.hexdigest() == '33072923312b8a609215e671417ac2e3'
