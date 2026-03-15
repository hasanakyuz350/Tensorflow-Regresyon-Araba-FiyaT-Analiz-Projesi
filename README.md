🚗# Mercedes-Benz Fiyat Tahmin Projesi (TensorFlow & Keras)

Bu proje, Mercedes-Benz otomobil verilerini analiz ederek araçların piyasa değerini tahmin etmek amacıyla geliştirilmiş bir uçtan uca makine öğrenmesi (regresyon) projesidir.

## 📌 Proje Özeti
Projede, araçların yılı, kilometresi, motor gücü ve yakıt tüketimi gibi özellikler kullanılarak fiyat tahmini yapılmaktadır. Model, TensorFlow/Keras kütüphanesi kullanılarak bir Yapay Sinir Ağı (ANN) mimarisi üzerine inşa edilmiştir.

## 📊 Veri Seti Hakkında
Veri seti Mercedes-Benz araçların teknik özelliklerini içermektedir:
- **Year:** Aracın üretim yılı.
- **Mileage:** Aracın toplam kilometresi.
- **Tax:** Yıllık vergisi.
- **MPG:** Yakıt verimliliği (mil başına galon).
- **Engine Size:** Motor hacmi.
- **Price:** Hedef değişkenimiz (Tahmin edilecek fiyat).

*Not: Veri ön işleme aşamasında, fiyatı aşırı yüksek olan (outlier) uç değerler model performansını artırmak amacıyla temizlenmiştir.*

## 🛠️ Kullanılan Teknolojiler & Kütüphaneler
- **Python 3.11.0**
- **TensorFlow & Keras:** Derin öğrenme modelinin oluşturulması ve eğitilmesi.
- **Pandas & NumPy:** Veri manipülasyonu ve analizi.
- **Matplotlib & Seaborn:** Veri görselleştirme (Fiyat dağılımı, korelasyon matrisi vb.).
- **Scikit-learn:** Veriyi ölçeklendirme (MinMaxScaler) ve eğitim/test setine ayırma.

## 🚀 Model Mimarisi
Model, ardışık (Sequential) bir yapıya sahiptir:
- 4 adet gizli katman (Her biri 12 nöron, ReLU aktivasyon fonksiyonu).
- 1 adet çıkış katmanı (Regresyon için doğrusal).
- Optimizer: **Adam**
- Loss Fonksiyonu: **MSE (Mean Squared Error)**

## 📈 Sonuçlar ve Performans
- Model eğitimi sırasında elde edilen kayıp (loss) verileri `kayip_verisi.csv` dosyasına kaydedilmiştir.
- Eğitim ve doğrulama kayıpları grafikler üzerinden takip edilerek aşırı öğrenme (overfitting) kontrol edilmiştir.

## 📂 Dosya Yapısı
- `main.py`: Veri işleme, model eğitimi ve değerlendirme kodları.
- `Mercedes.xlsx`: Ham veri seti.
- `Araba_FiyaT_Tahmin.keras`: Eğitilmiş ve kullanıma hazır model dosyası.
- `kayip_verisi.csv`: Eğitim süreci boyunca kaydedilen loss değerleri.
