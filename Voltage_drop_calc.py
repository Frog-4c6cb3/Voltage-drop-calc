# Ver1.0.0
# Tkinterのインポート
from tkinter import ttk
import tkinter
from tkinter.constants import RIGHT

# 電線抵抗
SQR = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 180]
R20km = [12.2, 7.56, 4.7, 3.11, 1.84, 1.16, 0.734,
         0.529, 0.391, 0.27, 0.195, 0.154, 0.126, 0.1]
R20m = dict(zip(SQR, R20km))


def v_drop(Amp, sqr, length, num):
    vd = R20m[sqr]*1.3*2*length*(Amp/num)*(1.732/2)/1000
    return vd


def v_drop_rate(vd, voltage):
    vd_rate = vd/voltage*100
    return vd_rate


def calculate():
    V = float(V_entry.get())
    A = float(A_entry.get())
    S = float(S_entry.get())
    L = int(L_entry.get())
    N = int(N_entry.get())
    Vd = v_drop(A, S, L, N)
    ans_v_entry.delete(0, tkinter.END)
    ans_v_entry.insert(0, round(Vd, 2))
    Vdr = v_drop_rate(Vd, V)
    ans_rate_entry.delete(0, tkinter.END)
    ans_rate_entry.insert(0, round(Vdr, 2))


# rootメインウィンドウの設定
root = tkinter.Tk()
root.title("電圧降下計算 (V1.0.0)")

# Frameを設定
frame1 = ttk.Frame(root)
frame2 = ttk.Frame(root)
frame3 = ttk.Frame(root)
frame4 = ttk.Frame(root)
frame5 = ttk.Frame(root)
frame6 = ttk.Frame(root)

# Frameの配置
frame1.grid(row=0, column=0, padx=5, pady=10)
frame2.grid(row=0, column=1, padx=5, pady=10)
frame3.grid(row=0, column=2, padx=5, pady=10)
frame4.grid(row=0, column=3, padx=5, pady=10)
frame5.grid(row=1, column=0, padx=5, pady=10, columnspan=4)
frame6.grid(row=2, column=0, padx=5, pady=10, columnspan=4)

# 各種ウィジェットの作成
# ラベル
lavel_1_1 = ttk.Label(frame1, text="電圧")
lavel_1_2 = ttk.Label(frame3, text="V")
label_2_1 = ttk.Label(frame1, text="電流")
label_2_2 = ttk.Label(frame3, text="A")
label_3_1 = ttk.Label(frame1, text="電線SQR")
label_3_2 = ttk.Label(frame3, text="㎟")
label_4_1 = ttk.Label(frame1, text="電線長")
label_4_2 = ttk.Label(frame3, text="m")
label_5_1 = ttk.Label(frame1, text="電線本数")
label_5_2 = ttk.Label(frame3, text="本")
label_6 = ttk.Label(frame5, text="----------計算結果----------")
label_6_1 = ttk.Label(frame5, text="電圧降下(V)")
label_7_1 = ttk.Label(frame6, text="電圧降下率(%)")


# ラベル配置
lavel_1_1.pack()
lavel_1_2.pack()
label_2_1.pack()
label_2_2.pack()
label_3_1.pack()
label_3_2.pack()
label_4_1.pack()
label_4_2.pack()
label_5_1.pack()
label_5_2.pack()
label_6.pack()
label_6_1.pack()
label_7_1.pack()

# Entry
V_entry = ttk.Entry(
    frame2,
    width=20,
    justify=RIGHT
)

A_entry = ttk.Entry(
    frame2,
    width=20,
    justify=RIGHT
)

S_entry = ttk.Entry(
    frame2,
    width=20,
    justify=RIGHT
)

L_entry = ttk.Entry(
    frame2,
    width=20,
    justify=RIGHT
)

N_entry = ttk.Entry(
    frame2,
    width=20,
    justify=RIGHT
)

ans_v_entry = ttk.Entry(
    frame5,
    width=20,
    justify=RIGHT
)

ans_rate_entry = ttk.Entry(
    frame6,
    width=20,
    justify=RIGHT
)

# Entryの配置
V_entry.pack()
A_entry.pack()
S_entry.pack()
L_entry.pack()
N_entry.pack()
ans_v_entry.pack()
ans_rate_entry.pack()

# ボタンの配置
button1 = ttk.Button(frame4, text="計算開始", command=calculate)
button1.pack()


root.mainloop()
