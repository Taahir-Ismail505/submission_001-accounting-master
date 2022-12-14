import user.authentication
import transactions.journal
import banking
# import banking.fvb.reconciliation
# import banking.ubsa.reconciliation
# import banking.online.reconciliation

import sys

for i in range(1,len(sys.argv)):
    print(sys.argv[i])

user.authentication.authenticate_user()
transactions.journal.receive_income(100)
transactions.journal.pay_expense(100)
# banking.reconciliation.do_reconciliation()
# banking.fvb.reconciliation.do_reconciliation()
# banking.ubsa.reconciliation.do_reconciliation()
# banking.online.reconciliation.do_reconciliation()
banking.fvb.reconciliation.do_reconciliation()


    
