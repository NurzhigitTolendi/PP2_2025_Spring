class Account:
    def __init__(self, owner, balance=0.0):
        """Инициализация владельца счета и баланса"""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Пополнение счета"""
        if amount > 0:
            self.balance += amount
            print(f"Пополнение: +{amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        """Снятие средств, если хватает денег на счету"""
        if amount > self.balance:
            print(f"Ошибка! Недостаточно средств. Ваш баланс: {self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Снятие: -{amount}. Остаток на счете: {self.balance}")
        else:
            print("Сумма снятия должна быть положительной.")

account = Account("Иван", 1000)  

account.deposit(500)   
account.withdraw(300) 
account.withdraw(1500) 
account.withdraw(100) 
