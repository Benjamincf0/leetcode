class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0: return False
        counts = defaultdict(int)
        min_heap = []

        for card in hand:
           if card not in counts: heapq.heappush(min_heap, card)
           counts[card]+=1

        while min_heap:
            card = heapq.heappop(min_heap)
            while counts[card] == 0 and min_heap:
                card = heapq.heappop(min_heap)

            num = counts[card]
            for i in range(card, card+groupSize):
                counts[i]-=num
                if counts[i]<0: return False

        return True