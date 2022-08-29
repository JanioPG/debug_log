# Debug Log

Use este script para observar o disparo/acionamento das tags de eventos e screenviews, ajudando você a verificar imediatamente se os eventos estão sendo enviados.
O script apenas habilita o registro detalhado permitindo verificar se os eventos estão sendo registrados corretamente pelo SDK. Isso inclui eventos registrados manual e automaticamente.

## **Dependências**:
* [Python](https://www.python.org/)
* [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb)
    
## **Como utilizar**:
Inicialize seu emulador(Android Studio) ou dispositivo físico conectado, em seguida execute o script Python:

`python debug_log.py` ou `python3 debug_log.py`

Após executar esse script, será pedido que você selecione uma das plataformas. Por exemplo, digite 0 para Firebase, 1 para Universal Analytics, etc.

Obs.: Digite `python debug_log.py -v` para receber mais detalhes ao iniciar a execução do script.

#### Função secundária:
Digite no seu terminal: `python debug_log.py -h`

Nele verá as informações dos argumentos que você pode especificar.
* `python debug_log.py -t1 "termo de busca 1" -t2 "termo de busca 2"`
    
    Exemplo (Firebase): 
    `debug_log.py -t1 select_content -t2 item_name=produto1`
    
    O exemplo acima irá retorar logs que sejam de um evento chamado select_conten e tenha como parâmetro item_name=produto1.
    
    Fique á vontade para realizar o filtro por RegEx também.
    
* `python debug_log.py -t1 "Add\ To\ Cart"`
   Como motrado acima, você também pode buscar por apenas um termo. Nesse exemplo, você receberá o retorno do evento que tiver o valor "Add To Cart" como valor em um dos parâmetros, por exemplo, em action (usado em dual tags).
   Para esse exemplo, você pode ainda buscar por dois ou mais termos, da seguinte forma usando ReGex:
   
   `python debug_log.py -t1 "Add\ To\ Cart|select_content"`
   Nesse exemplo, você receberá como retorno o log contento um evento 'select_content' ou evento que contém "Add To Cart" como valor em um dos parâmetros.

    O mesmo vale para o script relacionado ao Universal Analytics.

### **Comandos utilizados internamente no script**:
Firebase
```
adb shell setprop log.tag.FA-SVC VERBOSE
adb logcat -v time -s FA FA-SVC
```
Universal Analytics
```
adb shell setprop log.tag.GAv4-SVC DEBUG"
adb logcat -s GAv4-SVC"
```

### **Ferramentas sugeridas (Opcional)**:

[asdf](https://asdf-vm.com/guide/getting-started.html) -- Manage multiple runtime versions with a single CLI tool

[tmux](https://github.com/tmux/tmux/wiki) -- is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal.
