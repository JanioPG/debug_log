# Debug Log

Use este script para observar o disparo/acionamento das tags de eventos e screenviews, ajudando você a verificar imediatamente se os eventos estão sendo enviados.
O script apenas habilita o log detalhado para monitorar o log de eventos pelo SDK para ajudar a verificar se os eventos estão sendo registrados corretamente. Isso inclui eventos registrados automaticamente e manualmente.

## **Dependências**:
* [Python](https://www.python.org/)
* [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb)
    
## **Como utilizar**:
Inicialize seu emulador(Android Studio) ou dispositivo físico conectado, em seguida execute os scripts Python:
`python <nome do arquivo>.py`
ou
`python3 <nome do arquivo>.py`

## **Comandos utilizados internamento no script**:
```
adb shell setprop log.tag.FA-SVC VERBOSE
adb logcat -v time -s FA FA-SVC
```
    

### **Ferramentas sugeridas (Opcional)**:
[asdf](https://asdf-vm.com/guide/getting-started.html) -- Manage multiple runtime versions with a single CLI tool
[tmux](https://github.com/tmux/tmux/wiki) -- is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal.
