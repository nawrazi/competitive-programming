# https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        state = 0
        count = {'Radiant': 0, 'Dire': 0}
        eliminated = set()

        for party in senate:
            if party == 'R':
                count['Radiant'] += 1
            else:
                count['Dire'] += 1

        while count['Radiant'] > 0 and count['Dire'] > 0:
            for member, party in enumerate(senate):
                if party == 'R' and member not in eliminated:
                    if state < 0:
                        eliminated.add(member)
                        count['Radiant'] -= 1
                    state += 1

                if party == 'D' and member not in eliminated:
                    if state > 0:
                        eliminated.add(member)
                        count['Dire'] -= 1
                    state -= 1

        return 'Radiant' if count['Radiant'] > 0 else 'Dire'
