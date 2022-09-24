# Сервис для поиска фильмов

#### В данном приложении можно просматривать списки фильмов, режисеров и жанров, также реализована аутентификация, авторизация пользователей, хэширование паролей.

#### Данный проект я делал в целях улучшения своих практических знаний Python + Flask, SQLAlchemy, Marshmallow, JWT, REST, CRUD, CBV

### Установка зависимостей

    pip install -r requirements.txt

### Запуск приложения

    app.py -p

# Описание эндпоинтов

## Представления movies, genres и directors

### Получить список всех фильмов

#### Request

`GET /movies/`

    curl --location --request GET 'http://localhost:10001/movies/'

#### Response

<details><summary>Список фильмов</summary>

    Status: 200 OK

    [
        {
            "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
            "id": 1,
            "description": "Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
            "title": "Йеллоустоун",
            "year": 2018,
            "rating": 8
        },
        {
            "trailer": "https://www.youtube.com/watch?v=lmB9VWm0okU",
            "id": 2,
            "description": "США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.",
            "title": "Омерзительная восьмерка",
            "year": 2015,
            "rating": 7
        },
        {
            "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo",
            "id": 3,
            "description": "События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...",
            "title": "Вооружен и очень опасен",
            "year": 1978,
            "rating": 6
        },
        {
            "trailer": "https://www.youtube.com/watch?v=2Dty-zwcPv4",
            "id": 4,
            "description": "Эксцентричный охотник за головами, также известный как Дантист, промышляет отстрелом самых опасных преступников. Работенка пыльная, и без надежного помощника ему не обойтись. Но как найти такого и желательно не очень дорогого? Освобождённый им раб по имени Джанго – прекрасная кандидатура. Правда, у нового помощника свои мотивы – кое с чем надо сперва разобраться.",
            "title": "Джанго освобожденный",
            "year": 2012,
            "rating": 8
        },
        {
            "trailer": "https://youtu.be/VISiqVeKTq8",
            "id": 5,
            "description": "История превращения застенчивого парня Реджинальда Дуайта, талантливого музыканта из маленького городка, в суперзвезду и культовую фигуру мировой поп-музыки Элтона Джона.",
            "title": "Рокетмен",
            "year": 2019,
            "rating": 7
        },
        {
            "trailer": "https://www.youtube.com/watch?v=sgOhxneHkiE",
            "id": 6,
            "description": "Али - молодая амбициозная девушка из маленького городка с чудесным голосом, совсем недавно потеряла своих родителей. Теперь никому не нужная, она отправляется в большой город Лос-Анджелес, где устраивается на работу у Тесс, хозяйки ночного клуба «Бурлеск». За короткое время она находит друзей, поклонников и любовь всей своей жизни. Но может ли сказка длиться вечно? Ведь немало людей завидует этой прекрасной танцовщице...",
            "title": "Бурлеск",
            "year": 2010,
            "rating": 6
        },
        {
            "trailer": "https://www.youtube.com/watch?v=YxzS_LzWdG8",
            "id": 7,
            "description": "Рокси Харт мечтает о песнях и танцах и о том, как сравняться с самой Велмой Келли, примадонной водевиля. И Рокси действительно оказывается с Велмой в одном положении, когда несколько очень неправильных шагов приводят обеих на скамью подсудимых.",
            "title": "Чикаго",
            "year": 2002,
            "rating": 7
        },
        {
            "trailer": "https://www.youtube.com/watch?v=lpiMCTd87gE",
            "id": 8,
            "description": "Париж, 1899 год. Знаменитый ночной клуб «Мулен Руж» — это не только дискотека и шикарный бордель, но и место, где, повинуясь неудержимому желанию прочувствовать атмосферу праздника, собираются страждущие приобщиться к красоте, свободе, любви и готовые платить за это наличными.",
            "title": "Мулен Руж",
            "year": 2001,
            "rating": 7
        },
        {
            "trailer": "https://www.youtube.com/watch?v=Q9PxDPOo1jw",
            "id": 9,
            "description": "Эндрю мечтает стать великим. Казалось бы, вот-вот его мечта осуществится. Юношу замечает настоящий гений, дирижер лучшего в стране оркестра. Желание Эндрю добиться успеха быстро становится одержимостью, а безжалостный наставник продолжает подталкивать его все дальше и дальше – за пределы человеческих возможностей. Кто выйдет победителем из этой схватки?",
            "title": "Одержимость",
            "year": 2013,
            "rating": 8
        },
        {
            "trailer": "https://www.youtube.com/watch?v=LVdRR6m5OdQ",
            "id": 10,
            "description": "Авторитетный взгляд на историю культового электронного стиля глазами самых известных его представителей и последователей. Увлекательный рассказ о феномене итало-диско и возможность увидеть своими глазами, что творилось на главных танцполах 80-х.",
            "title": "Наследие итало-диско",
            "year": 2017,
            "rating": 0
        },
        {
            "trailer": "https://www.youtube.com/watch?v=RnFrrzg1OEQ",
            "id": 11,
            "description": "Юность певца Джонни Кэша была омрачена гибелью его брата и пренебрежительным отношением отца. Военную службу будущий певец проходил в Германии. После свадьбы и рождения дочери он выпустил свой первый хит и вскоре отправился в турне по США вместе с Джерри Ли Льюисом, Элвисом Пресли и Джун Картер, о которой он безнадёжно мечтал целых десять лет.",
            "title": "Переступить черту",
            "year": 2005,
            "rating": 7
        },
        {
            "trailer": "https://www.youtube.com/watch?v=DOlTmIhEsg0",
            "id": 12,
            "description": "Наследник знаменитого дома Атрейдесов Пол отправляется вместе с семьей на одну из самых опасных планет во Вселенной — Арракис. Здесь нет ничего, кроме песка, палящего солнца, гигантских чудовищ и основной причины межгалактических конфликтов — невероятно ценного ресурса, который называется меланж. В результате захвата власти Пол вынужден бежать и скрываться, и это становится началом его эпического путешествия. Враждебный мир Арракиса приготовил для него множество тяжелых испытаний, но только тот, кто готов взглянуть в глаза своему страху, достоин стать избранным.",
            "title": "Дюна",
            "year": 2021,
            "rating": 8
        },
        {
            "trailer": "https://www.youtube.com/watch?v=lneNCBIXD4I",
            "id": 13,
            "description": "Это история любви старлетки, которая между прослушиваниями подает кофе состоявшимся кинозвездам, и фанатичного джазового музыканта, вынужденного подрабатывать в заштатных барах. Но пришедший к влюбленным успех начинает подтачивать их отношения.",
            "title": "Ла-Ла Ленд",
            "year": 2016,
            "rating": 8
        },
        {
            "trailer": "https://www.youtube.com/watch?v=TvAbtsQKrHA",
            "id": 14,
            "description": "Рассказ о начале творческого пути Виктора Цоя и группы «Кино», о его взаимоотношениях с Майком Науменко, его женой Натальей и многими, кто был в авангарде рок-движения Ленинграда 1981 года.",
            "title": "Лето",
            "year": 2018,
            "rating": 7
        },
        {
            "trailer": "https://www.youtube.com/watch?v=NMSUEhDWXH0",
            "id": 15,
            "description": "Джек Торренс с женой и сыном приезжает в элегантный отдалённый отель, чтобы работать смотрителем во время мертвого сезона. Торренс здесь раньше никогда не бывал. Или это не совсем так? Ответ лежит во мраке, сотканном из преступного кошмара.",
            "title": "Сияние ",
            "year": 1980,
            "rating": 8
        },
        {
            "trailer": "https://www.youtube.com/watch?v=n7GlLxV_Igk",
            "id": 16,
            "description": "Что если в один прекрасный день в тебя вселяется существо-симбиот, которое наделяет тебя сверхчеловеческими способностями? Вот только Веном – симбиот совсем недобрый, и договориться с ним невозможно. Хотя нужно ли договариваться?.. Ведь в какой-то момент ты понимаешь, что быть плохим вовсе не так уж и плохо. Так даже веселее. В мире и так слишком много супергероев! Мы – Веном!",
            "title": "Веном",
            "year": 2018,
            "rating": 6
        },
        {
            "trailer": "https://www.youtube.com/watch?v=9H_t5cdszFU",
            "id": 17,
            "description": "К своим 16 годам старшеклассник Донни уже знает, что такое смерть. После несчастного случая, едва не стоившего ему жизни, Донни открывает в себе способности изменять время и судьбу. Произошедшие с ним перемены пугают его окружение — родителей, сестер, учителей, друзей и любимую девушку.",
            "title": "Донни Дарко",
            "year": 2001,
            "rating": 8
        },
        {
            "trailer": "https://www.youtube.com/watch?v=vsb8762mE6Q",
            "id": 18,
            "description": "Уже немолодой школьный учитель музыки Джо Гарднер всю жизнь мечтал выступать на сцене в составе джазового ансамбля. Однажды он успешно проходит прослушивание у легендарной саксофонистки и, возвращаясь домой вне себя от счастья, падает в люк и умирает. Теперь у Джо одна дорога — в Великое После, но он сбегает с идущего в вечность эскалатора и случайно попадает в Великое До. Тут новенькие души обретают себя, и у будущих людей зарождаются увлечения, мечты и интересы. Джо становится наставником упрямой души 22, которая уже много веков не может найти свою искру и отправиться на Землю.",
            "title": "Душа",
            "year": 2020,
            "rating": 8
        },
        {
            "trailer": "https://www.youtube.com/watch?v=rKsdTuvrF5w",
            "id": 19,
            "description": "Париж. 1910 год. Ужасный монстр, напоминающий гигантское насекомое, нагоняет страх на всю Францию. Застенчивый киномеханик и неутомимый изобретатель начинают охоту на него. В этой погоне они знакомятся со звездой кабаре, сумасшедшим ученым и его умной обезьянкой и, наконец, самим монстром, который оказывается совсем не страшным. Теперь безобидное, как блоха, чудовище ищет у своих новых друзей защиты от вредного начальника городской полиции.",
            "title": "Монстр в Париже",
            "year": 2010,
            "rating": 6
        },
        {
            "trailer": "https://www.youtube.com/watch?v=Qjpmysz4x-4",
            "id": 20,
            "description": "От Великого потопа зверей спас ковчег. Но спустя полгода скитаний они готовы сбежать с него куда угодно. Нервы на пределе. Хищники готовы забыть про запреты и заглядываются на травоядных. Единственное спасение — найти райский остров. Там простор и полно еды. Но даже если он совсем близко, будут ли рады местные такому количеству гостей?",
            "title": "Упс... Приплыли!",
            "year": 2020,
            "rating": 5
        },
        {
            "trailer": "-----",
            "id": 21,
            "description": "0 из 10!",
            "title": "-------",
            "year": 0,
            "rating": 0
        }
    ]

</details>

### Получить фильм по id

#### Request

`GET /movies/<id>`

    curl --location --request GET 'http://localhost:10001/movies/3'

#### Response

    Status: 200 OK

    {
        "description": "События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...",
        "year": 1978,
        "rating": 6,
        "title": "Вооружен и очень опасен",
        "id": 3,
        "trailer": "https://www.youtube.com/watch?v=hLA5631F-jo"
    }

`GET /genres/`

### Получить список жанров

    curl --location --request GET 'http://localhost:10001/genres/'

#### Response

<details><summary>Список жанров</summary>

    Status: 200 OK

    [
        {
            "name": "Комедия",
            "id": 1
        },
        {
            "name": "Семейный",
            "id": 2
        },
        {
            "name": "Фэнтези",
            "id": 3
        },
        {
            "name": "Драма",
            "id": 4
        },
        {
            "name": "Приключения",
            "id": 5
        },
        {
            "name": "Триллер",
            "id": 6
        },
        {
            "name": "Фантастика",
            "id": 7
        },
        {
            "name": "Аниме",
            "id": 8
        },
        {
            "name": "Документальное",
            "id": 9
        },
        {
            "name": "Короткометражка",
            "id": 10
        },
        {
            "name": "Ужасы",
            "id": 11
        },
        {
            "name": "Боевик",
            "id": 12
        },
        {
            "name": "Мелодрама",
            "id": 13
        },
        {
            "name": "Детектив",
            "id": 14
        },
        {
            "name": "Авторское кино",
            "id": 15
        },
        {
            "name": "Мультфильм",
            "id": 16
        },
        {
            "name": "Вестерн",
            "id": 17
        },
        {
            "name": "Мюзикл",
            "id": 18
        }
    ]

</details>

### Получить жанр по id

#### Request

`GET /genres/<id>`

    curl --location --request GET 'http://localhost:10001/genres/1'

#### Response

    Status: 200 OK

    {
        "name": "Комедия",
        "id": 1
    }

### Получить список режиссеров

`GET /directors/`

    curl --location --request GET 'http://localhost:10001/directors/'

#### Response

<details><summary>Список режиссеров</summary>

    Status: 200 OK

    [
        {
            "name": "Тейлор Шеридан",
            "id": 1
        },
        {
            "name": "Квентин Тарантино",
            "id": 2
        },
        {
            "name": "Владимир Вайншток",
            "id": 3
        },
        {
            "name": "Декстер Флетчер",
            "id": 4
        },
        {
            "name": "Стив Энтин",
            "id": 5
        },
        {
            "name": "Роб Маршалл",
            "id": 6
        },
        {
            "name": "Баз Лурман",
            "id": 7
        },
        {
            "name": "Дэмьен Шазелл",
            "id": 8
        },
        {
            "name": "Пьетро Антон",
            "id": 9
        },
        {
            "name": "Джеймс Мэнголд",
            "id": 10
        },
        {
            "name": "Дени Вильнёв",
            "id": 11
        },
        {
            "name": "Кирилл Серебренников",
            "id": 12
        },
        {
            "name": "Рубен Фляйшер",
            "id": 13
        },
        {
            "name": "Стэнли Кубрик",
            "id": 14
        },
        {
            "name": "Ричард Келли",
            "id": 15
        },
        {
            "name": "Пит Доктер",
            "id": 16
        },
        {
            "name": "Кемп Пауэрс",
            "id": 17
        },
        {
            "name": "Бибо Бержерон",
            "id": 18
        },
        {
            "name": "Тоби Генкель",
            "id": 19
        },
        {
            "name": "Шон Маккормак",
            "id": 20
        }
    ]

</details>

### Получить режиссера по id

#### Request

`GET /directors/<id>`

    curl --location --request GET 'http://localhost:10001/directors/1'

#### Response

    Status: 200 OK
    {
        "name": "Тейлор Шеридан",
        "id": 1
    }

## Представление auth

### Регистрация пользователя

#### Request

`POST http://localhost:10001/auth/register`

    curl --location --request POST 'http://localhost:10001/auth/register' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "email": "type_new_email@gmail.com",
        "password": "You'\''ll_never_guess_it",
        "name": "sample_name",
        "surname": "sample_surname",
        "favorite_genre": "sample_favorite_genre"
    }'

#### Response

    Status: 201 CREATED

### Аутентификация пользователя, получение access и refresh токенов

#### Request

`POST http://localhost:10001/auth/login`

    curl --location --request POST 'http://localhost:10001/auth/login' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "email": "random_email@gmail.com",
        "password": "You'\''ll_never_guess_it"
    }'

#### Response

    Status: 200 OK
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJhbmRvbV9lbWFpbEBnbWFpbC5jb20iLCJwYXNzd29yZCI6IllvdSdsbF9uZXZlcl9ndWVzc19pdCIsImV4cCI6MTY2NDAyMzA2OX0.M0M86UHn5e7VWVxwIU7GIEcjrTUjs4AhSKOhEV0C_NM",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJhbmRvbV9lbWFpbEBnbWFpbC5jb20iLCJwYXNzd29yZCI6IllvdSdsbF9uZXZlcl9ndWVzc19pdCIsImV4cCI6MTY3NTI1NDE2OX0.N0W7vhS-HEi0T6xX4UCkihm-l6xapUiwUQJLB4WPDWM"
    }

### получение новых access и refresh токенов

#### Request

`PUT http://localhost:10001/auth/login`

    curl --location --request PUT 'http://localhost:10001/auth/login' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJhbmRvbV9lbWFpbEBnbWFpbC5jb20iLCJwYXNzd29yZCI6IllvdSdsbF9uZXZlcl9ndWVzc19pdCIsImV4cCI6MTY3NDgxODk2Mn0.kxGG4-O_1IyQtQ7PkS-LokFXsDYuRvBaNqvTpB95n8I"
    }'

#### Response

    Status: 200 OK
    {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJhbmRvbV9lbWFpbEBnbWFpbC5jb20iLCJwYXNzd29yZCI6IllvdSdsbF9uZXZlcl9ndWVzc19pdCIsImV4cCI6MTY2NDAyMzI0OX0.iPsRH40Scz5A_Yp__WSvuydBbZJULMAH-WULSYAGPCw",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJhbmRvbV9lbWFpbEBnbWFpbC5jb20iLCJwYXNzd29yZCI6IllvdSdsbF9uZXZlcl9ndWVzc19pdCIsImV4cCI6MTY3NTI1NDM0OX0.4LyOBwaOAS9-96jGj8r_H4sHbmX0wU_kGV8kNprGCRQ"
    }

## Представление user

### Получение информации о пользователе

#### Request

`GET http://localhost:10001/user/`

    curl --location --request GET 'http://localhost:10001/user/' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjEyMzRkamxramFAZ21haWwuY29tIiwicGFzc3dvcmQiOiJWZXJ5X3N0cm9uZ19wYXNzIiwiZXhwIjoxNjc0ODE1MjEwfQ.722XEvzW8xoDZULciyV5VHXm1-BvUBkBEuH2V7I6VPI' \
    --data-raw ''

#### Response

    Status: 200 OK
    {
        "favorite_genre": "fantastic",
        "id": 1,
        "name": "Artyom",
        "password": "$2a$12$Fwj46L.faR18hNYUvQ4QNeMoFwmde8AVTYsYGniDX/uhFlOTHy5By",
        "surname": "Chirkov",
        "email": "1234djlkja@gmail.com"
    }

### Изменение любимого жанра, имени, фамилии, емейла

#### Request

`PATCH http://localhost:10001/user/`

    curl --location --request PATCH 'http://localhost:10001/user/' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjEyMzRkamxramFAZ21haWwuY29tIiwicGFzc3dvcmQiOiJWZXJ5X3N0cm9uZ19wYXNzIiwiZXhwIjoxNjc0ODE1MjEwfQ.722XEvzW8xoDZULciyV5VHXm1-BvUBkBEuH2V7I6VPI' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "favorite_genre": "fantastic",
        "name": "Artyom",
        "email": "1234djlkja@gmail.com",
        "surname": "Chirkov"
    }'

#### Response

    Status: 204 NO CONTENT

### Изменение пароля

#### Request

`PUT http://localhost:10001/user/password`

    curl --location --request PUT 'http://localhost:10001/user/password' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjEyMzRkamxramFAZ21haWwuY29tIiwicGFzc3dvcmQiOiJWZXJ5X3N0cm9uZ19wYXNzIiwiZXhwIjoxNjc0ODE1MjEwfQ.722XEvzW8xoDZULciyV5VHXm1-BvUBkBEuH2V7I6VPI' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "password_1": "very_strong_pass",
        "password_2": "another_very_strong_pass"
    }'

#### Response

    Status: 204 NO CONTENT
