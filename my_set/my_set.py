class MySet:
    def __init__(self, capacity=16, load_factor=0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _get_bucket_index(self, element):
        return hash(element) % self.capacity

    def add(self, element):
        if self.size >= self.load_factor * self.capacity:
            self._resize()
        index = self._get_bucket_index(element)
        bucket = self.buckets[index]
        if element in bucket:
            return False
        bucket.append(element)
        self.size += 1
        return True

    # def _resize(self):
    #     old_buckets = self.buckets
    #     self.capacity *= 2
    #     self.buckets = [[] for _ in range(self.capacity)]
    #     for bucket in old_buckets:
    #         for element in bucket:
    #             self.add(element)

    # fixed version of _resize to avoid double counting size
    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]

        # Переносим элементы вручную.
        # Мы не трогаем self.size, так как общее количество элементов не меняется
        for bucket in old_buckets:
            for element in bucket:
                index = self._get_bucket_index(element)
                self.buckets[index].append(element)

    def remove(self, element):
        index = self._get_bucket_index(element)
        bucket = self.buckets[index]
        if element not in bucket:
            return False
        bucket.remove(element)
        self.size -= 1
        return True

    def __contains__(self, element):
        index = self._get_bucket_index(element)
        bucket = self.buckets[index]
        return element in bucket

    def __len__(self):
        return self.size

    def __iter__(self):
        for bucket in self.buckets:
            for element in bucket:
                yield element

# a = 10
# b = 10
# print(a == b)