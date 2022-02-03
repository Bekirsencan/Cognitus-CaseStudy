# Cognitus Case Study

Tüm kod parçacıkları Docker Container içerisinde yürütülmek üzere yazıldı.

docker-compose.yml dosyası içerisinde Docker için gerekli olan tüm servisler ve özellikleri belirtilmiştir.

Kodları Docker üzerinde yürütmek için aşağıdaki komutların sırası ile yürütülmesi gerekmektedir.

# Commands

1- docker compose build

2- docker compose up

 Servisler Docker üzerinde çalışmaya başladıktan sonra aşağıdaki komutlar çalıştırılmalıdır. Aksi halde hata verir.

3- docker exec -it algorithm mv ../flask/models/model.pickle ../var/lib/volume

4- docker exec -it algorithm mv ../flask/models/vectorizer.pickle ../var/lib/volume

 Bu komutlar model.pickle ve vectorizer.pickle algorithm ve algorithm_celery servisleri tarafından ulaşılabilmesi adına 
models adlı volume path'ine yazdırmak için gereklidir.

5- docker exec -it web /bin/bash 
 
 Bu komutun ardından aşağıdaki komut çalıştırılmalıdır.
 
6- python manage.py migrate

 Veritabanı üzerinde tablolar oluştuktan sonra Django üzerinden veritabanına veri girişi yapılabilir.
 Veritabanı pgdata adında bir volume'a bağlıdır. web servisi ve algorithm servisi üzerinden veri kaybı
 yaşanmadan işlem yapılabilir.
 
# Notes

- Django uygulamasından Flask uygulamasına istek atarken Docker Network'e bağlı algorithm servisinin IP Adresi'ne
 istek atıldığından bu IP Adresi bilgisayarlar arası değişkenlik gösterebilir. IP Adresini öğrenmek için servisler
 çalıştırılırken algorithm servisi IP Adresi terminalden bulunabilir. Ya da aşağıdaki komut çalıştırılarak
 öğrenilebilir.
 
 docker network inspect network_ismi



 









