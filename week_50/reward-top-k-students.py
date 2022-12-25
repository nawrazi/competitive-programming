# https://leetcode.com/problems/reward-top-k-students/description/

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        scores = []
        
        for sentence, student in zip(report, student_id):
            score = 0
            for word in sentence.split():
                if word in positive:
                    score += 3
                elif word in negative:
                    score -= 1
                    
            scores.append((-score, student))
            
        return [student for _, student in sorted(scores)][:k]
    
