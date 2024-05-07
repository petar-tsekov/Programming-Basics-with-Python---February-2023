days_entered = int(input())

days_count = 0
examined_patient_count = 0
not_examined_patient_count = 0
doctors_count = 7


for days in range(1, days_entered+1):

    daily_examined_patient_count = 0
    daily_not_examined_patient_count = 0

    if days % 3 == 0 and not_examined_patient_count > examined_patient_count:
        doctors_count += 1

    patient_waiting = int(input())

    if doctors_count >= patient_waiting:
        daily_examined_patient_count += patient_waiting
        daily_not_examined_patient_count = 0
    else:
        daily_not_examined_patient_count = patient_waiting - doctors_count
        daily_examined_patient_count = patient_waiting - daily_not_examined_patient_count
    examined_patient_count += daily_examined_patient_count
    not_examined_patient_count += daily_not_examined_patient_count

print(f'Treated patients: {examined_patient_count}.')
print(f'Untreated patients: {not_examined_patient_count}.')





