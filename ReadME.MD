<!DOCTYPE html>
<html>
  <body>
    <img align="right" alt="Coding" width="350" src="https://user-images.githubusercontent.com/113009998/233772381-b051a566-85af-4f28-a6e1-5aa209f37318.png">
    <h1>EvoSoft Task</h1>
    <p>Данное задание направлено на создание скрипта на Python для парсинга данных с веб-сайта NSE India, используя библиотеку Selenium. Алгоритм включает в себя переход по различным разделам сайта, сбор информации о ценах, сохранение данных в CSV файл, а также симуляцию пользовательского взаимодействия с веб-сайтом. Дополнительно, задача включает парсинг последних твитов Илона Маска, без использования официального API Twitter, вывод текста твитов и ссылок на авторов последних трех комментариев к каждому твиту.</p>
    <h2>Содержание</h2>
    <ul>
      <li><a href="#install_p">Установка проекта</a></li>
      <li><a href="#install_v">Установка виртуального окружения</a></li>
      <li><a href="#install_r">Установка дополниткльных библиотек</a></li>
      <li><a href="#config">Содерживое config.py</a></li>
    </ul>
    <h1 id="install_p">Установка проекта</h1>
    <p>Для установки данного проекта вам потребуется скачать Git на ваш локальный компьютер и выполнить следующую команду
    <pre><code>git clone https://github.com/Peskovatskow-Ignat/EvoSoft </code></pre> <p>А так же можно просто скачать zip архив</p>
    <h1 id="install_v">Установка виртуального окружения</h1>
    <p>Для работы с нашим скриптом мы должны установить дополнительные библиотеки, все они указаны в файле <code>requirements.txt</code></p> Для начала мы установим виртуальное окружение если его нету, для перейдём в директорию прокта  и выполним команду <pre><code>python -m venv venv</code></pre>
    Активировация venv
    <p>Windows</p>
    <pre><code>.\venv\Scripts\activate</code></pre>
    <p>Linux</p>
    <pre><code>source venv\bin\activate</code></pre>
    <h1 id="install_r">Установка дополниткльных библиотек</h1>
    <p>Все дополнительные библиотеки возьмём из файла <code>requirements.txt</code></p>
    <pre><code>pip install -r requirements.txt</code></pre>
    <h1 id="config">Содерживое config.py</h1>
    <p>Так же для конфиденциальности я использовал файл <code>config.py</code> так как в файт <code>.env</code> нет возможности записать словарь. Этот файл должен находиться в папке Task2</p>
    <pre><code>cookies_post = {
cookies с профиля пользователя
}


cookies_link = {
        cookies с url поста
    }

proxies = {"https": "http://35.185.196.38:3128"}

headers_link = {
        headers с url поста
    }
headers_post = {
    headers с профиля пользователя
}
</code></pre>
