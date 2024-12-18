# Shell Emulator

## Описание

Shell Emulator — это эмулятор командной оболочки для UNIX-подобных операционных систем, написанный на Python. Он позволяет пользователям взаимодействовать с виртуальной файловой системой, загруженной из ZIP-архива, и поддерживает основные команды, такие как `ls`, `cd`, `exit`, `chown`, `head` и `cp`. Все действия записываются в лог-файл в формате XML.

## Установка

### Требования

- Python 3.6 или выше
- Библиотеки: `toml`, `xml.etree.ElementTree` (входит в стандартную библиотеку Python)

### Установка зависимостей

Убедитесь, что у вас установлен Python и pip. Затем выполните следующую команду для установки необходимых библиотек:

```bash
pip install toml
```

Создайте файл config.toml в корневом каталоге проекта с содержимым:

```bash
vfs_path = "path/to/your/vfs.zip"
log_file = "log.xml"
vfs_path: Путь к ZIP-архиву, содержащему виртуальную файловую систему.
log_file: Путь к файлу, в который будут записываться логи.

```

### Запуск эмулятора
Для запуска эмулятора выполните следующую команду в терминале:

```bash
python emulator.py config.toml
```

## Доступные команды

ls: Выводит список файлов и директорий в текущей директории.
cd <directory>: Изменяет текущую директорию на указанную.
exit: Завершает работу эмулятора и записывает лог.
chown <owner> <filename>: Изменяет владельца указанного файла (пока что это заглушка).
head <filename>: Выводит первые 10 строк указанного файла.
cp <source> <destination>: Копирует файл из источника в назначение.
Логирование
Все действия, выполненные в эмуляторе, записываются в лог-файл в формате XML, указанный в конфигурационном файле.

### Тестирование
Для запуска тестов используйте unittest. Убедитесь, что у вас есть тестовые данные, и выполните следующую команду:

```bash
python -m unittest discover -s tests
```

## Результаты тестов

Все тесты были успешно выполнены. Ниже приведены результаты тестирования для каждой команды:

<img width="440" alt="image" src="https://github.com/user-attachments/assets/983881d4-2884-4cee-ba61-9a72bc2f76c7" />

## Тесты команд

### Код Теста

```python
    def test_ls(self):
        self.emulator.ls()

    def test_cd(self):
        self.emulator.cd('some_directory')

    def test_exit(self):
        with self.assertRaises(SystemExit):
            self.emulator.exit()

    def test_chown(self):
        self.emulator.chown('new_owner', 'file.txt')

    def test_head(self):
        self.emulator.head('file.txt')

    def test_cp(self):
        self.emulator.cp('source.txt', 'destination.txt')
```

# Пример Использования
## Запуск эмулятора:
```python
python shell_emulator.py test_config.ini
```

## Использование команд

### 1. Использование команды ls:
<img width="131" alt="image" src="https://github.com/user-attachments/assets/8d2e52bd-1e5e-4b8d-86bd-5c2174bc4453" />

### 2. Использование команды cd:
<img width="178" alt="image" src="https://github.com/user-attachments/assets/e6d610b5-8e19-4722-ad3f-eb36820c5754" />

### 3. Использование команды head:
<img width="243" alt="image" src="https://github.com/user-attachments/assets/069f5872-6573-418b-9ef0-4b1c7c2dece1" />

### 4. Использование команды chown:
<img width="347" alt="image" src="https://github.com/user-attachments/assets/e44a5196-59b4-4523-8e41-5f247877fea1" />

### 5. Использование команды cp:
<img width="317" alt="image" src="https://github.com/user-attachments/assets/611fe67d-f46e-416e-ad37-0dd888687414" />


### Общая информация

Все тесты прошли успешно, что подтверждает корректность работы эмулятора и его команд. Рекомендуется периодически запускать тесты после внесения изменений в код для обеспечения стабильности и функциональности.

## Примечания

Убедитесь, что ZIP-архив с виртуальной файловой системой существует и доступен по указанному пути.
Эмулятор работает в режиме CLI и не требует распаковки ZIP-архива пользователем.
