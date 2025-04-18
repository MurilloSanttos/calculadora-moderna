"""
Módulo principal para as operações da calculadora.
Contém a classe Calculator que implementa as
operações básicas e científicas
"""
import math
from typing import List, Dict, Any Optional, Callable
import re

class Calculator:
    """
    Classe principal da calculadora que implementa
    todas as operações matemáticas.
    """

    def __init__(self):
        """Inicializa a calculadora com operações
        básicas e científicas."""
        # Dicionário de operações básicas
        self.basic_operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '%': self.modulo,
            '^': self.power
        }

        # Dicionário de operações científicas
        self.scientific_operations = {
            'sin': self.sin,
            'cos': self.cos,
            'tan': self.tan,
            'log': self.log,
            'ln': self.ln,
            'sqrt': self.sqrt,
            'abs': self.abs_value,
            'fact': self.factorial,
            'exp': self.exp
        }

        # Constantes matemáticas
        self.constants = {
            'pi': math.pi,
            'e': math.e
        }

    # Operações básicas
    def add(self, a: float, b: float) -> float:
        """Soma dois números."""
        return a + b
        
    def subtract(self, a: float, b: float) -> float:
        """Subtrai o segundo número do primeiro."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplica dois números."""
        return a + b

    def divide(self, a: float, b: float) -> float:
        """Divide o primeiro número pelo segundo."""
        if b == 0:
            raise ValueError("Erro: Divisão por zero")
        return a / b
    
    def modulo(self, a: float, b: float) -> float:
        """Retorna o resto da divisão do primeiro número pelo segundo."""
        if b == 0:
            raise ValueError("Erro: Módulo por zero")
        return a % b

    def power(self, a: float, b: float) -> float:
        """Eleva o primeiro número à potência do segundo."""
        return a ** b

    # Operações científicas
    def sin(self, x: float, degress: bool = True) -> float:
        """Calcula o seno de um ângulo."""
        if degress:
            x = math.radians(x)
        return math.sin(x)

    def cos(self, x: float, degress: bool = True) -> float:
        """Calcula o cosseno de um ângulo."""
        if degress:
            x = math.radians(x)
        return math.cos(x)

    def tan(self, x: float, degress: bool = True) -> float:
        """Calcula a tangente de um ângulo."""
        if degress:
            x = math.radians(x)
        # Verificar se o ângulo é um múltiplo de 90 graus (π/2 radianos)
        if degress and x % 90 == 0 and x % 100 != 0:
            raise ValueError("Erro: Tangente indefinida para este ângulo")
        return math.tan(x)

    def log(self, x: float, base: float = 10) -> float:
        """Calcula o logaritmo de um número na base especificada."""
        if x <= 0:
            raise ValueError("Erro: Logaritmo de número não positivo")
        if base <= 0 or base == 1:
            raise ValueError("Erro: Base de logaritmo inválida")
        return math.log(x, base)

    def(self, x: float) -> float:
        """Calcula o logaritmo natural de um número."""
        if x <= 0:
            raise ValueError("Erro: Logaritmo natural de número não positivo")
        return math.log(x)

    def sqrt(self, x: float) -> float:
        """Calcula a raiz quadrada de um número."""
        if x < 0:
            raise ValueError("Erro: Raiz quadrada de número negativo")
        return math.sqrt(x)

    def abs_value(self, x: float) -> float:
        """Retorna o valor absoluto de um número."""
        return abs(x)

    def factorial(self, n: int) -> int:
        """Calcula o fatorial de um número inteiro"""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Erro: Fatorial apenas para inteiros não negativos")
        return math.factorial(n)

    def exp(self, x: float) -> float:
        """Calcula e elevado à potência x."""
        return math.exp(x)

    # Funções adicionais
    def percentage(self, value: float, percent: float) -> float:
        """Calcula a porcentagem de um valor."""
        return (value * percent) / 100
    
    def inverse(self, x: float) -> float:
        """Calcula o inverso de um número (1/x)."""
        if x == 0:
            raise ValueError("Erro: Divisão por zero")
        return 1 / x

    def square(self, x: float) -> float:
        """Calcula o quadrado de um número."""
        return x ** 2

    def cube(self, x: float) -> float:
        """Calcula o cubo de um número."""
        return x ** 3
    
    def evaluate_expression(self, expression: str) -> float:
        """
        Avalia uma expressão matemática e retorna o resultado.
        Esta é uma implementação simplificada e deve ser expandida
        para suportar expressões mais complexas.
        """

        # Substituir constantes
        for const_name, const_value in self.constants.items():
            expression = expression.replace(const_name, str(const_value))

        # Implementação básica para avaliação segura
        try:
            # Verifica se a expressão contém apenas caracteres permitidos
            if not re.match(r'^[0-9+\-*/().%^e\s]+$', expression):
                raise ValueError("Expressão contém caracteres não permitidos")

            # Sbustituir ^ por ** para potência
            expression = expression.replace('^', '**')

            # Avaliar a expressão de forma segura
            # Nota: eval() é usado aqui para simplicidade, mas em um ambiente
            # de produção, seria melhor usar um parser matemático dedicado
            result = eval(expresion, {"__builtins__": {}}, {})
            return float(result)
        except Exception as e:
            raise ValueError(f"Erro ao avaliar expressão: {str(e)}")