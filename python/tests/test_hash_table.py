import pytest
from linked_list.linked_list import LinkedList
from code_challenges.hashtable.hash_table import HashTable
@pytest.fixture 
def temp_hash_table():
    return HashTable()


def test_hash_instantiation_default_size(temp_hash_table):
    actual = len(temp_hash_table._bucket)
    expected = temp_hash_table._size
    assert actual == expected

def test_predictable_hash():
    hashtable = HashTable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary


def test_same_hash():
    hashtable = HashTable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary


def test_in_range_hash():
    hashtable = HashTable()
    actual = hashtable._hash('spam')

    # assert actual >= 0
    # assert actual < hashtable._size

    assert 0 <= actual < hashtable._size


def test_different_hash():
    hashtable = HashTable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary


def test_hashed_index(temp_hash_table):
    actual = temp_hash_table._hash('acb')
    expected = 106
    assert actual == expected


def test_hash_add_no_existing_value(temp_hash_table):
    temp_hash_table.add('acb', 'yelp')
    actual = temp_hash_table.contains('acb')
    expected = True
    assert actual == expected


def test_hash_add_existing_key(temp_hash_table):
    temp_hash_table.add('acb', 'hotmess')
    with pytest.raises(KeyError) as excinfo:
        temp_hash_table.add('acb', 'try')
    actual = str(excinfo.value)
    expected = "'hashtable already contains key: acb at the hashable index.'"
    assert actual == expected


def test_get_no_key_in_table(temp_hash_table):
    with pytest.raises(ValueError) as excinfo:
        temp_hash_table.get('abc')
    actual = str(excinfo.value)
    expected = 'no Key: abc found in Hashtable object'
    assert actual == expected


def test_get_key_exists(temp_hash_table):
    temp_hash_table.add('acb', 'yelp')
    actual = temp_hash_table.get('acb')
    expected = 'yelp'
    assert actual == expected


