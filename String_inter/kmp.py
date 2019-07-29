class KMP:
    def partial(self, pattern): # def partial(self, pattern):  - partial이라는 자기 함수에 패턴을넣겠다
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]  # -1하는 이유 : 인덱스는 0부터 시작!
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in T
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = partial[j - 1]
            
        return ret




def test():
    p1 = "aa"
    t1 = "aaaaaaaa"

    kmp = KMP()
    assert(kmp.search(t1, p1) == [0, 1, 2, 3, 4, 5, 6])