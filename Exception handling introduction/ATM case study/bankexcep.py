#bankexcep.py--file name and treated as module name

class DepositError(Exception):pass

class WithdrawError(BaseException):pass

class InSuffFundError(Exception):pass