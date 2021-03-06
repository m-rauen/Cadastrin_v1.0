from entidade.participante import Participante 
from limite.tela_participante import TelaParticipante

class ControladorParticipante: 
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_participante = TelaParticipante()
        self.__participantes = []
        
    @property
    def participantes(self):
        return self.__participantes
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_participante, 2: self.altera_participante, 3: self.exclui_participante, 4: self.lista_um_participante, 5: self.lista_participantes, 0: self.voltar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_participante.tela_opcoes()]()
    
    def pega_participante_codigo(self, codigo: int):
        for participant in self.__participantes:
            if (participant.codigo == codigo):
                return participant
            #return None 
        return None
        
    def inclui_participante(self):
        dados_participante = self.__tela_participante.pega_dados_participante()
        participante = Participante(dados_participante["nome"], dados_participante["cpf"], dados_participante["endereço"], dados_participante["idade"], dados_participante["vacina"], dados_participante["pcr"], dados_participante["codigo"])
        self.__participantes.append(participante)
        #print(self.__participantes[0:])
        
    def exclui_participante(self):
        self.lista_participantes
        if len(self.__participantes) < 1:
            pass
        else:
            codigo_participante = self.__tela_participante.seleciona_participante()
            participante = self.pega_participante_codigo(codigo_participante)
            if participante is not None:
                self.__participantes.remove(participante)
                self.__tela_participante.mostra_mensagem('Participante excluído com sucesso!')
            else:
                self.__tela_participante.mostra_mensagem('Participante inexiste!')
                
    def altera_participante(self):
        self.__tela_participante.mostra_mensagem('* ALTERANDO PARTICIPANTE *')
        if len(self.__participantes) < 1: 
            pass
        else: 
            codigo_participante = self.__tela_participante.seleciona_participante()
            participante = self.pega_participante_codigo(codigo_participante)
            if participante is not None:
                novo_participante = self.__tela_participante.pega_dados_participante()
                participante.nome = novo_participante["nome"]
                participante.cpf = novo_participante["cpf"]
                participante.endereço = novo_participante["endereço"]
                participante.idade = novo_participante["idade"]
                participante.vacina_3d = novo_participante["vacina"]
                participante.exame_pcr = novo_participante["pcr"]
                participante.codigo = novo_participante["codigo"]
                self.lista_participantes()
            else: 
                self.__tela_participante.mostra_mensagem('Participante inexistente!')
            
    def lista_um_participante(self):
        if len(self.__participantes) < 1: 
            self.__tela_participante.mostra_mensagem('Não foram cadastrados participantes até o momento!')
        else:
            codigo_participante = self.__tela_participante.seleciona_participante() 
            participante = self.pega_participante_codigo(codigo_participante)
            if participante is not None: 
                self.__tela_participante.mostra_participante({"nome": participante.nome, "cpf": participante.cpf, "endereço": participante.endereço, "idade": participante.idade, "vacina": participante.vacina_3d, "pcr": participante.exame_pcr, "codigo": participante.codigo})
            else:
                self.__tela_participante.mostra_mensagem('Participante inexistente!')
                
    def lista_participantes(self):
        if len(self.__participantes) < 1: 
            self.__tela_participante.mostra_mensagem('Não foram cadastrados participantes até o momento!')
        else: 
            for participante in self.__participantes:
                 self.__tela_participante.mostra_participante({"nome": participante.nome, "cpf": participante.cpf, "endereço": participante.endereço, "idade": participante.idade, "vacina": participante.vacina_3d, "pcr": participante.exame_pcr, "codigo": participante.codigo})
                
    def voltar(self):
        self.__controlador_sistema.abre_tela()
        
    
            