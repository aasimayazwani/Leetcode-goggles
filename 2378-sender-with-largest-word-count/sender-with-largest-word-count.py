class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_count = {}
        for i in range(len(senders)):
            # Count the words in each message
            count = len(messages[i].split())
            if senders[i] in word_count:
                word_count[senders[i]] += count
            else:
                word_count[senders[i]] = count

        # Find the sender with the largest word count
        # In case of a tie, return the lexicographically largest name
        max_count = max(word_count.values())
        candidates = [sender for sender, count in word_count.items() if count == max_count]
        return max(candidates)