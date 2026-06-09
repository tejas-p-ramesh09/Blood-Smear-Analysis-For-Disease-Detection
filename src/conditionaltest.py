# Normal ranges for different groups
def diagnose(gen, totalwbc1, totalplatelets1, totalrbc1, age):
    # Convert parameters to integers
    totalwbc1 = int(totalwbc1)
    totalplatelets1 = int(totalplatelets1)
    totalrbc1 = int(totalrbc1)
    
    # Normalize gender input
    gen = gen.lower()

    if int(age)>12:
        # Determine normal RBC range based on gender or age group
        if gen == "male":
            rbc_normal_min, rbc_normal_max = 4700000, 6100000
        elif gen == "female":
            rbc_normal_min, rbc_normal_max = 4200000, 5400000
        else:
            return "Invalid gender"
    else:
        rbc_normal_min, rbc_normal_max = 4100000, 5500000


    # WBC normal range
    if int(age)<12:
        wbc_normal_min, wbc_normal_max = 5000, 10000
    else:
        wbc_normal_min, wbc_normal_max = 4000, 11000

    # Platelet normal range
    platelet_normal_min, platelet_normal_max = 150000, 450000

    # Diagnosis logic
    if (
        wbc_normal_min <= totalwbc1 <= wbc_normal_max
        and platelet_normal_min <= totalplatelets1 <= platelet_normal_max
        and rbc_normal_min <= totalrbc1 <= rbc_normal_max
    ):
        Detected_as = "Normal"
    elif totalrbc1 < rbc_normal_min and totalrbc1 >= 3000000:
        Detected_as = "Anemia"
    elif totalrbc1 < 3000000 and totalwbc1 < wbc_normal_min:
        Detected_as = "Leukopenia"
    elif totalrbc1 < 2500000 or totalwbc1 > wbc_normal_max or totalplatelets1 < platelet_normal_min:
        Detected_as = "Blood Cancer"
    else:
        Detected_as = "Leukopenia"
    
    return Detected_as

# # Example usage for normal
# gen = "male"
# age=35
# totalwbc1 = 5000
# totalplatelets1 = 150001
# totalrbc1 = 4700001


# # Example usage for Anemia
# gen = "male"
# age=35
# totalwbc1 = 5000
# totalplatelets1 = 150001
# totalrbc1 = 3000000


# # Example usage for Leukopenia
# gen = "male"
# age=35
# totalwbc1 = 5000
# totalplatelets1 = 150001
# totalrbc1 = 2900000
#print(diagnose(gen, totalwbc1, totalplatelets1, totalrbc1,age))
