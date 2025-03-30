prev_temp = None
decrease = 0

print("Введите значения температуры:")

while True:
    cur_temp = float(input())
    
    if cur_temp == 0:
        break
    

    if 37.4 <= cur_temp <= 37.8:
        if prev_temp is not None:
            if cur_temp < prev_temp:
                decrease += 1
        
        prev_temp = cur_temp
    else:
        print("Температура вне допустимого диапазона. Пожалуйста, введите значение от 37.4 до 37.8.")

print(f"Температура уменьшалась {decrease} раз(а).")
