class Category:
    #este metodo inicializa una lista llamada ledger
    def __init__(self, ledger):
        self.ledger = ledger

    def __str__(self):

        pass

    
    #este metodo crea un diccionario con un monto y una descripcion
    #el cual es agregador a la lista (ledger)
    def deposit(self, amount, description=""):
        append_deposit_to_ledger = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(append_deposit_to_ledger)

    #este metodo es similar a deposit, pero almacena valores negativos
    #pues se busca retirar/restar
    def withdraw(self,amount, description):
        
        if amount < 0:
            append_withdraw_to_ledger = {
            "amount": -amount,
            "description": description
            }
            self.ledger.append(append_withdraw_to_ledger)
            return True
        return False
    
    #obtenemos la suma total para cada keyword "amount" lo que indica
    #el balance total que hay almacenado en la lista mayor (ledger)
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    #transfiere y recibe una transferencia de otra categoria
    def transfer(self, amount, another_budget):
        append_withdraw_to_budget_category = {
            "amount": amount,
            "description": "Transfer to [Destination Budget Category]"
        }
        append_deposit_to_budget_category = {
            "amount": amount,
            "description": "Transfer from [Source Budget Category]"
        }
        if self.check_funds(amount):
            another_budget.append(append_withdraw_to_budget_category)
            another_budget.append(append_deposit_to_budget_category)
            return True 
        return False

        
    #metodo que checkea si el monto es positivo devolviendo True, caso contrario False
    def check_funds(self, amount):
        return False if amount > self.get_balance() else True




def create_spend_chart(categories):
    pass