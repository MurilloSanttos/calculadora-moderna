# Calculadora Moderna em Python

Uma calculadora moderna e completa desenvolvida em Python com interface gráfica responsiva, suporte a operações básicas e científicas, histórico de cálculos, atalhos de teclado e temas personalizáveis.

## Funcionalidades

- **Interface Gráfica Responsiva**: Interface amigável e adaptável a diferentes tamanhos de tela
- **Operações Básicas**: Adição, subtração, multiplicação, divisão, porcentagem
- **Operações Científicas**: Funções trigonométricas, logaritmos, exponenciais, raízes, constantes matemáticas
- **Histórico de Cálculos**: Armazenamento e visualização de cálculos anteriores
- **Atalhos de Teclado**: Suporte completo a atalhos para operações rápidas
- **Temas Claro/Escuro**: Alternância entre temas e personalização completa
- **Estrutura Modular**: Código organizado para fácil manutenção e expansão

## Requisitos

- Python 3.6 ou superior
- Tkinter (geralmente incluído na instalação padrão do Python)

## Instalação

1. Clone o repositório ou baixe os arquivos:
```
git clone https://github.com/MurilloSanttos/calculadora-moderna.git
```

2. Navegue até o diretório do projeto:
```
cd calculadora-moderna
```

3. Execute a aplicação:
```
python src/main.py
```

## Estrutura do Projeto

```
calculadora_moderna/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   └── calculator.py
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── basic_calculator.py
│   │   └── scientific_calculator.py
│   ├── history/
│   │   ├── __init__.py
│   │   ├── history_manager.py
│   │   ├── history_window.py
│   │   └── history_integration.py
│   ├── themes/
│   │   ├── __init__.py
│   │   ├── theme_manager.py
│   │   └── theme_customizer.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── utils.py
│   │   └── keyboard_shortcuts.py
│   ├── __init__.py
│   └── main.py
└── README.md
```

## Uso

### Modos de Operação

A calculadora possui dois modos de operação:

1. **Modo Básico**: Operações matemáticas fundamentais
2. **Modo Científico**: Operações avançadas e funções matemáticas

Para alternar entre os modos, use o menu "Exibir > Modo" ou os atalhos de teclado Ctrl+B (Básico) e Ctrl+S (Científico).

### Histórico de Cálculos

Para acessar o histórico de cálculos:
- Clique no botão "HIST" (modo científico)
- Use o menu "Arquivo > Histórico"
- Pressione Ctrl+H

O histórico permite:
- Visualizar cálculos anteriores
- Reutilizar expressões e resultados
- Salvar o histórico em um arquivo

### Temas

A calculadora suporta:
- Tema Claro (padrão)
- Tema Escuro
- Temas personalizados

Para alternar entre temas:
- Use o menu "Exibir > Tema"
- Pressione Ctrl+T para alternar entre claro e escuro
- Use "Exibir > Personalizar Tema" para criar seu próprio tema

### Atalhos de Teclado

A calculadora suporta diversos atalhos de teclado para operações rápidas:

- **Operações Básicas**: Teclas numéricas, +, -, *, /, =, Enter
- **Funções Científicas**: Ctrl+S (seno), Ctrl+O (cosseno), Ctrl+A (tangente), etc.
- **Interface**: Ctrl+T (alternar tema), Ctrl+H (histórico), F1 (ajuda)

Para ver todos os atalhos disponíveis, acesse "Exibir > Atalhos de Teclado".

## Personalização

### Configurações

As configurações da calculadora são salvas automaticamente, incluindo:
- Último tema utilizado
- Modo de operação (básico ou científico)
- Tamanho do histórico
- Atalhos de teclado personalizados

### Temas Personalizados

Para criar um tema personalizado:
1. Acesse "Exibir > Personalizar Tema"
2. Modifique as cores e fontes conforme desejado
3. Clique em "Aplicar" para visualizar as mudanças
4. Clique em "Salvar" para armazenar o tema personalizado

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## Autor

MurilloSanttos
