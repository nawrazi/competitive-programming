# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        requirements = defaultdict(int)
        q = deque(supplies)
        creatable = []

        for i, recipe in enumerate(recipes):
            for ing in ingredients[i]:
                graph[ing].append(recipe)
            requirements[recipe] = len(ingredients[i])

        while q:
            item = q.popleft()

            for rec in graph[item]:
                requirements[rec] -= 1
                if requirements[rec] == 0:
                    q.append(rec)
                    creatable.append(rec)

        return creatable
