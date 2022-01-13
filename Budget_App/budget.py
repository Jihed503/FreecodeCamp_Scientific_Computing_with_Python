class Category:
  def __init__(self, name):
    self.ledger = []
    self.name = name

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})
  
  def withdraw(self, amount, description=''):
    if amount > sum([i['amount'] for i in self.ledger]):
      return False
    else:
      self.ledger.append({'amount': -amount, 'description': description})
      return True
  
  def get_balance(self):
    return sum([i['amount'] for i in self.ledger])

  def transfer(self, amount, cat):
    if self.withdraw(amount, 'Transfer to {}'.format(cat.name)) :
      cat.deposit(amount, 'Transfer from {}'.format(self.name))
      return True
    return False

  def check_funds(self, amount):
    return amount <= sum([i['amount'] for i in self.ledger])
  
  def __str__(self):
    ch = self.name.center(30, '*') + '\n'
    for i in self.ledger :
      ch += i['description'][:23].ljust(23) + '{:.2f}'.format(i['amount']).rjust(7) + '\n'
    ch += 'Total: {}'.format(sum([i['amount'] for i in self.ledger]))
    return ch

def create_spend_chart(categories):
  total_sum = 0
  for cat in categories:
    total_sum += sum([abs(i['amount']) for i in cat.ledger if i['amount']<0])
  percentage_list = []
  for cat in categories :
    withdrawals = sum([abs(i['amount']) for i in cat.ledger if i['amount']<0])
    percentage_not_rounded = (withdrawals/total_sum)*100
    percentage = percentage_not_rounded-(percentage_not_rounded%10)
    percentage_list.append((percentage,cat))

  # percentage_list.sort(reverse=True, key=lambda x:x[0])
  
  ch = 'Percentage spent by category\n'

  for i in range(100,-1,-10):
    ch += str(i).rjust(3) + '| '
    for j in percentage_list :
      if j[0]>=i :
        ch += 'o  '
      else: ch += '   '
    ch += '\n'

  ch += '    ' + '-'*(3*len(percentage_list)+1) + '\n'

  max_len = max([len(i[1].name) for i in percentage_list])
  for i in range(1,max_len+1):
    ch += 5*' '
    for j in percentage_list:
      if i <= len(j[1].name) :
        ch += (j[1].name)[i-1] + '  '
      else: ch += '   '
    ch += '\n'
  
  return ch[:-1]
