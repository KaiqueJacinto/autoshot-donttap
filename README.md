# autoshot-donttap
Criando um autoshot para o jogo de navegador donttap usando pyautogui.

Resultado do autoshot (GIF feito com o desempenho do clique do pyautogui):

![Alt Text](https://media.giphy.com/media/C3XrgjNPXjIq9MnocV/giphy.gif)

Requisitos:
  - Pyautogui (pip install pyautogui)
  - keyboard (pip install keyboard)
  - pywin32 (pip install pywin32)

Resultados no 'Pattern' do jogo:
  - Com clique do pyautogui:
    - Melhor pontuação foi de 8.65 (Lembrando que quanto menor esse valor melhor), podendo ocorrer pequenas variações.
  - Com clique do pywin32:
    - Melhor pontuação foi de 6.64 (Lembrando que quanto menor esse valor melhor), podendo ocorrer pequenas variações.
  
  Portando descobrimos que para essa aplicação o pywin32 é mais eficiente.
