def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {'L':0,'R':0,'U':0,'D':0}
        
        for i in moves:
            d[i] +=1
        
        return d['L'] == d['R'] and d['U'] == d['D']