class CreditCardValidator :
    def __init__(self, cardNoInput):
        self.filterCardNo =  [ int(digit) for digit in cardNoInput if digit.isdigit() ]
        # self.cardno = "".join(map(str, self.filterCardNo))
    
    def validator(self):
        reversedDigit = self.filterCardNo[ : :-1]
        checkSum = sum( digit if i % 2 == 0 else (digit * 2 if digit * 2 < 10 else digit * 2 - 9)
        for i, digit in enumerate(reversedDigit))

        return checkSum % 10 == 0
    
    def IsValid(self):
        if self.validator():
            return "VALID"
        else:
            return "INVALID"
        
    @classmethod
    def Start(cls):
        cardNoInput = str(input("Enter Your Card No. : "))
        validator = cls(cardNoInput)
        print(validator.IsValid())

CreditCardValidator.Start()
