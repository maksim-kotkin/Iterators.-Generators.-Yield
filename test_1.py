class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.iter_list = iter(self.list_of_list)
        self.new_list = []
        self.cursor = -1
        return self


    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.new_list):
             self.new_list = next(self.iter_list)
             self.cursor = 0
        return self.new_list[self.cursor]
    
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    print(list(FlatIterator(list_of_lists_1)))
if __name__ == '__main__':
    test_1()