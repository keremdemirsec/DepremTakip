# Deprem Kontrol Servisi

Bu proje, Türkiye Cumhuriyetinde yaşanan depremleri kontrol eder.

## Başlangıç

Projenin yerel bir kopyasını almak ve çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler

Projenin çalışması için aşağıdaki yazılımlara ihtiyaç vardır:

- Python
- Requests
- BeautifulSoup
- flask

### Kurulum

1. Bu depoyu klonlayın:

    ```bash
    git clone https://github.com/keremdemirsec/DepremTakip
    ```

2. Proje klasörüne gidin:

    ```bash
    cd DepremTakip
    ```

3. Kütüphaneleri Yükleyin:

    ```bash
    pip install requests
    pip install beautifulsoup4
    pip install flask
    ```

4. Kodu Çalıştırın:

    ```bash
    python3 main.py
    ```

## Kullanım

## Web Arayüzü

Tarayıcınızın adres çubuğuna 
```bash 
http://127.0.0.1:5000
```
adresini girerek web arayüzüne erişebilirsiniz. Bu arayüzde, depremleri arayabilir ve detaylı bilgilerini görebilirsiniz.

## API

API'ye erişmek için 
```bash 
http://127.0.0.1:5000/api/earthquakes
```
adresini kullanabilirsiniz. Bu API, JSON formatında deprem verilerini sağlar.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Detaylar için lisans dosyasını inceleyin.

## İletişim

Eğer sorularınız, önerileriniz veya geri bildirimleriniz varsa, bana [e-posta](mailto:keremdemirsec@email.com) üzerinden ulaşabilirsiniz.
