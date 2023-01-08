class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # sort([
        #     [-5  0   0 a]
        #     [0  -2  -3 b]
        #     [0  -3  -2 c]
        # ])
        teams = sorted(votes[0])

        _map = {}
        for team in teams:
            _map[team] = [0] * len(teams) + [team]
        
        for vote in votes:
            for idx, team in enumerate(vote):
                _map[team][idx] -= 1
        
        ans = ""
        for val in sorted(_map.values()):
            ans += val[-1]
        
        return ans
        
        
        
