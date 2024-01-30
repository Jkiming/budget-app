class Category:
    def __init__(self, ledger):
        self.ledger = ledger

    def __str__(self):
        nombre_categoria = [nombre for nombre, valor in locals().items() if valor is self.ledger][0]
        largo_nombre_categoria = len(nombre_categoria)
        espaciado = int((30 - largo_nombre_categoria) / 2)
        simbolo = "*"
        texto_final = (simbolo * espaciado) + nombre_categoria + (espaciado * simbolo)
        if len(texto_final) % 2 != 0:
            texto_final = (simbolo * espaciado) + nombre_categoria + (espaciado * simbolo) + simbolo * 1
        for item in self.ledger:
            largo_desc = len(item["description"])
            espaciado_desc = 1 if (23 - largo_desc) is 0 else (23 - largo_desc)
            texto_final += f"{item["description"][:23] + espaciado_desc * " " + "{:.2f}".format(item["amount"])}\n"
        texto_final += f"Total:{"{:.2f}".format(self.get_balance())}"
        return texto_final
    
    #este metodo crea un diccionario con un monto y una descripcion
    #el cual es agregado a la lista (ledger)
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