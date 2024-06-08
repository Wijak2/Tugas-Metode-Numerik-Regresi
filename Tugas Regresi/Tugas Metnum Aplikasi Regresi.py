import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import sqrt

#Fungsi untuk regresi eksponensial
def exponential_model(x, a, b):
    return a * np.exp(b * x)

#Fungsi untuk regresi linear
def linear_model(x, m, c):
    return m * x + c

#Fungsi untuk regresi pangkat sederhana
def power_model(x, a, b):
    return a * np.power(x, b)

#Fungsi untuk membaca file CSV
def read_csv_file():
    filename = filedialog.askopenfilename(title="Select CSV File", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    if filename:
        data = pd.read_csv(filename)
        return data
    else:
        return None

#Fungsi untuk melakukan regresi dan plotting
def do_regression_and_plot(data, problem_number):
    if data is not None:
        # Mengambil kolom yang dibutuhkan
        TB = data['Hours Studied'].values
        NL = data['Sample Question Papers Practiced'].values
        NT = data['Performance Index'].values
        
        if problem_number == 1:
            # Regresi Linear untuk TB terhadap NT
            params_lin_tb, _ = curve_fit(linear_model, TB, NT)
            m_tb, c_tb = params_lin_tb
            NT_pred_lin_tb = linear_model(TB, m_tb, c_tb)

            # Regresi Eksponensial untuk TB terhadap NT
            params_exp_tb, _ = curve_fit(exponential_model, TB, NT)
            NT_pred_exp_tb = exponential_model(TB, *params_exp_tb)

            # Regresi Pangkat Sederhana untuk TB terhadap NT
            params_pow_tb, _ = curve_fit(power_model, TB, NT)
            NT_pred_pow_tb = power_model(TB, *params_pow_tb)

            # Plot untuk TB terhadap NT
            plt.figure(figsize=(18, 6))

            plt.subplot(1, 3, 1)
            plt.scatter(TB, NT, color='blue', label='Data Points')
            plt.plot(TB, NT_pred_lin_tb, color='red', label='Regresi Linear')
            plt.xlabel('Durasi Waktu Belajar (TB)')
            plt.ylabel('Nilai Ujian (NT)')
            plt.legend()
            plt.title('Regresi Linear: TB vs NT')

            plt.subplot(1, 3, 2)
            plt.scatter(TB, NT, color='blue', label='Data Points')
            plt.plot(TB, NT_pred_exp_tb, color='green', label='Regresi Exponensial')
            plt.xlabel('Durasi Waktu Belajar (TB)')
            plt.ylabel('Nilai Ujian (NT)')
            plt.legend()
            plt.title('Regresi Exponensial: TB vs NT')

            plt.subplot(1, 3, 3)
            plt.scatter(TB, NT, color='blue', label='Data Points')
            plt.plot(TB, NT_pred_pow_tb, color='orange', label='Regresi Pangkat Sederhana')
            plt.xlabel('Durasi Waktu Belajar (TB)')
            plt.ylabel('Nilai Ujian (NT)')
            plt.legend()
            plt.title('Regresi Pangkat Sederhana: TB vs NT')

            plt.tight_layout()
            plt.show()

            # Menghitung galat RMS
            rms_linear_tb = np.sqrt(np.mean((NT - NT_pred_lin_tb) ** 2))
            rms_exponential_tb = np.sqrt(np.mean((NT - NT_pred_exp_tb) ** 2))
            rms_power_tb = np.sqrt(np.mean((NT - NT_pred_pow_tb) ** 2))

            print(f'RMS Error for Linear Regression (TB vs NT): {rms_linear_tb}')
            print(f'RMS Error for Exponential Regression (TB vs NT): {rms_exponential_tb}')
            print(f'RMS Error for Power Regression (TB vs NT): {rms_power_tb}')

        elif problem_number == 2:
            # Regresi Linear untuk NL terhadap NT
            params_lin_nl, _ = curve_fit(linear_model, NL, NT)
            m_nl, c_nl = params_lin_nl
            NT_pred_lin_nl = linear_model(NL, m_nl, c_nl)

            # Regresi Eksponensial untuk NL terhadap NT
            params_exp_nl, _ = curve_fit(exponential_model, NL, NT)
            NT_pred_exp_nl = exponential_model(NL, *params_exp_nl)

            # Regresi Pangkat Sederhana untuk NL terhadap NT
            params_pow_nl, _ = curve_fit(power_model, NL, NT)
            NT_pred_pow_nl = power_model(NL, *params_pow_nl)

            # Plot untuk NL terhadap NT
            plt.figure(figsize=(18, 6))

            plt.subplot(1, 3, 1)
            plt.scatter(NL, NT, color='blue', label='Data Points')
            plt.plot(NL, NT_pred_lin_nl, color='red', label='Regresi Linear')
            plt.xlabel('Jumlah Latihan Soal Dikerjakan (NL)')
            plt.ylabel('Performance Index (NT)')
            plt.legend()
            plt.title('Regresi Linear: NL vs NT')

            plt.subplot(1, 3, 2)
            plt.scatter(NL, NT, color='blue', label='Data Points')
            plt.plot(NL, NT_pred_exp_nl, color='green', label='Regresi Exponensial')
            plt.xlabel('Jumlah Latihan Soal Dikerjakan (NL)')
            plt.ylabel('Performance Index (NT)')
            plt.legend()
            plt.title('Regresi Exponensial: NL vs NT')

            plt.subplot(1, 3, 3)
            plt.scatter(NL, NT, color='blue', label='Data Points')
            plt.plot(NL, NT_pred_pow_nl, color='orange', label='Regresi Pangkat Sederhana')
            plt.xlabel('Jumlah Latihan Soal Dikerjakan (NL)')
            plt.ylabel('Performance Index (NT)')
            plt.legend()
            plt.title('Regresi Pangkat Sederhana: NL vs NT')

            plt.tight_layout()
            plt.show()

            # Menghitung galat RMS
            rms_linear_nl = np.sqrt(np.mean((NT - NT_pred_lin_nl) ** 2))
            rms_exponential_nl = np.sqrt(np.mean((NT - NT_pred_exp_nl) ** 2))
            rms_power_nl = np.sqrt(np.mean((NT - NT_pred_pow_nl) ** 2))

            print(f'RMS Error for Linear Regression (NL vs NT): {rms_linear_nl}')
            print(f'RMS Error for Exponential Regression (NL vs NT): {rms_exponential_nl}')
            print(f'RMS Error for Power Regression (NL vs NT): {rms_power_nl}')


#Fungsi yang dipanggil saat tombol "Pilih File" ditekan
def browse_button_clicked():
    data = read_csv_file()
    if data is not None:
        problem_number = problem_combobox.current() + 1
        do_regression_and_plot(data, problem_number)

#GUI
root = tk.Tk()
root.title("Regresi")
root.geometry("400x150")
label = ttk.Label(root, text="Select Problem:")
label.pack(pady=5)
problem_combobox = ttk.Combobox(root, values=["Problem 1 (TB vs NT)", "Problem 2 (NL vs NT)"])
problem_combobox.pack(pady=5)
problem_combobox.current(0)
browse_button = ttk.Button(root, text="Pilih File", command=browse_button_clicked)
browse_button.pack(pady=5)

root.mainloop()
