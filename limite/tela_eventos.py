from limite.tela import Tela 

class TelaEventos:
    def trata_opçoes(self, msg: str = '', inteiros_validos = []):
        valor = input(msg)
        try:
            inteiro = int(valor)
            if inteiros_validos and inteiro not in inteiros_validos:
                raise ValueError
            return inteiro
        except ValueError:
            print('Valor inválido!!\n'
                  'Por favor, digite novamente.')
            if inteiros_validos:
                print('Valores aceitos: {}'.format(inteiros_validos))
            
    def tela_opçoes(self):
        print('-'*15)
        print('E V E N T O S')
        print('-'*15)
        print('(1) - Adicionar evento \n'
              '(2) - Alterar dados do evento \n'
              '(3) - Excluir evento \n'
              '(4) - Listar evento selecionado \n'
              '(5) - Listar todos os eventos \n '
              '(0) - Voltar')
        opçao = self.trata_opçoes('Digite a opção: ', [1,2,3,4,5,0])    
        return opçao
    
    def pega_dados_evento(self, lista_eventos = []):
        print('* DADOS DO EVENTO * \n')
        codigos = []
        
        for event in lista_eventos:
            codigos.append(event.codigo)
            
        while True:
            nome = input('Nome: ').capitalize()
            try:
                if nome.isascii() == False or nome.isnumeric == True:
                    raise ValueError
                if len(nome) < 1:
                    raise ValueError
                break
            except ValueError:
                print('Digite um nome válido!! \n'
                      'O nome deve ter, no mínimo, 1 caracter; \n'
                      'O nome não pode ser composto SOMENTE por números')
                
            while True:
                codigo = input('Código: ')
                try:
                    if codigo.isnumeric == False:
                        raise ValueError
                    if int(codigo) in codigos:
                        raise Exception 
                    break 
                except ValueError:
                    print('Digite um código válido!! \n'
                          'Os códigos devem conter SOMENTE números')
                except Exception:
                    print('Esse código já foi cadastrado!')
                    
            while True:
                lotacao_max  = input('Lotação máxima: ')
                try:
                    if lotacao_max .isnumeric == False:
                        raise ValueError
                    break
                except ValueError:
                    print('Digita uma lotação válida!! \n'
                          'As lotações máximas devem ser SOMENTE o número máximo que a casa permite')
                    
            while True:
                faixa_etaria = input('Faixa etária mínima: ')
                try:
                    if faixa_etaria.isnumeric == False:
                        raise ValueError
                    break
                except ValueError:
                    print('Digite uma faixa etária válida!! \n'
                            'A faixa etária deve ser SOMENTE a idade mínima para entrar') 
            
            while True:
                open_bar = input('Open bar (S/N): ').upper()
                try: 
                    if open_bar.isnumeric == True:
                        raise ValueError
                    break
                except ValueError:
                    print('Digite uma resposta válida!! \n'
                          "A opção correspondente deve ser 'S' (sim) ou 'N' (não)")
                    
            return {"nome":nome, "codigo":codigo, "lotacao_max":lotacao_max , "faixa_etaria":faixa_etaria, "open_bar":open_bar}
        
    def mostra_evento(self, dados_evento):
        print('#' *35)
        print('DADOS DO EVENTO:')
        print('Nome: {}'.format(dados_evento['nome']))
        print('Código: {}'.format(dados_evento['codigo']))
        print('Lotação Máxima: {}'.format(dados_evento['lotacao_max']))
        print('Faixa Etária: {}'.format(dados_evento['faixa_etaria']))
        print('Open bar: {}'.format(dados_evento['open_bar'])) 
    
    def seleciona_evento(self):
        while True:
            codigo = input('Código - Evento: ')
            # try: 
            #     if codigo.isnumeric() == False: 
            #         raise ValueError
            #     return int(codigo)
            # except ValueError:
            #     print('Digite um valor válido!! \n')
            #     'Os códigos devem conter SOMENTE números'
            return codigo 
        
    def pega_evento_codigo(self):
        codigo = input('Código do evento: ')
        try:
            if codigo.isnumeric() == False: 
                raise ValueError
        except ValueError:
            print('Digite um código válido!! \n'
                      'Os códigos devem conter SOMENTE números')
                
    def mostra_mensagem(self, msg: str):
        print(msg)
                
    
            
        
    
    