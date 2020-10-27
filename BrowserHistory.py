class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.history =self.history[:self.cur+1]
        self.history.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        if self.cur-steps>=0:
            self.cur = self.cur-steps
        else:
            self.cur = 0
        return self.history[self.cur]
    def forward(self, steps: int) -> str:
        if self.cur+steps<len(self.history):
            self.cur = self.cur+steps
        else:
            self.cur = len(self.history)-1
        return self.history[self.cur]