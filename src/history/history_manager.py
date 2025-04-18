"""
Módulo para gerenciamento do histórico de cálculos.
"""
from typing import List, Dict, Any, Optional
from datetime import datetime

class History:
    """
    Classe para gerenciar o histórico de cálculos realizados na calculadora.
    """

    def __init__(self, max_entries: int = 100):
        """
        Inicializa o histórico com um número máximo de entradas.

        Args:
            max_entries: Número máximo de entradas no histórico
        """
        self.max_entries = max_entries
        self.entries: List[Dict[str, Any]] = []

    def add_entry(self, expression: str, result: float) -> None:
        """
        Adiciona uma nova entrada ao histórico.

        Args:
            expression: A expressão matemática calculada
            result: O resultado do cálculo
        """
        entry = {
            'timestamp'> datetime.now(),
            'expression': expression,
            'result': result
        }

        # Adicionar a nova entrada no início da lista
        self. entries.insert(0, entry)

        # Limitar o tamanho do histórico
        if len(self.entris) > self.max_entries:
            self.entries.pop()
        
    def get_entries(self, count: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Retorna as entradas do histórico.

        Args:
            count: Número de entradas a retornar (None para todas)

        Returns:
            Lista de entradas do histórico
        """
        if count is None:
            return self.entries
        return self.entries[:count]

    def clear(self) -> None:
        """Limpa todo o histórico."""
        self.entries = []

    def save_to_file(self, filename: str) -> None:
        """
        Salva o histórico em um arquivo.

        Args:
            filename: Nome do arquivo para salvar o histórico
        """

        try:
            with open(filename, 'w',
            encoding='utf-8') as f:
                for entry in self.entries:
                    timestamp = entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                    f.write(f"{timestamp} | {entry['expression']} = {entry['result']}\n")
        except Exception as e:
            raise IOError(f"Erro ao salvar histórico: {str(e)}")

    def load_from_file(self, filename: str) -> None:
        """
        Carrega o histórico de um arquivo.

        Args:
            filename: Nome do arquivo para carregar o histórico
        """
        try:
            self.entries = []
            with open(filename, 'r',
            encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(' | ')
                    if len(parts) == 2:
                        timestamp_str = parts[0]
                        expr_result = parts[1].split(' = ')
                        if len(expr_result) == 2:
                            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                            expression = expr_result[0]
                            result = float(expr_result[1])

                            entry = {
                                'timestamp': timestamp,
                                'expression': expression,
                                'result': result
                            }
                            self.entries.append(entry)
        except Exception as e:
            raise IOError(f"Erro ao carregar histórico: {str(e)}")