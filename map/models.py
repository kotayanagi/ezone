from django.db import models

# Create your models here.

#Hokkaido
class Hokkaido(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "北海道"

#Tohoku
class Aomori(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "青森"

class Akita(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "秋田"

class Iwate(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "岩手"

class Miyagi(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "宮城"
 
class Yamagata(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "山形"
    
class Fukushima(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "福島"

class Niigata(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "新潟"

#Kanto
class Tochigi(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "栃木"

class Ibaraki(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "茨城"

class Saitama(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "埼玉"

class Chiba(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "千葉"

class Tokyo(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "東京"

class Kanagawa(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "神奈川"

class Shizuoka(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "静岡"

#Chubu
class Yamanashi(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "山梨"

class Gunma(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "群馬"

class Nagano(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "長野"

class Gifu(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "岐阜"

class Ishikawa(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "石川"

class Aichi(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "愛知"

class Toyama(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "富山"

class Fukui(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "福井"

class Mie(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "三重"

#Kansai
class Shiga(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "滋賀"

class Kyoto(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "京都"

class Osaka(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "大阪"

class Nara(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "奈良"

class Wakayama(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "和歌山"

class Hyogo(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "兵庫"

#Chugoku
class Tottori(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "鳥取"

class Okayama(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "岡山"

class Hiroshima(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "広島"

class Shimane(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "島根"

class Yamaguchi(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "山口"

#Shikoku
class Tokushima(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "徳島"

class Kagawa(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "香川"

class Ehime(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "愛媛"

class Kochi(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "高知"

#Kyushu
class Saga(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "佐賀"

class Fukuoka(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "福岡"

class Nagasaki(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "長崎"

class Oita(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "大分"

class Kumamoto(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "熊本"

class Miyazaki(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "宮崎"

class Kagoshima(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "鹿児島"

#Okinawa
class Okinawa(models.Model):
    city_name = models.CharField(max_length=55)
    city_name_ja = models.CharField(max_length=55)
    post_date = models.DateTimeField(auto_now=True)
    predicted_data = models.FileField(upload_to='data/')
    wind_data = models.FileField(upload_to='data/', null=True)
    wind_tendency = models.FileField(upload_to='data/', null=True)

    class Meta:
        verbose_name_plural = "沖縄"
