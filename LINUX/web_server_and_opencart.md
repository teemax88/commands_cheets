♀## Шаг 1. Обновите операционную систему
```commandline
sudo apt update && sudo apt upgrade -y
```

## Шаг 2. Установите веб-сервер Apache.
```commandline
sudo apt install apache2
```

*Выполнив следующие команды, вы можете запустить службу Apache и настроить ее на немедленный запуск при запуске:*
```commandline
sudo systemctl start apache2
sudo systemctl enable apache2
```

*Используйте systemctl statusкоманду, чтобы проверить Apacheстатус службы:*
```commandline
sudo systemctl status apache2
```

## Шаг 3. Установите PHP
```commandline
sudo apt-get install php php-cli libapache2-mod-php php-common php-mbstring php-gd php-intl php-xml php-mysql php-zip php-curl php-xmlrpc
```

*Проверьте, настроен ли PHP.*
```commandline
php -v
```

## Шаг 4. Установите MariaDB и создайте базу данных.
```commandline
sudo apt install mariadb-server mariadb-client
```

*Используйте systemctl statusкоманду, чтобы проверить MariaDBстатус службы:*
```commandline
sudo systemctl status mariadb
```

*По умолчанию MariaDB не защищена. С помощью mysql_secure_installationскрипта вы можете защитить MariaDB.*
```commandline
sudo mysql_secure_installation
```

*Настройте его следующим образом:*
```commandline
- Set root password? [Y/n] Y
- Remove anonymous users? [Y/n] Y
- Disallow root login remotely? [Y/n] Y
- Remove test database and access to it? [Y/n] Y
- Reload privilege tables now? [Y/n] Y
```

*Чтобы получить доступ к оболочке MariaDB, выполните команду ниже.*
```commandline
sudo mysql -u root -p
```

*Вы должны создать базу данных для установки OpenCart после входа на сервер базы данных:*
```commandline
MariaDB [(none)]> CREATE DATABASE opencart;
MariaDB [(none)]> CREATE USER 'opencart'@'localhost' IDENTIFIED BY 'Your-Strong-Password';
MariaDB [(none)]> GRANT ALL PRIVILEGES ON opencart . * TO 'opencart'@'localhost';
MariaDB [(none)]> FLUSH PRIVILEGES;
MariaDB [(none)]> exit;
```

## Шаг 5: Загрузите OpenCart
```commandline
sudo wget https://github.com/opencart/opencart/releases/download/4.0.0.0/opencart-4.0.0.0.zip
```

*Затем извлеките файл в /var/www/html/opencart/папку с помощью команды:*
```commandline
sudo apt -y install unzip 
sudo unzip opencart-4.0.0.0.zip -d /var/www/html/opencart/
```

*Скопируйте файлы конфигурации для OpenCart:*
```commandline
sudo cp /var/www/html/opencart/upload/{config-dist.php,config.php}

sudo cp /var/www/html/opencart/upload/admin/{config-dist.php,config.php}
```

*Предоставьте пользователю веб-сервера Apache доступ к файлам, включив это разрешение:*
```commandline
sudo chown -R www-data:www-data /var/www/html/opencart/
```

## Шаг 6. Создайте виртуальный хост для Opencart
*Затем создайте файл конфигурации виртуального хоста OpenCart:*
```commandline
sudo nano /etc/apache2/sites-available/opencart.conf
```

*Скопируйте и вставьте текст следующим образом:*
```commandline
<VirtualHost *:80>
    ServerAdmin admin@your-domain.com
    DocumentRoot /var/www/html/opencart/upload/
    ServerName your-domain.com
    ServerAlias www.your-domain.com

    <Directory /var/www/html/opencart/upload/>
        Options FollowSymLinks
        AllowOverride All
        Order allow,deny
        Allow from all
    </Directory>

    ErrorLog /var/log/apache2/your-domain.com-error_log
    CustomLog /var/log/apache2/your-domain.com-access_log common
</VirtualHost>
```

*Запустите следующую команду, чтобы включить этот сайт и отключить конфигурацию по умолчанию:*
```commandline
sudo a2ensite opencart.conf
sudo a2dissite 000-default
```

*Перезапустите веб-сервер Apache, чтобы применить изменения:*
```commandline
sudo systemctl restart apache2
```

## Шаг 7. Доступ к веб-интерфейсу OpenCart
*Откройте http://your-domain.com/веб-интерфейс OpenCart в браузере.*
```text
Лицензионное соглашение показано на первой странице. Нажмите «Продолжить» после прокрутки вниз.
```

```text
Прежде чем нажать кнопку «Продолжить» , убедитесь, что установлены все необходимые расширения PHP.
```

```text
Вы должны заполнить данные базы данных на следующей странице. Нажмите «Продолжить» после ввода информации, которую вы определили в базе данных MariaDB.
```

*Откройте терминал сейчас и используйте следующую команду, чтобы удалить каталог установки:*
```commandline
sudo rm -rf /var/www/html/opencart/upload/install/
```

## Проброс портов для SSH
После установки серверного дистрибутива Linux на виртуальную машину VirtualBox вы можете обнаружить, что подключение по SSH не работает. Это связано с тем, что по умолчанию на VirtualBox используется подключение к интернету с помощью NAT.

*Выполните команду, чтобы увидеть информацию о сетевых подключениях*
```commandline
ifconfig
```

*В настройках виртуальной машины нужно открыть раздел «Сеть», открыть дополнительные настройки и перейти к пробросу портов.*

*После этого откроется окно для проброса портов. Здесь нужно нажать на кнопку «Добавить» и заполнить следующие данные:*
```text
Имя: SSH.
Протокол: TCP.
Адрес хоста: оставляем пустым или указываем 127.0.0.1.
Порт хоста: любой свободный порт на вашей основной системе, например, 2222.
Адрес гостя: IP адрес, который был присвоен вашей виртуальной машине. В нашем случае это 10.0.2.15.
Порт гостя: порт SSH на виртуальной машине, по умолчанию – 22.
```

*Установить SSH- сервер на виртуальной машине*
```commandline
sudo apt-get install openssh-server
```

*Для подключения по SSH нужно выполнить следующую команду*
```commandline
ssh user@localhost -p 2222
```