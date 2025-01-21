import random
import string
from open_addressing_hash_table import OpenAddressingHashtable

def effect_of_primary_clustering():
    hash_table = OpenAddressingHashtable(size=500)
    for _ in range(400):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
        hash_table.insert(random_string)
        if not _ % 50:
            print("-"*100)
            hash_table.visualize_table()
            print("-"*100)


    print(hash_table.load_factor())
    # hash_table.visualize_table()
    print(hash_table.runs_length())


def test_open_addressing_hashtable():
    hash_table = OpenAddressingHashtable()

    for item in ["link", "ilnk", "klin", "likn", "ilkn"]:
        hash_table.insert(item)

    print(hash_table)

    index = hash_table.search("link")
    print(index)

    index = hash_table.search("osdf")
    print(index)

    print(hash_table.load_factor())


if __name__ == "__main__":
    effect_of_primary_clustering()
    # test_open_addressing_hashtable()