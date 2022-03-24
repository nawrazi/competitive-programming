# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}
        lengths = { 0:-1 }
        cur_group = 0
        top_group_changed = (0,0)

        for i, let in enumerate(s):
            if let not in last_seen:
                cur_group += 1
                lengths[cur_group] = i
                last_seen[let] = [i, cur_group]
                top_group = cur_group

            else:
                while cur_group > last_seen[let][1]:
                    lengths.pop(cur_group)
                    cur_group -= 1

                if cur_group > top_group_changed[1] and top_group_changed[0] > last_seen[let][0]:
                    cur_group = top_group_changed[1]

                if top_group > cur_group:
                    top_group = cur_group
                    top_group_changed = (i, top_group)

                last_seen[let] = (i, cur_group)
                lengths[cur_group] = i

        keys = sorted(lengths.keys())
        final = []
        cur_max = -1

        for i in range(len(keys) - 1):
            diff = lengths[keys[i+1]] - lengths[keys[i]]
            if diff > 0 and lengths[keys[i+1]] > cur_max:
                final.append(diff)
                cur_max = lengths[keys[i+1]]

        return final
