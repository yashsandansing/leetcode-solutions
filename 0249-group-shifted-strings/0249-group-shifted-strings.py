class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_hash(string: str) -> str:
            key = list()
            for a, b in zip(string, string[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            # print("".join(key))
            return "".join(key)
        
        hashmap = defaultdict(list)
        for word in strings:
            key = get_hash(word)
            hashmap[key].append(word)
        
        return list(hashmap.values())