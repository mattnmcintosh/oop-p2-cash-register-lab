#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self._discount = discount
    self._total = 0.00
    self._items = []
    self._previous_transactions = []

  @property
  def discount(self):
    return self._discount

  @property
  def total(self):
    return self._total

  @property
  def items(self):
    return self._items

  @property
  def previous_transactions(self):
    return self._previous_transactions

  @discount.setter
  def discount(self, value):
    if value < 0 or value > 100:
      print("Not valid discount")
    else:
      self._discount = value

  @total.setter
  def total(self, value):
    self._total = value

  @items.setter
  def items(self, value):
    self._items = value

  @previous_transactions.setter
  def previous_transactions(self, value):
    self._previous_transactions = value


  def add_item(self, item, price, quantity=1):
    self.total = self.total + ( price * quantity )
    for _ in range(quantity):
      self.items.append(item)
    currentTransaction = { "item": item, "price": price, "quantity": quantity }
    self.previous_transactions.append(currentTransaction)

  def apply_discount(self):
    discount_factor = float((100-self.discount)/100)
    if (len(self.previous_transactions) == 0 or self.discount == 0): 
      print("There is no discount to apply.")
    else:
      for transaction in self.previous_transactions:
        transaction["price"] = transaction["price"]*discount_factor
      self.total = self.total * discount_factor
      display_total = int(self.total) if self.total.is_integer() else self.total
      print(f"After the discount, the total comes to ${display_total}.")

  def void_last_transaction(self):
    if (len(self.previous_transactions) != 0):
      removed_transaction = self.previous_transactions.pop()
      for _ in range(removed_transaction["quantity"]):
        self.items.pop()
      self.total = self.total - ( removed_transaction["price"] * removed_transaction["quantity"] )
    else:
      print("There is no transaction to void")