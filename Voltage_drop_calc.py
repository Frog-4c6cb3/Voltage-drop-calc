# Ver1.3.0
# Tkinterのインポート
from tkinter import ttk
import tkinter
from tkinter.constants import RIGHT

# 電線抵抗
SQR = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185]
R20km = [12.2, 7.56, 4.7, 3.11, 1.84, 1.16, 0.734,
         0.529, 0.391, 0.27, 0.195, 0.154, 0.126, 0.1]
R20m = dict(zip(SQR, R20km))

# 三相交流の電圧降下計算


def v_drop_3p(Amp, sqr, length, num):
    vd = R20m[sqr]*1.3*2*length*(Amp/num)*(1.732/2)/1000
    return vd

# 単相・直流の電圧降下計算


def v_drop_dc(Amp, sqr, length, num):
    vd = R20m[sqr]*1.3*2*length*(Amp/num)/1000
    return vd

# 三相or単相・直流の判断


def v_drop(r, A, S, L, N):
    if r == 0:
        Vd = v_drop_3p(A, S, L, N)
    else:
        Vd = v_drop_dc(A, S, L, N)
    return Vd

# 電圧降下率計算


def v_drop_rate(vd, voltage):
    vd_rate = vd/voltage*100
    return vd_rate


def auto_sqr(r, V, A, L, N):
    rate = float(rate_entry.get())
    for i, sqr in enumerate(SQR):
        vd = v_drop(r, A, sqr, L, N)
        Vdr = v_drop_rate(vd, V)
        if Vdr <= rate:
            return sqr
            break
    return "Error"


def calculate():
    r = int(var.get())
    V = float(V_entry.get())
    A = float(A_entry.get())
    L = int(L_entry.get())
    N = int(N_entry.get())
    a_sqr = auto_sqr(r, V, A, L, N)
    auto_sqr_entry.delete(0, tkinter.END)
    auto_sqr_entry.insert(0, a_sqr)

    S = float(S_entry.get())
    Vd = v_drop(r, A, S, L, N)
    ans_v_entry.delete(0, tkinter.END)
    ans_v_entry.insert(0, round(Vd, 2))
    Vdr = v_drop_rate(Vd, V)
    ans_rate_entry.delete(0, tkinter.END)
    ans_rate_entry.insert(0, round(Vdr, 2))


# rootメインウィンドウの設定
root = tkinter.Tk()
root.title("電圧降下計算 (V1.3.0)")

# Frameを設定
frame0 = ttk.Frame(root)
frame10 = ttk.Frame(root)
frame11 = ttk.Frame(root)
frame20 = ttk.Frame(root)
frame21 = ttk.Frame(root)
frame30 = ttk.Frame(root)
frame31 = ttk.Frame(root)
frame40 = ttk.Frame(root)
frame41 = ttk.Frame(root)
frame50 = ttk.Frame(root)
frame51 = ttk.Frame(root)
frame60 = ttk.Frame(root)
frame61 = ttk.Frame(root)
frame7 = ttk.Frame(root)
frame8 = ttk.Frame(root)
frame9 = ttk.Frame(root)


# Frameの配置
frame0.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
frame10.grid(row=1, column=0, padx=10, pady=5)
frame11.grid(row=1, column=1, padx=10, pady=5)
frame20.grid(row=2, column=0, padx=5, pady=5)
frame21.grid(row=2, column=1, padx=5, pady=5)
frame30.grid(row=3, column=0, padx=5, pady=5)
frame31.grid(row=3, column=1, padx=5, pady=5)
frame40.grid(row=4, column=0, padx=5, pady=5)
frame41.grid(row=4, column=1, padx=5, pady=5)
frame50.grid(row=5, column=0, padx=5, pady=5)
frame51.grid(row=5, column=1, padx=5, pady=5)
frame60.grid(row=6, column=0, padx=5, pady=5)
frame61.grid(row=6, column=1, padx=5, pady=5)
frame7.grid(row=7, column=0, padx=5, pady=10, columnspan=2)
frame8.grid(row=8, column=0, padx=5, pady=10, columnspan=2)
frame9.grid(row=9, column=0, padx=5, pady=10, columnspan=2)

# Label frame
label_frame1 = ttk.Labelframe(
    frame8,
    text="計算結果",
    padding=(10),
    style="My.TLabelframe"
)

label_frame2 = ttk.Labelframe(
    frame9,
    text="電線自動選定",
    padding=(10),
    style="My.TLabelframe"
)

# 各種ウィジェットの作成
# ラジオボタン
var = tkinter.IntVar()
rad1 = tkinter.Radiobutton(frame0, value=0, variable=var, text='3φ AC')
rad2 = tkinter.Radiobutton(frame0, value=1, variable=var, text='1φ AC')
rad3 = tkinter.Radiobutton(frame0, value=2, variable=var, text='DC')
rad1.pack(side=tkinter.LEFT)
rad2.pack(side=tkinter.LEFT)
rad3.pack(side=tkinter.LEFT)

# ラベル
label1 = ttk.Label(frame10, text="電圧(V)")
label2 = ttk.Label(frame20, text="電流(A)")
label3 = ttk.Label(frame30, text="電線SQR(mm2)")
label4 = ttk.Label(frame40, text="電線長(m)")
label5 = ttk.Label(frame50, text="電線本数(本)")
label6 = ttk.Label(frame60, text="許容電圧降下率(%)")
label7 = ttk.Label(label_frame1, text="電圧降下(V)")
label8 = ttk.Label(label_frame1, text="電圧降下率(%)")
label9 = ttk.Label(label_frame2, text="電線SQR(mm2)")


label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label_frame1.grid()
label7.grid(row=0, column=0)
label8.grid(row=1, column=0)
label_frame2.grid()
label9.grid(row=0, column=0)

# Entry

V_entry = ttk.Entry(
    frame11,
    width=20,
    justify=RIGHT,
)
V_entry.insert(0, 440)

A_entry = ttk.Entry(
    frame21,
    width=20,
    justify=RIGHT
)

S_entry = ttk.Entry(
    frame31,
    width=20,
    justify=RIGHT
)

L_entry = ttk.Entry(
    frame41,
    width=20,
    justify=RIGHT
)

N_entry = ttk.Entry(
    frame51,
    width=20,
    justify=RIGHT
)
N_entry.insert(0, 1)

rate_entry = ttk.Entry(
    frame61,
    width=20,
    justify=RIGHT
)
rate_entry.insert(0, 3)

ans_v_entry = ttk.Entry(
    label_frame1,
    width=20,
    justify=RIGHT
)

ans_rate_entry = ttk.Entry(
    label_frame1,
    width=20,
    justify=RIGHT
)
auto_sqr_entry = ttk.Entry(
    label_frame2,
    width=20,
    justify=RIGHT
)

# Entryの配置
V_entry.pack()
A_entry.pack()
S_entry.pack()
L_entry.pack()
N_entry.pack()
rate_entry.pack()
ans_v_entry.grid(row=0, column=1)
ans_rate_entry.grid(row=1, column=1)
auto_sqr_entry.grid(row=0, column=1)

# ボタンの配置
button1 = ttk.Button(frame7, text="計算開始", command=calculate)
button1.pack()


root.mainloop()
