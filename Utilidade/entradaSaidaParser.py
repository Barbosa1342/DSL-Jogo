import json
import abc
import os

class ResetFile(abc.ABC):
    @abc.abstractmethod
    def resetar(self, path):
        pass

class InputParser(abc.ABC):
    @abc.abstractmethod
    def ler_entrada(self, path):
        pass

class OutputParser(abc.ABC):
    @abc.abstractmethod
    def salvar_saida(self, path, new_data):
        pass

class JsonResetFile(ResetFile):
    def resetar(self, path):
        with open(path, 'w') as file:
            json.dump([], file, indent=4)

class TextoInputParser(InputParser):
    def ler_entrada(self, path):
        try:
            with open(path, 'r') as file:
                return file.read()
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return ""

class JsonInputParser(InputParser):
    def ler_entrada(self, path):
        if os.path.getsize(path) == 0:
            return []

        try:
            with open(path, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Erro ao ler o arquivo JSON: {e}")
            return []

class JsonOutputParser(OutputParser):
    def salvar_saida(self, path, new_data):
        data = JsonInputParser().ler_entrada(path)
        
        if isinstance(data, Exception):
            print(f"Erro ao ler o arquivo JSON")
            return
        elif (data is None) or (not isinstance(data, list)):
            data = []
        
        data.append(new_data)

        with open (path, 'w') as file:
            json.dump(data, file, indent=4)