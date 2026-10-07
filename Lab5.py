# NUMPY LAB EXERCISE
# Hospital Patient Monitoring and Management Analytics System

import numpy as np

# 1. ARRAY CREATION AND DATASET PREPARATION

patients = np.array([
    [101, 45, 37.2, 82, 97, 125, 82, 20, 4],
    [102, 62, 38.1, 96, 94, 145, 90, 30, 7],
    [103, 35, 36.8, 72, 99, 118, 76, 10, 3],
    [104, 71, 39.0, 105, 91, 160, 95, 40, 12],
    [105, 54, 37.5, 88, 96, 135, 85, 25, 6],
    [106, 29, 36.6, 68, 98, 110, 72, 10, 2],
    [107, 66, 38.5, 101, 93, 150, 92, 35, 9],
    [108, 48, 37.0, 78, 97, 128, 80, 5, 5],
    [109, 76, 39.2, 110, 89, 170, 100, 50, 15],
    [110, 41, 36.9, 75, 98, 120, 78, 15, 4]
])


# Column numbers
PATIENT_ID = 0
AGE = 1
TEMPERATURE = 2
HEART_RATE = 3
SPO2 = 4
SYSTOLIC_BP = 5
DIASTOLIC_BP = 6
MEDICATION = 7
STAY = 8

# 1. ARRAY CREATION
print("=" * 65)
print("     HOSPITAL PATIENT MONITORING SYSTEM")
print("=" * 65)

print("\n1. ARRAY CREATION")
print("-" * 65)

print("Patient Dataset:")
print(patients)

# Other NumPy array creation functions
patient_count = np.arange(101, 111)
empty_array = np.empty((2, 2))
zero_array = np.zeros((2, 2))
one_array = np.ones((2, 2))

print("\nPatient IDs using arange():")
print(patient_count)

print("\nZeros array:")
print(zero_array)

print("\nOnes array:")
print(one_array)

# 2. ARRAY ATTRIBUTES
print("\n2. ARRAY ATTRIBUTES")
print("-" * 65)

print("Shape              :", patients.shape)
print("Number of dimensions:", patients.ndim)
print("Total elements     :", patients.size)
print("Data type          :", patients.dtype)
print("Bytes per element  :", patients.itemsize)
print("Total memory       :", patients.nbytes, "bytes")

# 3. INDEXING AND SLICING
print("\n3. INDEXING AND SLICING")
print("-" * 65)

# Patient IDs
patient_ids = patients[:, PATIENT_ID]

print("Patient IDs:")
print(patient_ids)

# Vital signs
vital_signs = patients[:, TEMPERATURE:SYSTOLIC_BP + 1]

print("\nVital Signs:")
print(vital_signs)

# First patient
print("\nFirst Patient:")
print(patients[0])

# Last patient using negative indexing
print("\nLast Patient:")
print(patients[-1])

# First five patients
print("\nFirst Five Patients:")
print(patients[:5])

# Selected patients
print("\nPatients 3 to 6:")
print(patients[2:6])

# Selected columns
print("\nPatient ID, Temperature and SpO2:")
print(patients[:, [PATIENT_ID, TEMPERATURE, SPO2]])

# Last three columns
print("\nLast Three Columns:")
print(patients[:, -3:])

# 2D indexing
print("\nTemperature of Patient 101:")
print(patients[0, TEMPERATURE])


# 4. PATIENT RISK IDENTIFICATION
print("\n4. PATIENT RISK IDENTIFICATION")
print("-" * 65)

temperature_risk = patients[:, TEMPERATURE] > 38
spo2_risk = patients[:, SPO2] < 95
heart_rate_risk = patients[:, HEART_RATE] > 100
bp_risk = patients[:, SYSTOLIC_BP] > 140

print("Temperature above 38°C:")
print(patient_ids[temperature_risk])

print("\nSpO2 below 95%:")
print(patient_ids[spo2_risk])

print("\nHeart rate above 100 bpm:")
print(patient_ids[heart_rate_risk])

print("\nSystolic BP above 140 mmHg:")
print(patient_ids[bp_risk])


# Combine all risk conditions
high_risk = (
    temperature_risk |
    spo2_risk |
    heart_rate_risk |
    bp_risk
)

attention_patients = patients[high_risk]

print("\nPatients requiring medical attention:")
print(patient_ids[high_risk])

# np.where()
risk_indices = np.where(high_risk)

print("\nRisk patient positions using np.where():")
print(risk_indices[0])

print("\nNumber of patients requiring attention:")
print(np.sum(high_risk))


# 5. ELEMENT-WISE MEDICAL CALCULATIONS
print("\n5. ELEMENT-WISE MEDICAL CALCULATIONS")
print("-" * 65)

# Pulse Pressure
pulse_pressure = (
    patients[:, SYSTOLIC_BP]
    - patients[:, DIASTOLIC_BP]
)

print("Pulse Pressure:")
print(pulse_pressure)

# Medication-adjusted value
medication_adjusted = patients[:, MEDICATION] * 1.10

print("\nMedication after 10% adjustment:")
print(np.round(medication_adjusted, 2))

# Percentage change from normal temperature 37°C
temperature_change = (
    (patients[:, TEMPERATURE] - 37)
    / 37
) * 100

print("\nTemperature percentage change from 37°C:")
print(np.round(temperature_change, 2))

# Squared heart rate
heart_rate_squared = np.square(
    patients[:, HEART_RATE]
)

print("\nSquared Heart Rate:")
print(heart_rate_squared)

# Square root of medication dose
medication_sqrt = np.sqrt(
    patients[:, MEDICATION]
)

print("\nSquare Root of Medication Dose:")
print(np.round(medication_sqrt, 2))

# Logarithm of medication
medication_log = np.log(
    patients[:, MEDICATION]
)

print("\nLogarithm of Medication Dose:")
print(np.round(medication_log, 2))

# Exponential transformation of medication
medication_exp = np.exp(
    patients[:, MEDICATION] / 100
)

print("\nExponential Transformation:")
print(np.round(medication_exp, 2))

# Absolute difference between systolic and diastolic BP
bp_difference = np.abs(
    patients[:, SYSTOLIC_BP]
    - patients[:, DIASTOLIC_BP]
)

print("\nAbsolute BP Difference:")
print(bp_difference)

# 6. RESHAPING AND ARRAY MANIPULATION
print("\n6. RESHAPING AND ARRAY MANIPULATION")
print("-" * 65)

# Create a small array for demonstration
sample_data = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print("Original sample array:")
print(sample_data)

# Reshape
reshaped = sample_data.reshape(2, 3)

print("\nReshaped array:")
print(reshaped)

# Flatten
flattened = patients.flatten()

print("\nFlattened patient dataset:")
print(flattened)

# Transpose
transposed = patients.T

print("\nTransposed dataset shape:")
print(transposed.shape)

# Concatenate
extra_patient = np.array([
    [111, 50, 37.1, 80, 97, 130, 82, 20, 5]
])

combined_patients = np.concatenate(
    (patients, extra_patient),
    axis=0
)

print("\nAfter concatenating new patient:")
print(combined_patients)

# Vertical stacking
patient_group_1 = patients[:5]
patient_group_2 = patients[5:]

vertical_stack = np.vstack(
    (patient_group_1, patient_group_2)
)

print("\nVertical Stack Shape:")
print(vertical_stack.shape)

# Horizontal stacking
patient_ids_column = patients[:, PATIENT_ID].reshape(-1, 1)
age_column = patients[:, AGE].reshape(-1, 1)

horizontal_stack = np.hstack(
    (patient_ids_column, age_column)
)

print("\nHorizontal Stack - ID and Age:")
print(horizontal_stack)

# Split dataset
groups = np.array_split(patients, 2)

print("\nFirst patient group:")
print(groups[0])

print("\nSecond patient group:")
print(groups[1])

# 7. STATISTICAL PATIENT ANALYSIS
print("\n7. STATISTICAL PATIENT ANALYSIS")
print("-" * 65)

temperature = patients[:, TEMPERATURE]
heart_rate = patients[:, HEART_RATE]
spo2 = patients[:, SPO2]
medication = patients[:, MEDICATION]
hospital_stay = patients[:, STAY]

print("Temperature Statistics")

print("Total        :", np.sum(temperature))
print("Mean         :", round(np.mean(temperature), 2))
print("Standard Dev :", round(np.std(temperature), 2))
print("Variance     :", round(np.var(temperature), 2))
print("Minimum      :", np.min(temperature))
print("Maximum      :", np.max(temperature))
print("Median       :", np.median(temperature))
print("25th Percent :", np.percentile(temperature, 25))
print("75th Percent :", np.percentile(temperature, 75))


print("\nHeart Rate Statistics")

print("Mean         :", round(np.mean(heart_rate), 2))
print("Standard Dev :", round(np.std(heart_rate), 2))
print("Minimum      :", np.min(heart_rate))
print("Maximum      :", np.max(heart_rate))
print("Median       :", np.median(heart_rate))


print("\nSpO2 Statistics")

print("Mean         :", round(np.mean(spo2), 2))
print("Standard Dev :", round(np.std(spo2), 2))
print("Minimum      :", np.min(spo2))
print("Maximum      :", np.max(spo2))
print("Median       :", np.median(spo2))


# Cumulative medication
cumulative_medication = np.cumsum(medication)

print("\nCumulative Medication Dose:")
print(cumulative_medication)

# Cumulative hospital stay
cumulative_stay = np.cumsum(hospital_stay)

print("\nCumulative Hospital Stay:")
print(cumulative_stay)

print("\nTotal Medication Dose:")
print(np.sum(medication), "mg")

print("\nTotal Hospital Stay:")
print(np.sum(hospital_stay), "days")

# 8. HIGH-RISK AND BEST-CONDITION PATIENTS
print("\n8. HIGH-RISK PATIENTS")
print("-" * 65)

# Lowest SpO2
lowest_spo2_index = np.argmin(spo2)
lowest_spo2_id = patient_ids[lowest_spo2_index]

print(
    "Lowest SpO2:",
    lowest_spo2_id,
    "->",
    spo2[lowest_spo2_index],
    "%"
)

# Highest temperature
highest_temp_index = np.argmax(temperature)
highest_temp_id = patient_ids[highest_temp_index]

print(
    "Highest Temperature:",
    highest_temp_id,
    "->",
    temperature[highest_temp_index],
    "°C"
)

# Highest heart rate
highest_hr_index = np.argmax(heart_rate)
highest_hr_id = patient_ids[highest_hr_index]

print(
    "Highest Heart Rate:",
    highest_hr_id,
    "->",
    heart_rate[highest_hr_index],
    "bpm"
)

# Longest hospital stay
longest_stay_index = np.argmax(hospital_stay)
longest_stay_id = patient_ids[longest_stay_index]

print(
    "Longest Hospital Stay:",
    longest_stay_id,
    "->",
    hospital_stay[longest_stay_index],
    "days"
)

# 9. SORTING AND SEARCHING
print("\n9. SORTING AND SEARCHING")
print("-" * 65)

# Sort by temperature
temperature_order = np.argsort(
    temperature
)

print("Patients sorted by Temperature:")
print(patient_ids[temperature_order])

# Sort by SpO2
spo2_order = np.argsort(
    -spo2
)

print("\nPatients sorted by SpO2 (highest first):")
print(patient_ids[spo2_order])

# Sort by heart rate
heart_rate_order = np.argsort(
    -heart_rate
)

print("\nPatients sorted by Heart Rate (highest first):")
print(patient_ids[heart_rate_order])

# Sort by hospital stay
stay_order = np.argsort(
    -hospital_stay
)

print("\nPatients sorted by Hospital Stay (longest first):")
print(patient_ids[stay_order])

# 10. INTEGRATED HOSPITAL DASHBOARD
print("\n")
print("=" * 65)
print("           HOSPITAL ANALYTICS DASHBOARD")
print("=" * 65)

print("\nTotal Number of Patients :", patients.shape[0])

print("\n--- Average Vital Signs ---")

print(
    "Average Temperature :",
    round(np.mean(temperature), 2),
    "°C"
)

print(
    "Average Heart Rate  :",
    round(np.mean(heart_rate), 2),
    "bpm"
)

print(
    "Average SpO2        :",
    round(np.mean(spo2), 2),
    "%"
)

print(
    "Average Systolic BP :",
    round(np.mean(patients[:, SYSTOLIC_BP]), 2),
    "mmHg"
)

print(
    "Average Diastolic BP:",
    round(np.mean(patients[:, DIASTOLIC_BP]), 2),
    "mmHg"
)


print("\n--- Highest / Lowest Values ---")

print(
    "Lowest SpO2:",
    lowest_spo2_id,
    "(",
    np.min(spo2),
    "%)"
)

print(
    "Highest Temperature:",
    highest_temp_id,
    "(",
    np.max(temperature),
    "°C)"
)

print(
    "Highest Heart Rate:",
    highest_hr_id,
    "(",
    np.max(heart_rate),
    "bpm)"
)

print(
    "Longest Hospital Stay:",
    longest_stay_id,
    "(",
    np.max(hospital_stay),
    "days)"
)


print("\n--- Patients Requiring Immediate Attention ---")

print(
    patient_ids[high_risk]
)

print(
    "Number requiring attention:",
    np.sum(high_risk)
)


print("\n--- Patient Ranking by Risk Indicators ---")

print(
    "Temperature Ranking:",
    patient_ids[temperature_order]
)

print(
    "Heart Rate Ranking:",
    patient_ids[heart_rate_order]
)

print(
    "SpO2 Ranking:",
    patient_ids[spo2_order]
)


print("\n--- Hospital Resource Requirements ---")

print(
    "Total Medication Required:",
    np.sum(medication),
    "mg"
)

print(
    "Total Hospital Bed-Days:",
    np.sum(hospital_stay),
    "days"
)

print(
    "Average Hospital Stay:",
    round(np.mean(hospital_stay), 2),
    "days"
)


print("\n--- Risk Summary ---")

print(
    "Temperature Risk Patients:",
    np.sum(temperature_risk)
)

print(
    "SpO2 Risk Patients:",
    np.sum(spo2_risk)
)

print(
    "Heart Rate Risk Patients:",
    np.sum(heart_rate_risk)
)

print(
    "Blood Pressure Risk Patients:",
    np.sum(bp_risk)
)

print("\n" + "=" * 65)
print("             END OF REPORT")
print("=" * 65)

