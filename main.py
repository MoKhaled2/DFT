import math

# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __str__(self):
#         if self.real==0:
#             return f"{self.imag}i"
#         elif self.imag > 0:
#             return f"{self.real} + {self.imag}i"
#         elif self.imag==0:
#             return f"{self.real}"
#         else:
#             return f"{self.real} - {-self.imag}i"

def Complex(real,imag):
    if real == 0:
        return f"{imag}i"
    elif imag > 0:
        return f"{real} + {imag}i"
    elif imag == 0:
        return f"{real}"
    else:
        return f"{real} - {-imag}i"

def phase(sum_reals,sum_imags):
    if sum_reals == 0:
        if sum_imags > 0:
            return 90
        elif sum_imags < 0:
            return -90
        else:
            return 0
    elif sum_reals < 0:
        if sum_imags > 0:
            return 180 + round(math.degrees(math.atan(sum_imags / sum_reals)), 3)
        else:
            return -180 + round(math.degrees(math.atan(sum_imags / sum_reals)), 3)
    else:
        return round(math.degrees(math.atan(sum_imags / sum_reals)), 3)

def calculate(input_signal,N):
    while len(input_signal)<N:
        input_signal.append(0)
    dft_result = []
    phase_result=[]
    magnitude_result=[]

    for k in range(N):
        sum_reals = 0
        sum_imags = 0

        for n in range(N):
            angle = 2 * math.pi * k * n / N
            sum_reals +=  round(input_signal[n]*(math.cos(angle)),3)
            sum_imags +=  round(input_signal[n]*(-1*math.sin(angle)),3)

        phase_result.append(phase(sum_reals,sum_imags))
        magnitude_result.append(round(math.sqrt(sum_imags**2+sum_reals**2),3))
        dft_result.append(Complex(sum_reals,sum_imags))

    return dft_result ,magnitude_result,phase_result



input_signal = [.5,1]

N=int(input("How many points do you want ? "))
dft_result ,magnitude_result,phase_result = calculate(input_signal,N)


print("DFT Result:")
print(dft_result)
# for i in dft_result :
#         print(i)

print("------------------------------------------------------------------------------------")

print("Magnitude_result:")
print(magnitude_result)

print("-------------------------------------------------------------------------------------")
print("Phase_result:")
print(phase_result)