# forest_type_project
Предсказание типа лесного покрова (ВКР учебный)

Данный проект был подготовлен в учебных, ознакомительных целях и не должен быть использован в коммерческой среде. Все ссылки, использованные в данном проекте, были взяты из открытых источников.

Цель проекта.
Прогнозирование типа лесного покрова по картографическим признакам. 

Источник данных. 
Описание датасета.
https://archive.ics.uci.edu/ml/datasets/Covertype

•	Elevation - Высота в метрах

•	Aspect - Аспект в градусах по азимуту

•	Slope - Наклон в градусах

•	Horizontal_Distance_To_Hydrology - Расстояние до ближайших поверхностных водоемов

•	Vertical_Distance_To_Hydrology - Вертикальное расстояние до ближайших водных объектов на поверхности

•	Horizontal_Distance_To_Roadways - Горизонтальное расстояние до ближайшей проезжей части

•	Hillshade_9am (0 to 255 index) - Hillshade индекс в 9 утра, в день летнего солнцестояния

•	Hillshade_Noon (0 to 255 index) - Hillshade индекс в полдень, летнее солнцестояние

•	Hillshade_3pm (0 to 255 index) - Hillshade индекс в 15:00, летнее солнцестояние

•	Horizontal_Distance_To_Fire_Points - Расстояние по горизонтали до ближайших точек возгорания лесных пожаров

•	Wilderness_Area (4 двоичных столбца, 0 = отсутствие или 1 = присутствие) - Обозначение заповедной зоны

•	Soil_Type (40 двоичных столбцов, 0 = отсутствие или 1 = наличие) - Обозначение типа почвы

•	Cover_Type (7 типов, целые числа от 1 до 7) - Обозначение типа лесного покрова

Области дикой природы:
1.	Rawah Wilderness Area
2.	Neota Wilderness Area
3.	Comanche Peak Wilderness Area
4.	Cache la Poudre Wilderness Area
Типы почв:
1.	Cathedral family - Rock outcrop complex, extremely stony.
2.	Vanet - Ratake families complex, very stony.
3.	Haploborolis - Rock outcrop complex, rubbly.
4.	Ratake family - Rock outcrop complex, rubbly.
5.	Vanet family - Rock outcrop complex complex, rubbly.
6.	Vanet - Wetmore families - Rock outcrop complex, stony.
7.	Gothic family.
8.	Supervisor - Limber families complex.
9.	Troutville family, very stony.
10.	Bullwark - Catamount families - Rock outcrop complex, rubbly.
11.	Bullwark - Catamount families - Rock land complex, rubbly.
12.	Legault family - Rock land complex, stony.
13.	Catamount family - Rock land - Bullwark family complex, rubbly.
14.	Pachic Argiborolis - Aquolis complex.
15.	unspecified in the USFS Soil and ELU Survey.
16.	Cryaquolis - Cryoborolis complex.
17.	Gateview family - Cryaquolis complex.
18.	Rogert family, very stony.
19.	Typic Cryaquolis - Borohemists complex.
20.	Typic Cryaquepts - Typic Cryaquolls complex.
21.	Typic Cryaquolls - Leighcan family, till substratum complex.
22.	Leighcan family, till substratum, extremely bouldery.
23.	Leighcan family, till substratum - Typic Cryaquolls complex.
24.	Leighcan family, extremely stony.
25.	Leighcan family, warm, extremely stony.
26.	Granile - Catamount families complex, very stony.
27.	Leighcan family, warm - Rock outcrop complex, extremely stony.
28.	Leighcan family - Rock outcrop complex, extremely stony.
29.	Como - Legault families complex, extremely stony.
30.	Como family - Rock land - Legault family complex, extremely stony.
31.	Leighcan - Catamount families complex, extremely stony.
32.	Catamount family - Rock outcrop - Leighcan family complex, extremely stony.
33.	Leighcan - Catamount families - Rock outcrop complex, extremely stony.
34.	Cryorthents - Rock land complex, extremely stony.
35.	Cryumbrepts - Rock outcrop - Cryaquepts complex.
36.	Bross family - Rock land - Cryumbrepts complex, extremely stony.
37.	Rock outcrop - Cryumbrepts - Cryorthents complex, extremely stony.
38.	Leighcan - Moran families - Cryaquolls complex, extremely stony.
39.	Moran family - Cryorthents - Leighcan family complex, extremely stony.
40.	Moran family - Cryorthents - Rock land complex, extremely stony.

Список файлов использованные при создании проекта
datasets/covtype.data - исходные данные

names_columns.csv – наименования столбцов

static/styles/ - файл my_style.css и image.jpg (стиль страницы html)

templates/index.html – одностраничный сайт

app.py – приложение для прогнозирования

feature_function.py – вспомогательная функция для генерации дополнительных признаков

model_lgbm.pkl – обученная модель LightGBM (формат pkl)

notebook.ipynb – файл с анализом данных и обучением моделей для предсказаний типа лесного покрова

requirements.txt – список использованных библиотек для функциональности программы


Запуск программы

1.	Скачать все файлы на свой локальных компьютер (сохранить все в 1 файловую директорию)
    Или создать клон репозитория GitHub 
    git clone https://github.com/AleksejCagareisvili/forest_type_project.git
2.	Установить необходимые библиотеки из файла requirements.txt для корректного функционирования программы
3.	Запустить в терминале файл – написать в строке терминала $env:FLASK_APP="app.py" (при первом запуске flask должен найти файл app.py) 
4.	Написать в строке терминала flask run
5.	Выход из программы ctrl + c
