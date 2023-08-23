import calendar

print()
yy = int(input("Entre com o ano: (exemplo: 2012)-->> ")) # year
mm = int(input("Entre com o mês: (1-12)-->> ")) # month
print()

# display the calendar
print(calendar.month(yy, mm))



