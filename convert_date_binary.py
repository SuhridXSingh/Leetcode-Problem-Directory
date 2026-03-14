class Solution:
    def convertDateToBinary(self, date: str) -> str:
        dl = date.split("-")
        y = f"{int(dl[0]):b}"
        m = f"{int(dl[1]):b}"
        d = f"{int(dl[2]):b}"
        return f"{y}-{m}-{d}"
