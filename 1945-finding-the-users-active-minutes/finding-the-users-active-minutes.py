class Solution:
    def findingUsersActiveMinutes(self, logs, k):
        # log = [id, time]
        mapping = {}
        for log in logs:
            user_id, minute = log
            if user_id not in mapping:
                mapping[user_id] = {minute}  # Use a set to store unique minutes
            else:
                mapping[user_id].add(minute)  # Add minute to the set

        # Initialize a list to count users with exactly i UAMs
        uam_counts = [0] * k
        for minutes in mapping.values():
            if 1 <= len(minutes) <= k:
                uam_counts[len(minutes) - 1] += 1  # Increment the count for the number of UAMs

        return uam_counts
