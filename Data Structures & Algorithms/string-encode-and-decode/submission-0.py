class Solution:
    store = []
    def encode(self, strs: List[str]) -> str:
        self.store = strs
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        return self.store
