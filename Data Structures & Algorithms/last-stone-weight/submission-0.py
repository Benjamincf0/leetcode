class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [None]

        for stone in stones: heap.append(stone)

        def heapify(i: int, heap: List[int], size: int):
            l = 2*i
            r = 2*i+1

            biggest = i

            if l in range(size) and heap[l] > heap[biggest]:
                biggest = l

            if r in range(size) and heap[r] > heap[biggest]:
                biggest = r

            if biggest != i:
                # swap
                heap[biggest], heap[i] = heap[i], heap[biggest]
                heapify(biggest, heap, size)

        for i in range(len(heap)//2, 0, -1):
            heapify(i, heap, len(heap))

        count = len(stones)
        while count > 1:
            x = heap[1]
            heap[1] = float('-inf')
            heapify(1, heap, len(heap))

            y = heap[1]

            if x == y:
                heap[1] = float('-inf')
                heapify(1, heap, len(heap))
                count -= 2

            if x != y:
                heap[1] = x-y
                heapify(1, heap, len(heap))
                count -= 1

        return heap[1] if count != 0 else 0