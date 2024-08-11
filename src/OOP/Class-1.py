class PC:
    def __init__(self, owner, cpu, ram, storage, storage_type, os):
        self.owner = owner
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.storage_type = storage_type
        self.os = os

    def configuration(self):
        # print(self)
        # or
        print(f"{self.owner}'s PC Configuration:-")
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage} {self.storage_type}")
        print(f"OS: {self.os}")
        print()


x = PC("Shubham", "i5", 16, "1TB", "HDD", "Windows 11").configuration()
x = PC("Farhan", "i5", 6, "512GB", "SSD", "Windows 11").configuration()
x = PC("Xact", "i5", 32, "2TB", "SSD", "Linux").configuration()
