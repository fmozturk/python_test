# python_test

original.py içinde hatalı birşey yok. Ancak her zaman kodumuzu daha anlaşılır ve verimli hale getirebilmek hem bizim daha sonra hatalarımızı ayıklamamız için kolaylık sağlar, hem de başkaları tarafından daha anlaşılır ve hızlı çalışan bir kodumuz olur.

Yazacağımız program ne kadar kısa olursa olsun, program içinde yapılacak işlemleri küçük parçalara (fonksiyonlar) bölersek, hem hataları tespit etmek kolay olur, hem de daha anlaşılır bir programımız olur.

Yazılım içinde kullandığımız değişken isimleri olabildiğince temsil ettiği değer ile ilgili olmalıdır. Kısa isimler vermek belki hızlı yazılım üretmeyi sağlayabilir ama kod büyüdükçe hangi değişken, ne değer taşıyordu takip etmek zorlaşır. python dili büyük ve küçük harf ayrımı yapabilse de aynı değişken ismi olarak farklı değerler için büyük ve küçük harfli değişken (Örneğin 'N', 'n') kullanmak ilerde sorunlara sebep olacaktır.

for, while gibi döngü parçalarından çıkmak için "break" komutu çok etkilidir. "break" kendisinden sonra gelen komutların işlemesine gerek kalmadan direkt olarak for, while döngüsünün dışına çıkar. Bu programda "break" çok anlamlı gelmese de, "break" komutundan sonra olan komutların işlenmesi için harcanan zaman bu tip program parçalarının günde milyonlarca kez çağrıldıklarında gereksiz kaybedilen dakikalara dönüşür.

print komutunun çıktılarımızı daha anlaşılır bir şekilde verecek bir özelliği vardır. Tabii ki daha karmışık çıktı üreten hazır kütüphaneler bulunmakta.

"for" komutu özünde while kullanmaktadır. Ancak arka tarafta kodu çalıştıran program, "for" gördüğünde kendini ona göre optimize edip, daha hızlı program parçaları çalıştırabilmektedir.
