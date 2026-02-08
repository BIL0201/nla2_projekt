Projekt č.11 - Gram–Schmidtův a modifikovaný Gram–Schmidtův proces

Projekt porovnává klasický Gram–Schmidtův proces (dále CGS) a modifikovaný Gram–Schmidtův proces (MGS) pro QR rozklad matic. Testování je provedeno na reálných řídkých maticích ze SuiteSparse Matrix Collection, které jsou nejprve načteny ve formátu Matrix Market a následně převedeny na husté matice.

Cílem je numericky porovnat:

- přesnost rozkladu (‖A − QR‖)
- ortogonalitu vypočtené matice Q (‖QᵀQ − I‖)



Struktura projektu

Projektová složka obsahuje vstupní matice ve formátu Matrix Market, implementaci algoritmů klasického a modifikovaného Gram–Schmidtova procesu v jazyce Python, textový soubor s reportem a soubor README s popisem projektu a instrukcemi ke spuštění.

projekt_nla2/
├── abb313.mtx
├── bcspwr01.mtx
├── ash219.mtx
├── lp_stocfor.mtx
├── CGS_MGS.py
├── report.txt
└── README.md



Spuštění programu

Pro spuštění programu je nutné mít nainstalovány balíčky NumPy a SciPy.
Program se spustí zadáním následujícího příkazu v příkazové řádce:
python CGS_MGS.py

Program načte všechny matice, provede QR rozklad pomocí CGS i MGS a vypíše normy chyb do standardního výstupu.



Poznámky

- matice musí být ve stejné složce jako skript.
- kvůli převodu na husté matice je program vhodný pro středně velké matice.

