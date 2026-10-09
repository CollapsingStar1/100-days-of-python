import pandas as  pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Group squirrels by Age and count how many were observed doing each activity

activity_by_age = (
    data.groupby("Primary Fur Color")[["Running", "Climbing", "Eating", "Foraging"]].sum()
)
print(activity_by_age)

# Filter for squirrels that are either Black or Cinnamon AND observed in the PM shift
selected_squirrels = data[
    data["Primary Fur Color"].isin(["Black", "Cinnamon"])
    & (data["Shift"] == "PM")
]

print(f"Total matching squirrels: {len(selected_squirrels)}")

shift_color_matrix = pd.crosstab(
    data["Shift"], data["Primary Fur Color"], margins=True
)
print(shift_color_matrix)
