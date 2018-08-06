def sort(func):
    def sort_array():
        return sorted(func())
    return sort_array


@sort
def data_feeder():
    return [4, 2, 1, 3]


def main():
    print(data_feeder())
    print(data_feeder() == [1, 2, 3, 4])


if __name__ == '__main__':
    main()
