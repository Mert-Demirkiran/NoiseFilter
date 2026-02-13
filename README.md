Python üzerinden temel alçak geçirgen filtre

Bu projenin amacı, temel bazda sinyali istenmeyen frekanslardaki gürültülerden arındırmaktır. Pyhton üzerinden NumPy ve SciPy kütüphaneleri kullanılmıştır (Kodu çalıştırmak için CMD üzerinden "pip install numpy scipy matplotlib" komutu ile kütüphaneleri indirebilirsiniz.

5.dereceden butterworth filtre kullanılmıştır, sinyal geçme bandında sinyal kalitesini bozmadan gürültüyü temizler. 

Mavi çizgiler 5Hz frekansa dahil olan gürültülerle birlikteki çıktısını gösterirken turuncu sinüs dalgası bunun filtrelenmiş halini ufak bir gecikme payı ile gösterir. Yatay eksen saniye, dikey eksen genlik (amplitude) gösterir. 
sinyal frekansı 5Hz
kesim frekansı 10H
örnekleme - saniye başı tekrar frekansı ise 500Hz olarak ayarlanmıştır. 


<img width="1000" height="600" alt="filtre" src="https://github.com/user-attachments/assets/5b415ed3-6a68-4b0b-b143-229dc9b96b45" />
