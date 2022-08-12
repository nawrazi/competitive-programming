# https://leetcode.com/problems/sender-with-largest-word-count/

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        words = defaultdict(int)
        for i, message in enumerate(messages):
            words[senders[i]] += len(message.split())
            
        pairs = sorted([(v, k) for k, v in words.items()])
        return pairs[-1][1]
    
