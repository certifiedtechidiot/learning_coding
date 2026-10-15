readings = [21.5, 22.0, 21.8, 99.9, 22.1, -5.0, 22.4, 21.9]
normal_readings=[]
glitch_readings=[]
for i in readings:
    if i>=0 and i<=50:
        normal_readings.append(i)
    else:
        glitch_readings.append(i)

def lentcounter(x):
    count=0
    for i in x:
        count+=1
    return count

def sumcalculator(x):
    sum=0
    for i in x:
        sum+=i
    return sum

valid_reading_avg=sumcalculator(normal_readings)/lentcounter(normal_readings)
invalid_readings_avg=sumcalculator(glitch_readings)/lentcounter(glitch_readings)

print(f"valid avg = {valid_reading_avg}\ninvalid avg = {invalid_readings_avg}")

