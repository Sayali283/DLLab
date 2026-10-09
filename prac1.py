import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("Libraries imported")
plt.figure(figsize=(8, 3))
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(image_data[i], cmap="grey", vmin=0, vmax=255)
    plt.title("Image"+ str(i+1))
    plt.axis("off")
    plt.show()
    print("Number of Images:",image_data.shape[0])
    print("Image Height:",image_data.shape[1])
    print("Image width:",image_data.shape[2])
    print("First Image dimensions:",image_data.shape[0])
temprature_data={
    "Date": [
        "2026-10-07",
        "2026-10-08",
        "2026-10-09",
        "2026-10-10",
        "2026-10-11",
    ],
    "Temperature":[45,23,35,38,42]
}
temp_df=pd.DataFrame(temprature_data)
temp_df["Date"]=pd.to_datetime(temp_df["Date"])
print(temp_df)
plt.figure(figsize=(12, 6))
plt.plot(
    temp_df["Date"],
    temp_df["Temperature"],
    marker="o",
    color="red"
)
plt.title("Daily Temprature")
plt.xlabel("Date")
plt.ylabel("Temperature in Celcius")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
print("Dataset Shape:", temp_df.shape)
print("No of rows:", temp_df.shape[0])
print("No of Columns:", temp_df.shape[1])
print("Columns Names:", temp_df.columns.tolist())
employee_data={
    "Employee":["Avinash","Rahul","Ketan","Shri","Kunal"],
    "Salery":[2300,4500,6000,2500,6000],
    "Attendence":[65,78,80,85,43]
}
df=pd.DataFrame(employee_data)
df.to_csv("employee_data.csv", index=False)
print("CSV file Created Successfully!")
loaded_df = pd.read_csv("employee_data.csv")
print(loaded_df)
plt.figure(figsize=(8, 5))
plt.bar(loaded_df["Employee"], loaded_df["Salery"], color="pink")
plt.title("Employee Table")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.ylim(0,7000)
plt.show()
print("Dataset Shape:", loaded_df.shape)
print("No of rows:", loaded_df.shape[0])
print("No of Columns:", loaded_df.shape[1])
print("Columns Names:", loaded_df.columns.tolist())
print("IMAGE DATA")
print("Shape:",image_data.shape)
print("\nTIME_SERIES DATA")
print("Shape:",temp_df.shape)
print("\n CSV DATA")
print("Shape:",loaded_df.shape)
