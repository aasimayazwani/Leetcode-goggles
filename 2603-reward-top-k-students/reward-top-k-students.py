class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # something called positive and negative feedback 
        # positive and negative words are provided
        # add them to a individual dictionaries
        # if positive word += 3 
        # if negative word -=1 
        from collections import Counter
        positive = Counter(positive_feedback)
        negative = Counter(negative_feedback)
        report = [item.split(" ") for item in report]
        total = []
        for i in range(0,len(report)):
            total.append(self.feedback(report[i],positive,negative))
        score = {}
        for i in range(0,len(total)):
            if total[i] in score:
                score[total[i]].append(student_id[i])

            if total[i] not in score:
                score[total[i]] = [student_id[i]]

        keys = sorted(list(score.keys()),reverse=True)
        
        answer = []
        
        for i in range(0,len(keys)):
            answer.extend(sorted(score[keys[i]]))
            if len(answer) >= k:
                break
        return answer[0:k]



        
    def feedback(self,sentence,positive,negative):
        total = 0 
        for i in range(0,len(sentence)):
            word = sentence[i]
            if word in positive:
                total += 3 
            if word in negative:
                total -=1 
        return total



