class Logger:

    def __init__(self):
        # use dic to track the latest timestamp for a unique message
        self.log = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # track new message
        if message not in self.log:
            self.log[message] = timestamp
            return True
        else:
            last_timestamp = self.log[message]
            # prevent other identical messages from being printed until timestamp t + 10
            if timestamp - last_timestamp < 10:
                return False
            # update seen message
            else:
                self.log[message] = timestamp
                return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
