# Generated by Django 2.1.2 on 2018-10-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aichi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '愛知',
            },
        ),
        migrations.CreateModel(
            name='Akita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '秋田',
            },
        ),
        migrations.CreateModel(
            name='Aomori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '青森',
            },
        ),
        migrations.CreateModel(
            name='Chiba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '千葉',
            },
        ),
        migrations.CreateModel(
            name='Ehime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '愛媛',
            },
        ),
        migrations.CreateModel(
            name='Fukui',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '福井',
            },
        ),
        migrations.CreateModel(
            name='Fukuoka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '福岡',
            },
        ),
        migrations.CreateModel(
            name='Fukushima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '福島',
            },
        ),
        migrations.CreateModel(
            name='Gifu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '岐阜',
            },
        ),
        migrations.CreateModel(
            name='Gunma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '群馬',
            },
        ),
        migrations.CreateModel(
            name='Hiroshima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '広島',
            },
        ),
        migrations.CreateModel(
            name='Hokkaido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '北海道',
            },
        ),
        migrations.CreateModel(
            name='Hyogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '兵庫',
            },
        ),
        migrations.CreateModel(
            name='Ibaraki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '茨城',
            },
        ),
        migrations.CreateModel(
            name='Ishikawa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '石川',
            },
        ),
        migrations.CreateModel(
            name='Iwate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '岩手',
            },
        ),
        migrations.CreateModel(
            name='Kagawa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '香川',
            },
        ),
        migrations.CreateModel(
            name='Kagoshima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '鹿児島',
            },
        ),
        migrations.CreateModel(
            name='Kanagawa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '神奈川',
            },
        ),
        migrations.CreateModel(
            name='Kochi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '高知',
            },
        ),
        migrations.CreateModel(
            name='Kumamoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '熊本',
            },
        ),
        migrations.CreateModel(
            name='Kyoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '京都',
            },
        ),
        migrations.CreateModel(
            name='Mie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '三重',
            },
        ),
        migrations.CreateModel(
            name='Miyazaki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '宮崎',
            },
        ),
        migrations.CreateModel(
            name='Nagano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '長野',
            },
        ),
        migrations.CreateModel(
            name='Nagasaki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '長崎',
            },
        ),
        migrations.CreateModel(
            name='Nara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '奈良',
            },
        ),
        migrations.CreateModel(
            name='Niigata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '新潟',
            },
        ),
        migrations.CreateModel(
            name='Oita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '大分',
            },
        ),
        migrations.CreateModel(
            name='Okayama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '岡山',
            },
        ),
        migrations.CreateModel(
            name='Okinawa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '沖縄',
            },
        ),
        migrations.CreateModel(
            name='Osaka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '大阪',
            },
        ),
        migrations.CreateModel(
            name='Saga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '佐賀',
            },
        ),
        migrations.CreateModel(
            name='Saitama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '埼玉',
            },
        ),
        migrations.CreateModel(
            name='Shiga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '滋賀',
            },
        ),
        migrations.CreateModel(
            name='Shimane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '島根',
            },
        ),
        migrations.CreateModel(
            name='Shizuoka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '静岡',
            },
        ),
        migrations.CreateModel(
            name='Tochigi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '栃木',
            },
        ),
        migrations.CreateModel(
            name='Tokushima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '徳島',
            },
        ),
        migrations.CreateModel(
            name='Tokyo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '東京',
            },
        ),
        migrations.CreateModel(
            name='Tottori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '鳥取',
            },
        ),
        migrations.CreateModel(
            name='Toyama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '富山',
            },
        ),
        migrations.CreateModel(
            name='Wakayama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '和歌山',
            },
        ),
        migrations.CreateModel(
            name='Yamagata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '山形',
            },
        ),
        migrations.CreateModel(
            name='Yamaguchi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '山口',
            },
        ),
        migrations.CreateModel(
            name='Yamanashi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=55)),
                ('city_name_ja', models.CharField(max_length=55)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('predicted_data', models.FileField(upload_to='data/')),
            ],
            options={
                'verbose_name_plural': '山梨',
            },
        ),
        migrations.AlterModelOptions(
            name='miyagi',
            options={'verbose_name_plural': '宮城'},
        ),
    ]
