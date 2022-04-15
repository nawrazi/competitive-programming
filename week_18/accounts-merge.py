# https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def findParent(email):
            if email not in parents or parents[email] == email:
                return email
            parent = findParent(parents[email])
            parents[email] = parent
            return parent

        parents = {}
        names = {}
        for account in accounts:
            name = account[0]
            parent = account[1]
            for i in range(1, len(account)):
                email = account[i]
                if email in parents:
                    parent = findParent(email)
                    break

            for i in range(1, len(account)):
                email = account[i]
                parents[findParent(email)] = parent

            names[parent] = name

        allMails = defaultdict(set)
        for account in accounts:
            row_parent = findParent(account[1])
            for i in range(1, len(account)):
                allMails[row_parent].add(account[i])

        return [[names[k]] + sorted(v) for k, v in allMails.items()]
