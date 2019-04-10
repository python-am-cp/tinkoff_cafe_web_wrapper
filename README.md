Tinkoff Cafe Web Wrapper
===========


Мы разрабатываем веб-обертку в виде SPA для помощи команде Tinkoff Cafe в тестировании их гипотез, в т.ч. проведении автоматической кросс-валидации и выведении результатов. 

[Сверстанная страница](https://python-am-cp.github.io/tinkoff_cafe_web_wrapper/frontend/index.html)


   Схема логики
   ===============
   Мы получам от аналитиков: 
   +Название исследования
   +Описание исследования
   +Имя
   +Электронную почту
   
   +train.py -- обучающий скрипт
   +train.csv -- Все данные
   +menu-train.csv -- Меню по дням (вспомогательные выведенные данные)
   +menu-tagged.csv -- Блюда с тегами (вспомогательные выведенные данные)
   +predict.py -- скрипт-предсказатель
   
   
   Приложение должно разделить train.csv в некоторой пропорции и провести контрольные вычисления, включая различные формулы  сопоставления предсказания с ответами из тестовых данных. Результат в виде таблицы/векторов результатов по формулам пока что планируется присылать на электронную почту.
   ![](im/Снимок%20экрана%20(463).png)
  
   Распределение обязанностей:
   ===========================
   ![alt text](https://github.com/python-am-cp/tinkoff_cafe_web_wrapper/blob/develop/im/charges.png)
   
   Используемые технологии:
   ========================
   ![alt text](https://github.com/python-am-cp/tinkoff_cafe_web_wrapper/blob/develop/im/tech.png)
   
   План разработки:
   ================
   ![alt text](https://github.com/python-am-cp/tinkoff_cafe_web_wrapper/blob/develop/im/Untitled%20Diagram.png)
   
   Обратная связь:
   ===============
   * [Артемий](https://vk.com/temimo)
   * [Тимур](https://vk.com/subelta)
   * [Александр](https://vk.com/papernyuk)
   
   Другие полезные ссылки:
   =======================

+ [Cтек технологий](https://docs.google.com/spreadsheets/d/10_ih1ONghtAGQ29BRwEeNhrGonIFp6qVrk0CyaJH7SM/edit?usp=sharing)

+ [Список дел и материалов для изучения](https://trello.com/b/sYs31Fnj/tinkoff-web) 





