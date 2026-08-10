import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "City": ["Ahmedabad", "Surat", "Vadodara", "Rajkot",
             "Gandhinagar", "Bhavnagar", "Jamnagar", "Junagadh"],
    "Cases": [25000, 22000, 15000, 12000, 9000, 7000, 6000, 5000],
    "Recovered": [24000, 21000, 14500, 11500, 8500, 6700, 5700, 4700],
    "Deaths": [350, 280, 200, 150, 110, 90, 75, 60]
}

df = pd.DataFrame(data)

while True:
    print("\nCOVID-19 DATA ANALYSIS")
    print("1. Show Data")
    print("2. Total Cases")
    print("3. Total Recovered")
    print("4. Total Deaths")
    print("5. Search City")
    print("6. Cases Bar Chart")
    print("7. Deaths Bar Chart")
    print("8. Cases Comparison")
    print("9. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        print(df)

    elif choice == "2":
        print("Total Cases :", df["Cases"].sum())

    elif choice == "3":
        print("Total Recovered :", df["Recovered"].sum())

    elif choice == "4":
        print("Total Deaths :", df["Deaths"].sum())

    elif choice == "5":
        city = input("Enter City : ")
        result = df[df["City"].str.lower() == city.lower()]

        if len(result) > 0:
            print(result)
        else:
            print("City Not Found")

    elif choice == "6":
        plt.figure(figsize=(10, 5))
        plt.bar(df["City"], df["Cases"])
        plt.title("COVID-19 Cases by City")
        plt.xlabel("City")
        plt.ylabel("Cases")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif choice == "7":
        plt.figure(figsize=(10, 5))
        plt.bar(df["City"], df["Deaths"])
        plt.title("COVID-19 Deaths by City")
        plt.xlabel("City")
        plt.ylabel("Deaths")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif choice == "8":
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df, x="City", y="Cases")
        plt.title("COVID-19 Cases Comparison")
        plt.xlabel("City")
        plt.ylabel("Cases")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif choice == "9":
        print("Thank You")
        break

    else:
        print("Invalid Choice")