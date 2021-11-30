import time


class Block:
    """
    A unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency
    """
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            "Block("
            f"Timestamp: {self.timestamp}, "
            f"LastHash: {self.last_hash}, "
            f"Hash: {self.hash}, "
            f"Data: {self.data}), "
        )
    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = f"{timestamp}-{last_hash}"

        return Block(timestamp, last_hash, hash, data)
    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """
        return Block(1, "genesis_last_hash", "genesis hash", [])


def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'data')
    print(block)



if __name__ == '__main__':
    main()
