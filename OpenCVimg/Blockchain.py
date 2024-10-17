class Blockchain:
    def __init__(self):
        self.chain = []

    def creat_block(self,nonce,previous_hash):