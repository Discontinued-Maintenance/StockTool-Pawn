import tkinter as tk
import math as math
window = tk.Tk()
window.title('StockTool-Pawn')
window.geometry('500x300')

def _volume(event):
    try:
        buy = float(buy_entry.get())
    except:
        buy = 0
    try:
        single = float(single_entry.get())
    except:
        single = 0
    volume = single/0.015
    formula = (buy*1000) + (buy*0.001425)
    try:
        sheets_number_formula = math.floor(volume/formula)
    except:
        sheets_number_formula = 0
    result = '成交量：{}'.format(volume)
    result2 = '張數：{}'.format(sheets_number_formula)
    return _volume_text.set(result),_sheets_number_text.set(result2)

def _buy_estimated_cost_text(event):
    try:
        buy = float(buy_entry.get())
    except:
        buy = 0
    try:
        single = float(single_entry.get())
    except:
        single = 0
    volume = single/0.015
    formula = ((buy*1000) + (buy*1000*0.001425))/1000
    try:
        sheets_number_formula = math.floor(volume/formula/1000)
    except:
        sheets_number_formula = 0
    result = '預估成本：{}'.format(formula)
    result2 = '張數：{}'.format(sheets_number_formula)
    return _buy_estimated_cost_text.set(result),_sheets_number_text.set(result2)

def _sell_text(event):
    try:
        stoploss = float(stop_loss_entry.get())
    except:
        stoploss = 0
    try:
        buy = float(buy_entry.get())
    except:
        buy = 0
    sell = buy-(buy*(stoploss/100))
    formula = ((sell *1000)+(sell*1000*0.001425)+(sell*1000*0.003))/1000
    result = '賣：{} '.format(str(sell))
    result1 = '預估成本：{} '.format(str(formula))
    return _sell_text.set(result),_sell_estimated_cost_text.set(result1)

        
first_row_frame = tk.Frame(window)
first_row_frame.pack(side=tk.TOP)

single_label = tk.Label(first_row_frame, text='單筆：')
single_label.pack(side=tk.LEFT)
single_entry = tk.Entry(first_row_frame)
single_entry.bind('<KeyRelease>', _volume)
single_entry.pack(side=tk.LEFT)

_volume_text = tk.StringVar()
volume_label = tk.Label(window, textvariable=_volume_text,font=('Arial', 20))
volume_label.pack()

second_row = tk.Frame(window)
second_row.pack(side=tk.TOP)

buy_label = tk.Label(second_row, text='買：')
buy_label.pack(side=tk.LEFT)
buy_entry = tk.Entry(second_row)
buy_entry.bind('<KeyRelease>', _buy_estimated_cost_text)
buy_entry.pack(side=tk.LEFT)

_buy_estimated_cost_text = tk.StringVar()
estimated_cost_label = tk.Label(window, textvariable=_buy_estimated_cost_text,font=('Arial', 20))
estimated_cost_label.pack()

third_row = tk.Frame(window)
third_row.pack(side=tk.TOP)

stop_loss_label = tk.Label(third_row, text='停損：')
stop_loss_label.pack(side=tk.LEFT)
stop_loss_entry = tk.Entry(third_row)
stop_loss_entry.bind('<KeyRelease>' ,_sell_text)
stop_loss_entry.pack(side=tk.LEFT)
stop_loss_label = tk.Label(third_row, text='%')
stop_loss_label.pack(side=tk.RIGHT)

_sell_text = tk.StringVar()
sell_label = tk.Label(window, textvariable=_sell_text,font=('Arial', 20))
sell_label.pack()

_sell_estimated_cost_text = tk.StringVar()
_sell_estimated_cost_label = tk.Label(window, textvariable=_sell_estimated_cost_text,font=('Arial', 20))
_sell_estimated_cost_label.pack()

_sheets_number_text = tk.StringVar()
_sheets_number_label = tk.Label(window, textvariable=_sheets_number_text,font=('Arial', 20))
_sheets_number_label.pack()

window.mainloop()