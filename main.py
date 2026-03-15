import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import tensorflow as tf
import keras as ks
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense

dataFrame = pd.read_excel(
    "BTK-Akademi-Tensorflow-Araba-FiyaT-Analiz-Projesi\Mercedes.xlsx"
)
print(dataFrame.describe())
print("\n")
print(dataFrame.isnull().sum())
print("\n")
# sbn.displot(dataFrame["price"])
# sbn.displot(dataFrame["year"])
# plt.show()

print(dataFrame.corr(numeric_only=True)["price"].sort_values())
print("\n")
print(dataFrame.sort_values("price", ascending=False).head(20))
print("\n")
print(dataFrame.sort_values("price", ascending=True).head(20))
print("\n")
yuzdeDoksanDokuzDF = dataFrame.sort_values("price", ascending=False).iloc[131:]
print(yuzdeDoksanDokuzDF.describe())
# sbn.displot(yuzdeDoksanDokuzDF["price"])
# plt.show()

print(dataFrame.groupby("year")["price"].mean())
print("\n")
print(yuzdeDoksanDokuzDF.groupby("year")["price"].mean())
print("\n")
dataFrame = yuzdeDoksanDokuzDF
dataFrame = dataFrame[dataFrame.year != 1970]
print(dataFrame.groupby("year")["price"].mean())
print("\n")
dataFrame = dataFrame.drop("transmission", axis=1)

y = dataFrame["price"].values
x = dataFrame.drop("price", axis=1).values
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=10
)

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# model=Sequential()
# model.add(Dense(12,activation="relu"))
# model.add(Dense(12,activation="relu"))
# model.add(Dense(12,activation="relu"))
# model.add(Dense(12,activation="relu"))

# model.add(Dense(1))

# model.compile(optimizer="adam",loss="mse")

# egitimGecmisi=model.fit(x=X_train,y=y_train,validation_data=(X_test,y_test),epochs=300)

# model.save("Araba_FiyaT_Tahmin.keras")

# kayipDF = pd.DataFrame(egitimGecmisi.history)
# kayipDF.to_csv("kayip_verisi.csv", index=False)

kayitliModel = load_model(
    "BTK-Akademi-Tensorflow-Araba-FiyaT-Analiz-Projesi\Araba_FiyaT_Tahmin.keras"
)

kayipVerisi = pd.read_csv(
    "BTK-Akademi-Tensorflow-Araba-FiyaT-Analiz-Projesi\kayip_verisi.csv"
)
print(kayipVerisi.head())
print("\n")
kayipVerisi.plot()
plt.show()

tahminFiyatDizisi = kayitliModel.predict(X_test)
print(mean_absolute_error(y_test, tahminFiyatDizisi))

plt.scatter(y_test, tahminFiyatDizisi)
plt.show()

print("\n")
print(dataFrame.iloc[2])
print("\n")

yeniBirAraba = dataFrame.drop("price", axis=1).iloc[2]
print(yeniBirAraba)
print("\n")

yeniBirAraba = scaler.transform(yeniBirAraba.values.reshape(-1, 5))

print(kayitliModel.predict(yeniBirAraba))
