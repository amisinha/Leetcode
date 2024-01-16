class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = set()
        loss_c = 0
        losser = []
        one_loss = []
        for p in matches:
            if p[0] not in winner:
                winner.add(p[0])
        for p in matches:
            losser.append(p[1])
            if p[1] in winner:
                winner.remove(p[1])
        
        freq_loss = Counter(losser)
        team = list(freq_loss.keys())
        team_val = list(freq_loss.values())
        for v in range(len(team_val)):
            
            if team_val[v] == 1:
                one_loss.append(team[v])
                
        res = []
        res.append(list(sorted(winner)))
        res.append(sorted(one_loss))
        return res
        