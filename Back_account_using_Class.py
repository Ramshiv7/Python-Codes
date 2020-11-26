#For this challenge, create a bank account class that has two attributes:  owner &  balance and two methods: deposit & withdraw.


class Account:

	

	def __init__(self,owner,balance):
		self.owner = owner
		self.balance = balance

		print(f'Account Owner: {self.owner}')
		print(f'Account Balance: ${self.balance}')

	def deposit(self,deposit_amount):
		self.deposit_amount = deposit_amount
		print('Deposit Accepted !!!')
		self.balance = self.balance + self.deposit_amount
		print(f'Balance After Deposit: ${self.balance}')

	def withdraw(self,withdraw_amount):
		self.withdraw_amount = withdraw_amount

		if self.withdraw_amount > self.balance:
			print('Not Enough Fund to withdraw')
		else:
			print(f'Balance Now : ${self.balance}')
			print(f'Withdrawal Amount Requested: ${self.withdraw_amount}')
			self.balance =  self.balance - self.withdraw_amount 
			print(f'Current Balance : ${self.balance}')


corey_account = Account('Corey',100)


print(corey_account.owner)
print(corey_account.balance)

corey_account.deposit(50)
corey_account.withdraw(50)
