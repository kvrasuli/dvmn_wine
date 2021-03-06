# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Запустите сайт командой `python3 main.py`
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Входные данные

- Файл wine_example.xls является образцом входных данных. Дополните эту excel-таблицу своими строками по образцу.
- Путь к тестовому файлу указывается в необязательном аргументе
- По умолчанию аргумент равен 'wine_example.xlsx'

```
python main.py --winetable [your path to test xlsx file]
```
Например, если тестовый файл лежит в папке проекта:
```
python main.py --winetable wine_example.xlsx
```
Пример тестовых данных:
```
| Категория    | Название            | Сорт            | Цена | Картинка                 | Акция                |
|--------------|---------------------|-----------------|------|--------------------------|----------------------|
| Белые вина   | Белая леди          | Дамский пальчик | 399  | belaya_ledi.png          | Выгодное предложение |
| Напитки      | Коньяк классический |                 | 350  | konyak_klassicheskyi.png |                      |
| Белые вина   | Ркацители           | Ркацители       | 499  | rkaciteli.png            |                      |
| Красные вина | Черный лекарь       | Качич           | 399  | chernyi_lekar.png        |                      |
| Красные вина | Хванчкара           | Александраули   | 550  | hvanchkara.png           |                      |
| Белые вина   | Кокур               | Кокур           | 450  | kokur.png                |                      |
| Красные вина | Киндзмараули        | Саперави        | 550  | kindzmarauli.png         |                      |
| Напитки      | Чача                |                 | 299  | chacha.png               | Выгодное предложение |
| Напитки      | Коньяк кизиловый    |                 | 350  | konyak_kizilovyi.png     |                      |
```

## Установка зависимостей

Python 3 должен быть установлен. Установить зависимости:
```
pip install -r requirements.txt
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
