from abc import ABCMeta, abstractmethod

class Template_Imposto_Condicional(object):
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_taxacao_max(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_taxacao_max(self, orcamento): pass
    @abstractmethod
    def maxima_taxacao(self, orcamento): pass
    @abstractmethod
    def maxima_taxacao(self, orcamento): pass


class ISS(object):
	def calcula(self, orcamento):
		return orcamento.valor * 0.1


class ICMS(object):
	def calcula(self, orcamento):
		return orcamento.valor * 0.06


class ICPP(Template_Imposto_Condicional):
    def deve_usar_taxacao_max(self, orcamento): 
        return orcamento.valor > 500
 
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento): 
        return orcamento.valor * 0.05


class IKCV(Template_Imposto_Condicional):
    def _tem_item_maior_que_100(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

    def deve_usar_taxacao_max(self, orcamento): 
        return orcamento.valor > 500 and self._tem_item_maior_que_100(orcamento)
 
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento): 
        return orcamento.valor * 0.06
