# -*- coding: utf-8 -*-

"""
Algoritmo guloso de agendamento de intervalos

Autor:

Colaborador:
	Pedro Arthur Duarte (JEdi)
	pedroarthur.jedi@gmail.com

Tipo:
	Interval Scheduling
	Greed Algorithms
	Optimization

Descrição:
	Dado um conjunto de tarefas expressos como t = (s,e), onde 's' especifica
	o inicio da tarefa e 'e' o seu fim, determinar o subconjunto máximo de
	tarefas que não se sobrepõem.

	Uma das maneiras de determinar esse subconjunto consiste em selecionar
	gulosamente as tarefas com base no seu horário de término: as tarefas com
	término mais cedo que não se sobrepõem são selecionadas para formar o
	subconjunto de saída.

Complexidade:
	O(n), para um conjunto de tarefas ordenadas;

	O(n) + O(g(n)), para um conjunto de tarefas não ordenadas, onde 'g' é
                    uma função de ordenação.

Dificuldade:
	Fácil

Referências:
	Kleinberg, Jon; Tardos, Eva (2006). Algorithm Design.
	ISBN 0-321-29535-8

Licença:
	GPLv3

"""

def intervalScheduling(tasks):
	# Cópia a lista de tarefas e a ordena. O método "sort" das listas Python
	# é local. Portanto, caso seja necessário a lista original, não devemos
	# chamá-lo sem antes cloná-la.
	tasks = tasks[:]
	tasks.sort()

	# A tarefa com termino mais cedo sempre é a primeira do subconjunto
	# de saída
	scheduling = [ tasks[0] ]

	# Agora, para todos os outros elementos da lista ordenada de tarefas, nós
	# verificamos se esse elemento é compatível com as tarefas já presentes
	# no subconjunto de saída. Para uma lista ordenada, essa operação é O(1)
	# pois necessita apenas acessar a última tarefa inserida.
	for t in tasks[1:]:
		# Se o momento de inicio da tarefa é maior ou igual ao fim da última
		# tarefa do subconjunto de saída, ela é compatível.
		if t.start >= scheduling[-1].end:
			# E, logo, nós a inserimos no subconjunto de saída
			scheduling.append(t)

	# Por último, retornamos a lista
	return scheduling

# Conjunto de tarefas de exemplo
#  --- ---- --------
# ---- --- - --- ----
#  ----  -- -- --- --
#   ---- --- ---- ---

class Task:
	'''
	Abstração das tarefas
	'''
	start = 0
	end = 0

	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __repr__(self):
		return '''<Task %s:%s>''' % (self.start, self.end)

	def __cmp__(self, o):
		if self.end < o.end:
			return -1

		if self.end == o.end:
			if self.start < o.start:
				return -1
			elif self.start > o. start:
				return 0
			else:
				return 1

		return 1

# Em formato de lista
tasks = [ Task(40, 70), Task(80, 120), Task(130, 210),
 Task(30, 70), Task(80, 110), Task(120, 130), Task(140, 170), Task(180, 220),
 Task(40, 80), Task(100, 120), Task(130, 150), Task(160, 190), Task(200, 220),
 Task(50, 90), Task(100, 130), Task(140, 180), Task(190, 220) ]

print intervalScheduling(tasks)
