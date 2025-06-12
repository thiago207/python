class MeuArquivo:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        #print('Abrindo')
        self._arquivo = open(self.caminho, self.modo, encoding='utf-8')
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        self._arquivo.close()
        #print('FECHANDO')

class ArquivoSeguro(MeuArquivo):
    def __init__(self, caminho, modo, usuario):
        super().__init__(caminho, modo)
        self._arquivo = None
        self.usuario = usuario

    def __repr__(self):
       return f'{self.caminho!r} - {self.modo!r} - {self.usuario!r} - {self._arquivo!r}'
    

    def __enter__(self):
        print('Abrindo')
        if self.usuario == 'admin':
            self._arquivo = open(self.caminho, self.modo, encoding='utf-8')
        else:
            raise PermissionError("Usuário sem permissão para abrir o arquivo.")
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        if self.usuario== 'admin':
            self._arquivo.close()
        #print('FECHANDO')


with MeuArquivo('EX-42', 'w') as arquivo:
    #print('Escrevendo no arquivo...')
    arquivo.write('OPA')


arquivo_seguro = ArquivoSeguro('arq-seguro', 'w', usuario='admin')

with arquivo_seguro as arquivo:
    arquivo.write('ola, adm')