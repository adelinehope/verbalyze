import hashlib
import time
import json

class Block:
    def _init_(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def _init_(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

class VotingSystem:
    def _init_(self):
        self.candidates = {}
        self.voters = set()

    def add_candidate(self, candidate_name):
        self.candidates[candidate_name] = 0

    def vote(self, voter_id, candidate_name):
        if voter_id in self.voters:
            return "You have already voted."

        if candidate_name not in self.candidates:
            return "Invalid candidate."

        timestamp = int(time.time())
        vote_data = f"Voter: {voter_id}, Candidate: {candidate_name}, Timestamp: {timestamp}"
        new_block = Block(len(my_blockchain.chain), my_blockchain.get_latest_block().hash, timestamp, vote_data)
        my_blockchain.add_block(new_block)

        self.candidates[candidate_name] += 1
        self.voters.add(voter_id)
        return "Vote recorded successfully."

    def get_results(self):
        return self.candidates

# Create a blockchain
my_blockchain = Blockchain()

# Create a voting system
voting_system = VotingSystem()

def display_menu():
    print("\nWelcome to the Innovative Voting System!")
    print("1. Register Candidate")
    print("2. Cast Vote")
    print("3. View Results")
    print("4. View Blockchain")
    print("5. Exit")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        candidate_name = input("Enter the candidate's name: ")
        voting_system.add_candidate(candidate_name)
        print(f"Candidate '{candidate_name}' registered.")

    elif choice == "2":
        voter_id = int(input("Enter your voter ID: "))
        candidate_name = input("Enter the candidate's name you want to vote for: ")
        result = voting_system.vote(voter_id, candidate_name)
        print(result)

    elif choice == "3":
        print("\nElection Results:")
        results = voting_system.get_results()
        for candidate, votes in results.items():
            print(f"{candidate}: {votes} votes")

    elif choice == "4":
        print("\nBlockchain:")
        for block in my_blockchain.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}\n")

    elif choice == "5":
        print("Thank you for using our Voting System. Have a great day!")
        break