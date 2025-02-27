# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        #self.elems = []
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        result = ""
        for item in chain:
            result = item + " " + result 
        print(result)

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        # if query.type == "check":
        #     # use reverse order, because we append strings to the end
        #     self.write_chain(cur for cur in reversed(self.elems)
        #                 if self._hash_func(cur) == query.ind)
        # else:
        #     try:
        #         ind = self.elems.index(query.s)
        #     except ValueError:
        #         ind = -1
        #     if query.type == 'find':
        #         self.write_search_result(ind != -1)
        #     elif query.type == 'add':
        #         if ind == -1:
        #             self.elems.append(query.s)
        #     else:
        #         if ind != -1:
        #             self.elems.pop(ind)
        # print(f"elems: {self.elems}")
        if query.type == "add":
            hash = self._hash_func(query.s)
            if hash not in self.elems:
                self.elems[hash] = []
            if query.s not in self.elems[hash]:
                self.elems[hash].append(query.s)
        elif query.type == "del":
            hash = self._hash_func(query.s)
            if hash in self.elems:
                if query.s in self.elems[hash]:
                    self.elems[hash].remove(query.s)
        elif query.type == "find":
            hash = self._hash_func(query.s)
            if hash in self.elems:
                if query.s in self.elems[hash]:
                    print("yes")
                else:
                    print("no")
            else:
                print("no")
        elif query.type == "check":
            #print("check")
            #print(f"query.ind: {query.ind}")
            #print(f"self.elems: {self.elems}")
            hash = query.ind
            if hash in self.elems:
                #make the list reversed:
                #print(f"self.elems[hash]: {self.elems[hash]}")
                if len(self.elems[hash])==0:
                    print("")
                if len(self.elems[hash])>0:
                    if len(self.elems[hash])==1:
                        print(self.elems[hash][0])
                    else:
                        #print(f"self.elems[hash].reverse() {self.elems[hash]}")
                        self.write_chain(self.elems[hash]) 
            else:
                print("")
                

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())
        

# Correct output:
# HellO world
# no
# yes
# HellO
# GooD luck

    # def PolyHash(self, S,p,x):
    #     hash = 0
    #     for i in range(len(S)-1,-1,-1):
    #         hash = (hash*x + ord(S[i]))%p
    #     return hash % self.bucket_count

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
