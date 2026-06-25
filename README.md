# YOLOv8-Pose ile Canlı Yüz ve Yorgunluk Algılama Sistemi 🚀

Bu proje, bilgisayar kamerasını kullanarak kullanıcının yüzünün görünürlüğünü anlık olarak takip eden ve belirli bir süre yüz algılanmadığında (yüz kapatıldığında veya kullanıcı uyuyakalıp kafası düştüğünde) sesli uyarı veren bir Yapay Zeka (Bilgisayarlı Görüş) uygulamasıdır.

## 🧠 Projenin Hikayesi ve Mantığı

Proje ilk başta bir "göz kırpma/jumpscare" uygulaması olarak tasarlanmış, ancak geliştirme sürecinde YOLOv8-Pose modelinin nesne algılama karakteristikleri analiz edilerek daha kararlı ve endüstriyel değeri yüksek bir **Yüz/Yorgunluk Denetim Sistemine** dönüştürülmüştür.

YOLOv8-Pose modeli, nesneleri bütünsel desenlere bakarak tanır. Kullanıcı yüzünü kapattığında veya kameradan gizlendiğinde, yüzün merkez üssü olan **Burun (0. İndeks)** noktasının güven skoru (confidence score) aniden düşer. Projede, bu skorların NumPy dizileri (Array) üzerinden anlık filtrelemesi yapılmıştır.

* **Algılama Mekanizması:** Eğer yüzün (burun noktasının) güven skoru `0.4`ün altına düşerse, sistem yüzün kapandığını anlar ve bir zamanlayıcı başlatır.
* **Akıllı Ses Yönetimi:** Yüz `0.5 saniye`den uzun süre kapalı kalırsa sürekli bir uyarı sesi (`ses.mp3`) tetiklenir. `Pygame` kütüphanesinin `get_busy` ve şalter (flag) mantığı kullanılarak, döngü içinde sesin üst üste binip kulak tırmalaması (kesik kesik çalması) engellenmiş, kararlı bir ses döngüsü kurulmuştur.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

* **Python 3:** Projenin ana programlama dili.
* **YOLOv8 (Ultralytics - Pose Model):** İnsan iskelet yapısını ve yüz noktalarını yüksek doğrulukla yakalayan derin öğrenme modeli.
* **OpenCV (cv2):** Kamera akışını yönetmek, ayna görüntüsü oluşturmak ve görsel arayüzü (`cv2.imshow`) çizmek için.
* **Pygame (mixer):** Arka plandaki ses dosyasının donma yapmadan, asenkron ve döngüsel şekilde çalınmasını sağlamak için.
* **NumPy:** YOLO modelinden gelen tensor ve güven skoru verilerini hızlıca işlemek ve indekslemek için.

---

## 🗺️ YOLOv8-Pose İskelet Noktaları (Keypoints) Referansı

Projede yüz tespiti ve takibi yapılırken modelin standart 17 iskelet noktasından yararlanılmıştır. Projenin temel taşını oluşturan indeks haritası şu şekildedir:

```text
[YÜZ NOKTALARI]
0: Burun (Projede yüzün görünürlüğünü denetlemek için bu merkez nokta referans alınmıştır)
1: Sağ Göz
2: Sol Göz
3: Sağ Kulak
4: Sol Kulak

[ÜST VÜCUT]                     [ALT VÜCUT]
5: Sağ Omuz   6: Sol Omuz       11: Sağ Kalça  12: Sol Kalça
7: Sağ Dirsek 8: Sol Dirsek     13: Sağ Diz    14: Sol Diz
9: Sağ Bilek  10: Sol Bilek     15: Sağ Ayak   16: Sol Ayak Bileği
