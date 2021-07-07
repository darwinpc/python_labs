class Taxes:
    def __init__(self, amount, zf):
        self.amount = amount
        self.zf = zf.lower() == 'si' if True else False
    def calculate(self):
        if self.amount.isdigit():
            items = {}
            iva = 0.16
            amount = int(self.amount)
            if self.zf == True:
                iva = 0.08
            print("%IVA aplicado: {}".format(iva))
            items['head'] = {1:'Concepto',2:'Monto'}
            items['tax'] = {1:'IVA:', 2: amount*iva }
            items['tax_transfer'] = {1:'IVA Trasladado:', 2: items['tax'][2]/3 }
            items['subtotal'] = {1: 'SubTotal:', 2: amount + items['tax'][2] + items['tax_transfer'][2] }
            items['tax_retain'] = {1:'IVA Retenido:', 2: items['tax_transfer'][2] * 2}
            items['isr'] = {1:'ISR:', 2: amount * 0.10}
            items['retain_total'] = {1:'Total Retenciones:', 2: items['tax_retain'][2] + items['isr'][2] }
            items['total'] = {1:'Total Deposito:',2: items['subtotal'][2] - items['tax_transfer'][2] - items['tax_retain'][2] }
            self.items = items
        else:
            dash = '-' * 42
            print(dash)
            print("Ingresa datos validos.")
    def result(self):
        if self.amount.isdigit():
            dash = '-' * 42
            for item, value in self.items.items():
                if item == 'head':
                    print(dash)
                    print('{:<25s}{:>12s}'.format(value[1], value[2]))
                    print(dash)
                else:
                    print('{:<25s}${:>12.2f}'.format(value[1], value[2]))
            
            
amount = input("Proporcionar Importe a calcular:  ")
cp = input("Vives en Franja Fronteriza (si/no):  ")
taxes = Taxes(amount, cp)
taxes.calculate()
taxes.result()
        
