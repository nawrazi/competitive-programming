# https://leetcode.com/problems/design-a-food-rating-system/

from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_data = {}
        self.ratings = defaultdict(SortedList)
        self.build(foods, cuisines, ratings)
        
    def build(self, foods, cuisines, ratings):
        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_data[food] = cuisine, rating
            self.ratings[cuisine].add((-rating, food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self.food_data[food]
        self.food_data[food] = cuisine, newRating
        self.ratings[cuisine].discard((-oldRating, food))
        self.ratings[cuisine].add((-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        return self.ratings[cuisine][0][1]
    
