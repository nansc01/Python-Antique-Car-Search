import pandas as pd
df = pd.read_csv("cars.csv")

df = df[["Model", "MPG", "Horsepower", "Origin"]]

#1 Step 1: Search Car
while(True):
    print("Welcome to Antique Car Search")
    print("===============================")
    print("1 - search car")
    print("2 - Green Best/Worst Report")
    print("3 - Car Origin Report")
    print("0 - Exit")
    
    do = int(input("What do you want to do? "))
    
    if do ==0:
        break;

    if do == 1:
        MinMPG = int(input("Required Min. MPG: "))
        MinHorsepower = int(input("Required Min. Horsepower: "))
        df1 = df[(df["MPG"] >= MinMPG) & (df["Horsepower"] >= MinHorsepower)]
        
        print("\nFound " + str(len(df1)) + " cars matching the criteria\n")
        print(df1["Model"].reset_index().to_string())
        
    elif do ==2:
        avg = df["MPG"].mean()
        minrow = df.MPG.idxmin()
        maxrow = df.MPG.idxmax()
        print("Avg MPG of all car is", avg)
        print("Greenest car is " + str(df.loc[minrow,"Model"]) + " with " + str(df.loc[minrow,"MPG"]) + " MPG.")
        print("Worst car is " + str(df.loc[maxrow,"Model"]) + " with " + str(df.loc[maxrow,"MPG"]) + " MPG.")
        
    elif do ==3:
        org = df[["Origin", "Model"]]
        ret = org.groupby("Origin").count()
        print(ret)