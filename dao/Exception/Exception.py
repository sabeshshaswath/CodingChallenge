class ApplyLoneException(Exception):
    def __init__(self,msg="Error adding Loan") -> None:
        super().__init__(msg)
class calculateInterestException(Exception):
    def __init__(self,msg="Error calculating Interest") -> None:
        super().__init__(msg)
class InvalidLoanException(Exception):
    def __init__(self,msg="Error on loanStatus") -> None:
        super().__init__(msg)
class calculateEMIException(Exception):
    def __init__(self,msg="Error on calculateEMI") -> None:
        super().__init__(msg)
class loanRepaymentException(Exception):
    def __init__(self,msg="Error loanRepayment") -> None:
        super().__init__(msg)
class RetriveloanException(Exception):
    def __init__(self,msg="Error Retriving information") -> None:
        super().__init__(msg)