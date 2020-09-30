class Plotnost():
    def __init__(self, p = 0.008, quantity = 1):
        self.p = p
        self.quantity = quantity

    def payment(self):                  #Расчет плотности
        x = self.p * (self.quantity * 2)
        return x


class Raschet():
    def __init__(self, l,w,quan):
        self.l = l
        self.w = w
        self.quan = quan


    def sizeMaterial(self):             #Расчет длинны материала
        tempQ = self.quan
        rasL = (self.l / tempQ)
        rasW = (self.w / tempQ)
        # print(rasL,rasW)
        return [rasL,rasW]
    def quantityPaper(self):
        print('')
        quanPapers = 1
        i = 1
        while i <= self.quan:
            quanPapers = quanPapers * 2
            i = i + 1
        return quanPapers


# plot = float(input("Введите плотность предмета в г/см2: "))
quan = int(input("Введите количество раз складывания: "))
#
# long = float(input("Введите длинну листка в см: ")) # длинна
# width = float(input("Введите ширину листка в см: ")) # ширина

widthPaper =  1/32
plot = 0.008
# quan = 2
long = 21
width = 29.7


plotnostResult = Plotnost(plot, quan)  #Обьявляем плотность и количество складывания
longResult = Raschet(long,width,quan).sizeMaterial()
retPlot = plotnostResult.payment()
quantityPapers = Raschet(long,width,quan).quantityPaper()


print(" ")
print(" ")
print("**********************************************************************************************************")
print("* ")
print("* ")
print("* Превоначальные данные")
print("* ")
print("* Начальная Длинна: {0} см,     Ширина: {1} см,     Плотность: {2} г/см2 (бумага),    Количество Згибов: {3} раз".format(long, width,plot,quan))
print("* ")
print("* ")
print("* ")
print("* Расчеты:")
print("* ")

print("* Длинна равна: {0} см".format(longResult[0]), "   Ширина равна: {0} см".format(longResult[1]))
print("* ")
print('* Плотность равна: {0} г/см2 или {1} г/м2'.format(retPlot, retPlot*10000))# Плотность
print("* ")
print("* Количество слоев: {0} шт , Общая высота {1} см".format(quantityPapers, quantityPapers * widthPaper))
print("* ")
print("* ")
print("************************************************************************************************************ ")
