class TeaRankRewards:
    def __init__(self):
        self.ranks = {
            "initiate": 0,
            "connoisseur": 5,
            "master": 15,
            "grandmaster": 30
        }
        self.user_tea_counts = {}

    def add_tea_to_user(self, user, tea_type):
        if user not in self.user_tea_counts:
            self.user_tea_counts[user] = {tea_type: 0}
        self.user_tea_counts[user][tea_type] += 1

    def get_user_rank(self, user):
        total_tea_count = sum(self.user_tea_counts[user].values())
        for rank, required_tea_count in self.ranks.items():
            if total_tea_count >= required_tea_count:
                return rank
        return "initiate"
