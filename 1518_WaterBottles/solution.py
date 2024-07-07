class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        totalBottles = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            newBottles = emptyBottles // numExchange
            totalBottles += newBottles
            emptyBottles = newBottles + (emptyBottles % numExchange)
        
        return totalBottles