# Построение L-систем

Пример простого приложения на PyQt для рисования L-систем.

![./screenshot.png](Screenshot)

## Начало работы

Установка Python 3.7+: https://python.org/

Установка все необходимые зависимости:
```shell script
pip install -r requirements.txt
```

Для работы с дизайнером рекомендуется также установить pyqt5-tools:
```shell script
pip install pyqt5-tools
```

## Запуск приложения

```shell script
python main.py
```

## Сборка UI файлов

Для компиляции ui файлов требуется pyuic5. Готовая команда компиляции в `build_ui.cmd`.

## Структура проекта
```
├───core            # Основные компоненты приложения
│       lsystem.py  # Класс L-системы
├───samples         # Примеры L-систем
├───ui              # Компоненты интерфейса
│   ├───built       # Скомпилированные ui файлы
│   ├───src         # Исходные ui файлы дизайнера
│   ├───views       # Представления, формы приложения
│   └───widgets     # Вспомогательные виджеты
│   .gitignore      
│   build_ui.cmd    # Скрипт компиляции UI файлов
│   main.py         # Основной файл
│   README.md 
│   requirements.txt
```

## Contribution

Coming soon
