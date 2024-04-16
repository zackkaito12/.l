import math

def fungsi_f(x):
    if x > 0:
        return 3 * x ** 2 + 7 * x - 2
    else:
        return 2 * x ** 2 - 5 * x - 4

def fungsi_g(x):
    return fungsi_f(x) ** 2 - math.sqrt(fungsi_f(x))

def fungsi_h(x):
    return fungsi_f(x) * fungsi_g(x)

while True:
    print("TABEL FUNGSI")
    print("f(x) = 3x^2 + 7x - 2 jika x > 0")
    print("     = 2x^2 - 5x - 4 jika x < 0")
    print("g(x) = (f(x))^2 - sqrt(f(x))")
    print("h(x) = f(x) * g(x)\n")

    n = int(input("Input banyak data n: "))

    x = []
    f = []
    g = []
    h = []

    for i in range(n):
        nilai_x = float(input(f"Input nilai x ke-{i+1}: "))
        x.append(nilai_x)
        f.append(fungsi_f(nilai_x))
        g.append(fungsi_g(nilai_x))
        h.append(fungsi_h(nilai_x))

    print("\nNo\tf(x)\tg(x)\th(x)")
    for i in range(n):
        print(f"{i+1}\t{f[i]}\t{g[i]}\t{h[i]}")

    input_lagi = input("\nInput nilai x lagi? (Y/N): ")
    if input_lagi.upper() != 'Y':
        break
