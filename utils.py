def konversi_suhu(nilai, dari, ke):
    dari = str(dari).lower()
    ke = str(ke).lower()

    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: satuan harus 'c', 'f', atau 'k'."
    
    if dari == "k" and nilai < 0:
        return "Error: suhu Kelvin tidak boleh negatif."
    
    if dari == ke:
        return nilai
    
    if dari == "c" and ke == "f":
        return (nilai * 9/5) + 32
    elif dari == "c" and ke == "k":
        return nilai + 273.15
    elif dari == "f" and ke == "c":
        return (nilai - 32) * 5/9
    elif dari == "f" and ke == "k":
        return (nilai - 32) * 5/9 + 273.15
    elif dari == "k" and ke == "c":
        return nilai - 273.15
    elif dari == "k" and ke == "f":
        return (nilai - 273.15) * 9/5 + 32