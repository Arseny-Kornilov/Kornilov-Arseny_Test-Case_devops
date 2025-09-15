### Инструкция
1. Запустить плейбук: ansible-playbook -i inventory.ini playbook.yml --ask-become-pass

2. Подключиться к Виртуальной машине по ssh и использовать команду: sudo systemctl status metrics-server --> status: active (running)

3. http://localhost:8080 --> вывод соответсвующих метрик 
