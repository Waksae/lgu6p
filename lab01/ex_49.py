class BankAccount:

    def __init__(self, owner, password, balance=0):
        account_list =[]
        self.owner = owner
        self.password = f'{"0"*(4-len(str(password)))}{password}'
        self.balance = balance
        account_list.append (self.owner)

        print(f'{owner}님의 계좌가 잔엑 {balance}원으로 개설되었습니다.')

    def pwcheck(self):                                                 # 비밀번호 확인 함수
        PPS = (input('계좌 비밀번호를 입력하세요: '))
        if PPS == self.password:
            return True
        else:
            return False
        
    def deposit(self,amount):                                          # 입금 함수
        if amount > 0:
            self.balance += amount
            print(f'{amount}원이 입급되었습니다.')
        else :
            print('잘못된 입력입니다.')
        
    def withdraw(self,amount):                                         # 출금 함수
        while True:                                         
            if 0 < amount <= self.balance:
                self.balance -= amount
                break
            elif amount > self.balance:
                print(f'잔액이 부족합니다. 다시 입력해주세요.')
            else:
                print('잘못된 입력입니다. 다시 입력해주세요.')
        print(f'{amount}원이 출금되었습니다.')

    def get_balance(self):
        while True:
            if BankAccount.pwcheck(self):
                print(f'{self.owner}님의 계좌 내 잔액은 {self.balance}원입니다.')
                break
            else:
                print('다시 입력해주세요.')

    def remittance(self,amount):
        if BankAccount.pwcheck(self):  
            account_name = input('입금계좌정보를 입력하세요.')
            print(f'{amount}원이 {account_name}님의 계좌로 ')


account = BankAccount('홍길동',0000, 10000)
# account.deposit(5000)
# account.get_balance()
# account.withdraw(30000)
account.get_balance()