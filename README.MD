Самая первая кнопка — падающий список с названиями эффектов. 
По списку можно передвигаться при помощи стрелок вверх-вниз, либо при помощи окошка поиска.
Рядом с падающим списком — галочка. Со включённой галочкой идёт поиск по ID эффекта, без галочки идёт поиск по названию эффекта.

При клике на название эффекта прога загружает и выводит на экран инфу.

В случае, если поле для инфы называется "0xЧисло", то при наведении на это поле должно появиться всплывающее окно "Заметки". 
В эти заметки пользователь вводит данные с клавиатуры, прога сохраняет заметки в .txt файле.

Для каждого поля с инфой свои заметки.

СТРУКТУРА КАЖДОГО ЭФФЕКТА (блока) 
 
0x00 Название эффекта 
0x10 (16bit) — ID эффекта
 
 
следующие данные должны отображаться в РЕДАКТИРУЕМЫХ ПОЛЯХ, и они должны быть представлены в указанном формате. (float32, 8bit hex).  Если указано "галочка", то вместо редактируемого поля вставь галочку — без галки значение 00, с галкой — 01. 
 
Структура проги — сначала напиши то, что находится в кавычках (просто текст), под текстом — РЕДАКТИРУЕМОЕ ПОЛЕ 
 
Подписать группу как "BASE" 
0x12 "???ANIM DATA" (8bit) 
0x14 "0x14" (32bit hex string) 
0x18 "Effect attack element scaling" (8bit) 
0x19 "0x19" (8bit) 
0x1a "Damage ID"(8bit) 
0x1c "0x1c" (32bit hex string) 
0x20 "0x20" (32bit hex string) 
0x24 "0x24" (32bit hex string) 
0x28 Effect model (64bit hex string) 
0x34 "0x34" (32bit hex string) 
 
Подписать эту группу как "EFFECT FLAGS" 
 
0x38 Source bone separation (8bit галочка) 
0x39 T-pose(8bit галочка) 
0x3a Bounce enabled(8bit галочка) 
0x3b Dissapear after collision (8bit галочка) 
0x3c Falls through the ground (8bit галочка) 
 
Подписать группу как "PHYSICS" 
 
0x3d Number of bounces (8bit) 
0x3e "0x3e" (8bit) 
0x3f "0x3f" (8bit) 
0x40 "0x40" (32bit float single) 
0x44 "0x44" (32bit float single) 
0x48 "0x48" (32bit float single) 
0x4c "0x4c" (32bit float single) 
0x50 "Effect weight" (32bit float single) 
0x54 "Effect angle pos X" (32bit float single) 
0x58 "Effect angle pos Y" (32bit float single) 
0x60 "Effect speed" (32bit float single) 
0x64 "0x64" (32bit float single) 
 
Подписать группу как "HITBOX" 
 
0x68 "flag1collision" (8bitгалочка) 
0x69 "flag2" (8bit галочка) 
0x6a "flag3" (8bit галочка) 
0x6b "flag4behaviour" (8bit галочка) 
0x6c "flag5" (8bit) 
0x6d "flag6" (8bit) 
0x6e Effect hitbox width (32bit float single) 
0x70 Effect hitbox height (32bit float single) 
0x74-0x7f Effect collision placeholder (96 bit hex string) 
 
Группу подписать как "APPEARANCE" 
 
0x84 "gravity" (8bit) 
0x85 "Animation default/smooth" (8bit) 
0x86 "Animation renderer" (8bit) 
0x87 "0x87" (8bit) 
0x88 "0x88 ~ 0x68" (8bit) 
 
0x90 "SOUND DATA" (32bit float single) 
0x98 "ANIM DATA" (8bit) 
0xa0 "Animation timer" (32bit float single) 


Ну и кнопка "сохранить файл" которая применяет изменения



Список эффектов прога должна составить как в проге Льва. В падающем списке должны показываться имена для эффектов.

Имя для эффекта — первые 0x10(16 в десятеричной системе счисления) байтов. Читается как текстовая строка.
Прога сама создаёт .txt файл. В той папке, в которой лежит исполняемый файл. И читает его автоматически при запуске
 
Пусть у неё будет имя "Notes.txt"
 
В таком случае она всегда будет при запуске искать Notes.txt в своей папке.

Если он отсутствует, то прога создаст файл.

[(32bit hex) + (single float) - означает, что нужно сделать два поля, с 4 байтами в хексе, и поле с сингл флоатом, данные беруться из одного и того же оффсета 
 
(32bit hex) - означает, что нужно вывести в поле 4 байта, в ШЕСТНАДЦАТЕРИЧНОЙ СИСТЕМЕ СЧИСЛЕНИЯ(смотреть приложеный скриншот в качестве примера) 
 
(string) - означает, что нужно вывести в поле строку текста из заданного оффсета(длина строки в байтах написана после названия в ТЗ) 
 
(8bit переключатель) - означает, что нужно вывести кнопку-переключатель, если переключатель включен, в данный байт записывается 01, если переключатель выключен, записывается 00(по умолчанию программа должна считывать значения из файла, и выставлять актуальные положения переключателей) 

 
группа "Effect: " 
0x00 "Effect name" (string) длина: 16 байт 
0x10 "ID" (16bit) 
 
группа "Base" 
0x12 "unknown Animation param" (8bit) 
0x14 "unknown param 14" (32bit hex) + (single float) 
 
0x18 "Damage on/off" (8bit) 
0x19 "unknown param 19" (8bit) 
0x1a "damageparam ID"(8bit) 
0x1c "unknown param 1c" (32bit hex) + (single float) 
0x20 "unknown param 20" (32bit hex) + (single float) 
0x24 "unknown param 24" (32bit hex) + (single float) 
0x28 "Effect model" (string) длина: 12 байт 
0x34 "unknown param 34" (32bit hex) + (single float) 
 
группа "Effect flags 1" 
 
0x38 "Source bone separation" (8bit переключатель) 
0x39 "T-pose" (8bit переключатель) 
0x3a "Bounce enabled" (8bit переключатель) 
0x3b "Dissapear after collision" (8bit переключатель) 
0x3c "Falls through the ground" (8bit переключатель) 
 
группа "Physics" 
 
0x3d Number of bounces (8bit) 
0x3e "unknown param 3e" (8bit) 
0x3f "unknown param 3f" (8bit) 
0x40 "unknown param 40" (32bit float single) 
0x44 "unknown param 44" (32bit float single) 
0x48 "unknown param 48" (32bit float single) 
0x4c "unknown param 4c" (32bit float single) 
0x50 "Effect weight" (32bit float single) 
0x54 "Effect angle pos X" (32bit float single) 
0x58 "Effect angle pos Y" (32bit float single) 
0x60 "Effect speed" (32bit float single) 
0x64 "unknown param 64" (32bit float single) 
 
группа "Hitbox" 
 
0x68 "flag 68 (collision)" (8bit переключатель) 
0x69 "flag 69" (8bit переключатель) 
0x6a "flag 6a" (8bit переключатель) 
0x6b "flag 6b (behavior)" (8bit переключатель) 
0x6e "Effect hitbox width" (32bit float single) 
0x70 "Effect hitbox height" (32bit float single) 
0x74-0x7f "collision placeholder" (string) длина: 12 байт 
 
группа "Appearance" 
 
0x84 "gravity" (8bit) 
0x85 "Animation default/smooth" (8bit) 
0x86 "Animation renderer" (8bit) 
0x87 "unknown param 87" (8bit) 
0x88 "unknown param 88 ~ 0x68" (8bit) 
 
группа "Animation" 
 
0x90 "unknown Sound param" (32bit float single) 
0x98 "unknown Animation param" (8bit) 
0xa0 "Animation timer" (32bit float single)

