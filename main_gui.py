from subnetcalc import *
import tkinter as tk


win = tk.Tk()
win.title("Subnet calculator")
win.geometry("600x400")

ip = tk.StringVar(win)
sbnt = tk.IntVar(win)
ntad = tk.StringVar(win)
bdad = tk.StringVar(win)
avip = tk.StringVar(win)
rng = tk.StringVar(win)


def clear():
	ip.set('')
	sbnt.set(0)
	ntad.set('')
	bdad.set('')
	avip.set('')
	rng.set('')
	

def calc():
	ipl = [int(x) for x in ip.get().split(".")]
	mask = sbnt.get()
	ntadr = net_adress(ipl, mask)
	ntad.set(".".join([str(x) for x in ntadr]))
	bdcst = broadcast(ntadr,mask)
	bdad.set(".".join([str(x) for x in bdcst]))
	rng.set(subrange(ntadr,bdcst))
	subnets,hosts = available(mask,ipl)
	avip.set(f"hosts : {hosts} subnets: {subnets}")

tk.Label(win,text = "IP Address").grid(row=0,column=0)
ipfld = tk.Entry(win,textvariable=ip)
ipfld.grid(row=0,column=1)

tk.Label(win, text="Subnet").grid(row=1, column=0)
sbntfld = tk.Entry(win, textvariable=sbnt)
sbntfld.grid(row=1, column=1)

tk.Label(win, text="Subnet").grid(row=1, column=0)
sbntfld = tk.Entry(win, textvariable=sbnt)
sbntfld.grid(row=1, column=1)

tk.Button(win,text="Calculate",command = calc).grid(row=2,column=0)
tk.Button(win,text="Clear",command = clear).grid(row=2,column=1)

tk.Label(win,text = "Network Address").grid(row=3,column=0)
ntfld = tk.Entry(win,textvariable=ntad)
ntfld.grid(row=3,column=1)

tk.Label(win, text="Broadcast Address").grid(row=4, column=0)
bdfld = tk.Entry(win, textvariable=bdad)
bdfld.grid(row=4, column=1)

tk.Label(win,text = "No Of available IP").grid(row=5,column=0)
avipfld = tk.Entry(win,textvariable=avip)
avipfld.grid(row=5,column=1)

tk.Label(win,text = "Range").grid(row=6,column=0)
rngfld = tk.Entry(win,textvariable=rng)
rngfld.grid(row=6,column=1)

win.mainloop()