'''
Write a custom class that will be used to model a single bank account.

Your class should implement functionality to:

allow initialization with values for first_name, last_name, account_number,
balance, is_overdraft_allowed keep track of a "ledger" that keeps a record all
transactions (just use a list to keep track of this) at a minimum it should
keep track of the transaction date (the current UTC datetime) and the amount
(positive, or negative to indicate deposits/withdrawals) - later you could add
tracking the running balance as well.
provide read-only properties for first_name, last_name, account_number and
balance provide a property to access the ledger in such a way that a user of
this class cannot mutate the ledger directly provide a read-write property for
is_overdraft_allowed that indicates whether overdrafts are allowed on the
account.
provide methods to debit (def withdraw) and credit (def deposit) transactions
that:
verify withdrawals against available balance and is_overdraft_allowed flag
if withdrawal is larger than available balance and overdrafts are not allowed,
this should raise a custom OverdraftNotAllowed exception.
if transaction value is not positive, this should raise a ValueError exception
(we have separate methods for deposits and withdrawals, and we expect the value
to be positive in both cases - one will add to the balance, one will subtract
from the balance).
add an entry to the ledger with a current UTC timestamp (positive or negative
to indicate credit/debit) keeps the available balance updated
implements a good string representation for the instance (maybe something like
first_name last_name (account_number): balance
Feel free to expand on the minimum definition I have given here and enhance
your custom class.
'''