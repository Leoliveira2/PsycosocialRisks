#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def criar_questao_radio(num, nome_campo, titulo, opcoes):
    """Cria uma questão com radio buttons de forma compacta"""
    html = f'''        <div class="question-group">
          <label class="question-title">{num}. {titulo}</label>
          <div class="radio-group">
'''
    for valor, texto in opcoes:
        html += f'            <label class="radio-option"><input type="radio" name="{nome_campo}" value="{valor}" onchange="updateProgress()"><span class="radio-text">{texto}</span></label>\n'
    
    html += '          </div>\n        </div>\n\n'
    return html

# Ler arquivo original
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar posição de inserção (antes de </main>)
insert_marker = '      <!-- Dashboard de Resultados -->'
parts = content.split(insert_marker)

if len(parts) != 2:
    print("ERRO: Marcador não encontrado!")
    exit(1)

# Criar todos os questionários novos
novos_questionarios = ""

# ============= COPSOQ COMPLETA =============
novos_questionarios += '''
      <!-- COPSOQ III Short - Versão Completa -->
      <div id="copsoq-completa" class="questionario card">
        <h2>🧠 COPSOQ III Short - Avaliação Completa</h2>
        <p class="questionnaire-info">20 questões abrangentes baseadas no questionário oficial internacional</p>
        
'''

opcoes_freq = [(4, "Sempre"), (3, "Frequentemente"), (2, "Às vezes"), (1, "Raramente"), (0, "Nunca")]
opcoes_medida = [(4, "Em grande medida"), (3, "Em boa medida"), (2, "De alguma forma"), (1, "Em pequena medida"), (0, "Muito pouco")]

questoes_copsoq_completa = [
    ("copsoq_c_q1", "Com que frequência você não tem tempo suficiente para completar todas as suas tarefas de trabalho?", opcoes_freq),
    ("copsoq_c_q2", "Você tem um alto grau de influência nas decisões relacionadas ao seu trabalho?", opcoes_medida),
    ("copsoq_c_q3", "Com que frequência você recebe ajuda e apoio do seu supervisor imediato, quando necessário?", opcoes_freq),
    ("copsoq_c_q4", "Com que frequência você recebe ajuda e apoio dos seus colegas, quando necessário?", opcoes_freq),
    ("copsoq_c_q5", "Seu trabalho é significativo para você?", opcoes_medida),
    ("copsoq_c_q6", "Com que frequência você tem que trabalhar muito rápido?", opcoes_freq),
    ("copsoq_c_q7", "Você pode influenciar a quantidade de trabalho que lhe é atribuída?", opcoes_medida),
    ("copsoq_c_q8", "Você pode usar suas habilidades ou conhecimentos no trabalho?", opcoes_medida),
    ("copsoq_c_q9", "Seu trabalho exige que você aprenda coisas novas?", opcoes_medida),
    ("copsoq_c_q10", "Você sente que seu trabalho é emocionalmente exigente?", opcoes_freq),
    ("copsoq_c_q11", "Você tem que esconder seus sentimentos no trabalho?", opcoes_freq),
    ("copsoq_c_q12", "Você recebe reconhecimento pelo seu trabalho?", opcoes_freq),
    ("copsoq_c_q13", "Você é tratado de forma justa no seu local de trabalho?", opcoes_freq),
    ("copsoq_c_q14", "Você confia no seu supervisor imediato?", opcoes_medida),
    ("copsoq_c_q15", "Você confia nos seus colegas de trabalho?", opcoes_medida),
    ("copsoq_c_q16", "Você sente que seu trabalho tem um propósito importante?", opcoes_medida),
    ("copsoq_c_q17", "Você sente que pertence ao seu local de trabalho?", opcoes_medida),
    ("copsoq_c_q18", "Você se preocupa com problemas do trabalho quando não está trabalhando?", opcoes_freq),
    ("copsoq_c_q19", "Você se sente exausto emocionalmente após um dia de trabalho?", opcoes_freq),
    ("copsoq_c_q20", "Você se sente fisicamente exausto após um dia de trabalho?", opcoes_freq),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_copsoq_completa, 1):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''        <button class="btn" onclick="calcularResultados('copsoq-completa')">Calcular Resultados</button>
      </div>

'''

# ============= HSE COMPLETA =============
novos_questionarios += '''      <!-- HSE Indicator Tool - Versão Completa -->
      <div id="hse-completa" class="questionario card">
        <h2>📊 HSE Indicator Tool - Avaliação Completa</h2>
        <p class="questionnaire-info">35 questões abrangentes cobrindo todos os 7 domínios do questionário oficial britânico</p>
        
        <h3 style="color: #2196f3; margin-top: 20px;">Domínio 1: Demandas (8 questões)</h3>
'''

# Simplificar HSE completa - 35 questões
questoes_hse = [
    ("hse_c_q1", "Eu tenho prazos irreais para cumprir", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("hse_c_q2", "Eu tenho que trabalhar muito intensamente", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("hse_c_q3", "Eu tenho que negligenciar algumas tarefas porque tenho muito a fazer", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("hse_c_q4", "Eu sou incapaz de fazer uma pausa", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("hse_c_q5", "Eu tenho que trabalhar muito rápido", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("hse_c_q6", "Eu tenho tempo suficiente para fazer tudo", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q7", "Diferentes grupos no trabalho exigem coisas incompatíveis de mim", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("hse_c_q8", "Eu sei como fazer meu trabalho", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_hse[:8], 1):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''
        <h3 style="color: #2196f3; margin-top: 20px;">Domínio 2: Controle (6 questões)</h3>
'''

questoes_hse_controle = [
    ("hse_c_q9", "Eu posso decidir quando fazer uma pausa", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q10", "Eu tenho uma opinião sobre o trabalho que faço", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q11", "Eu tenho uma opinião sobre como faço meu trabalho", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q12", "Meu ritmo de trabalho pode ser flexível", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q13", "Eu posso decidir quando trabalhar", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q14", "Eu tenho alguma opinião sobre a ordem em que faço as coisas", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_hse_controle, 9):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''
        <h3 style="color: #2196f3; margin-top: 20px;">Domínio 3: Apoio (10 questões)</h3>
'''

questoes_hse_apoio = [
    ("hse_c_q15", "Se o trabalho ficar difícil, meus colegas me ajudam", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q16", "Eu recebo o respeito que mereço dos meus colegas", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q17", "Meus colegas estão dispostos a me ouvir sobre problemas relacionados ao trabalho", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q18", "Eu recebo ajuda e apoio do meu supervisor imediato", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q19", "Meu supervisor imediato me encoraja no trabalho", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q20", "Eu posso confiar no meu supervisor imediato para me ajudar com um problema de trabalho", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q21", "Eu recebo o respeito que mereço do meu supervisor imediato", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q22", "Meu supervisor imediato está disposto a me ouvir sobre problemas relacionados ao trabalho", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q23", "Eu sou apoiado em situações emocionalmente exigentes no trabalho", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("hse_c_q24", "Recursos e comunicação são adequados", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_hse_apoio, 15):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''
        <h3 style="color: #2196f3; margin-top: 20px;">Domínio 4: Relacionamentos (4 questões)</h3>
'''

questoes_hse_rel = [
    ("hse_c_q25", "Existe tensão ou raiva entre os colegas", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("hse_c_q26", "Eu sou pessoalmente assediado na forma de comentários ofensivos ou outros comportamentos", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("hse_c_q27", "Relacionamentos no trabalho são tensos", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("hse_c_q28", "Eu sou sujeito a bullying no trabalho", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_hse_rel, 25):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''
        <h3 style="color: #2196f3; margin-top: 20px;">Domínio 5: Papel (5 questões)</h3>
'''

opcoes_concordo = [(4,"Concordo totalmente"),(3,"Concordo"),(2,"Neutro"),(1,"Discordo"),(0,"Discordo totalmente")]
questoes_hse_papel = [
    ("hse_c_q29", "Está claro para mim quais são meus deveres e responsabilidades", opcoes_concordo),
    ("hse_c_q30", "Está claro o que se espera de mim no trabalho", opcoes_concordo),
    ("hse_c_q31", "Eu sei como fazer meu trabalho", opcoes_concordo),
    ("hse_c_q32", "Eu entendo como meu trabalho se encaixa nos objetivos gerais da organização", opcoes_concordo),
    ("hse_c_q33", "Eu recebo informações oportunas sobre mudanças organizacionais", opcoes_concordo),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_hse_papel, 29):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''
        <h3 style="color: #2196f3; margin-top: 20px;">Domínio 6: Mudança (2 questões)</h3>
'''

questoes_hse_mudanca = [
    ("hse_c_q34", "Quando mudanças são feitas no trabalho, fica claro como funcionarão na prática", opcoes_concordo),
    ("hse_c_q35", "Eu tenho oportunidade suficiente para questionar os gerentes sobre mudanças no trabalho", opcoes_concordo),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_hse_mudanca, 34):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''        <button class="btn" onclick="calcularResultados('hse-completa')">Calcular Resultados</button>
      </div>

'''

# ============= NIOSH RÁPIDA =============
novos_questionarios += '''      <!-- NIOSH WellBQ - Versão Rápida -->
      <div id="niosh-rapida" class="questionario card">
        <h2>🏥 NIOSH WellBQ - Triagem Rápida</h2>
        <p class="questionnaire-info">5 questões essenciais sobre bem-estar no trabalho baseadas no questionário oficial americano</p>
        
'''

questoes_niosh_rapida = [
    ("niosh_q1", "Nos últimos 7 dias, com que frequência você se sentiu feliz?", [(4,"Sempre"),(3,"Frequentemente"),(2,"Às vezes"),(1,"Raramente"),(0,"Nunca")]),
    ("niosh_q2", "Nos últimos 7 dias, com que frequência você se sentiu estressado?", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("niosh_q3", "Você está satisfeito com seu trabalho atual?", [(4,"Muito satisfeito"),(3,"Satisfeito"),(2,"Neutro"),(1,"Insatisfeito"),(0,"Muito insatisfeito")]),
    ("niosh_q4", "Você sente que seu trabalho é valorizado pela organização?", opcoes_concordo),
    ("niosh_q5", "Você consegue equilibrar bem sua vida pessoal e profissional?", opcoes_concordo),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_niosh_rapida, 1):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''        <button class="btn" onclick="calcularResultados('niosh-rapida')">Calcular Resultados</button>
      </div>

'''

# ============= NIOSH COMPLETA =============
novos_questionarios += '''      <!-- NIOSH WellBQ - Versão Completa -->
      <div id="niosh-completa" class="questionario card">
        <h2>🏥 NIOSH WellBQ - Avaliação Completa</h2>
        <p class="questionnaire-info">18 questões abrangentes sobre bem-estar no trabalho baseadas no questionário oficial americano</p>
        
        <h3 style="color: #2196f3; margin-top: 20px;">Bem-estar Emocional (6 questões)</h3>
'''

questoes_niosh_completa = [
    ("niosh_c_q1", "Nos últimos 7 dias, com que frequência você se sentiu feliz?", opcoes_freq),
    ("niosh_c_q2", "Nos últimos 7 dias, com que frequência você se sentiu estressado?", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("niosh_c_q3", "Nos últimos 7 dias, com que frequência você se sentiu ansioso?", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("niosh_c_q4", "Nos últimos 7 dias, com que frequência você se sentiu deprimido?", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("niosh_c_q5", "Nos últimos 7 dias, com que frequência você se sentiu satisfeito com sua vida?", opcoes_freq),
    ("niosh_c_q6", "Nos últimos 7 dias, com que frequência você se sentiu esgotado emocionalmente?", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_niosh_completa, 1):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''
        <h3 style="color: #2196f3; margin-top: 20px;">Satisfação no Trabalho (4 questões)</h3>
'''

questoes_niosh_satisfacao = [
    ("niosh_c_q7", "Você está satisfeito com seu trabalho atual?", [(4,"Muito satisfeito"),(3,"Satisfeito"),(2,"Neutro"),(1,"Insatisfeito"),(0,"Muito insatisfeito")]),
    ("niosh_c_q8", "Você sente que seu trabalho é valorizado pela organização?", opcoes_concordo),
    ("niosh_c_q9", "Você tem oportunidades de crescimento profissional?", opcoes_concordo),
    ("niosh_c_q10", "Você se sente realizado com seu trabalho?", opcoes_concordo),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_niosh_satisfacao, 7):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''
        <h3 style="color: #2196f3; margin-top: 20px;">Equilíbrio Vida-Trabalho (4 questões)</h3>
'''

questoes_niosh_equilibrio = [
    ("niosh_c_q11", "Você consegue equilibrar bem sua vida pessoal e profissional?", opcoes_concordo),
    ("niosh_c_q12", "Você tem tempo suficiente para atividades pessoais e familiares?", opcoes_concordo),
    ("niosh_c_q13", "Seu trabalho interfere negativamente em sua vida pessoal?", [(0,"Concordo totalmente"),(1,"Concordo"),(2,"Neutro"),(3,"Discordo"),(4,"Discordo totalmente")]),
    ("niosh_c_q14", "Você consegue desconectar do trabalho fora do horário de expediente?", opcoes_concordo),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_niosh_equilibrio, 11):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''
        <h3 style="color: #2196f3; margin-top: 20px;">Bem-estar Físico (4 questões)</h3>
'''

questoes_niosh_fisico = [
    ("niosh_c_q15", "Você se sente fisicamente saudável?", opcoes_concordo),
    ("niosh_c_q16", "Você dorme o suficiente para se sentir descansado?", opcoes_concordo),
    ("niosh_c_q17", "Você tem energia suficiente para realizar suas atividades diárias?", opcoes_concordo),
    ("niosh_c_q18", "Seu trabalho causa dores físicas ou desconforto?", [(0,"Concordo totalmente"),(1,"Concordo"),(2,"Neutro"),(3,"Discordo"),(4,"Discordo totalmente")]),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_niosh_fisico, 15):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''        <button class="btn" onclick="calcularResultados('niosh-completa')">Calcular Resultados</button>
      </div>

'''

# ============= NR RÁPIDA =============
novos_questionarios += '''      <!-- NR-01 e NR-17 - Versão Rápida -->
      <div id="nr-rapida" class="questionario card">
        <h2>📋 NR-01 e NR-17 - Triagem Rápida</h2>
        <p class="questionnaire-info">6 questões essenciais sobre gestão de riscos e ergonomia baseadas nas normas regulamentadoras brasileiras</p>
        
'''

questoes_nr_rapida = [
    ("nr_q1", "Você recebe treinamento adequado sobre os riscos do seu trabalho?", opcoes_freq),
    ("nr_q2", "Seu posto de trabalho é ergonomicamente adequado?", opcoes_concordo),
    ("nr_q3", "Você realiza pausas adequadas durante a jornada de trabalho?", opcoes_freq),
    ("nr_q4", "Você sente desconforto físico durante ou após o trabalho?", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("nr_q5", "A organização identifica e avalia os riscos psicossociais no trabalho?", opcoes_concordo),
    ("nr_q6", "Você participa de decisões sobre melhorias nas condições de trabalho?", opcoes_freq),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_nr_rapida, 1):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''        <button class="btn" onclick="calcularResultados('nr-rapida')">Calcular Resultados</button>
      </div>

'''

# ============= NR COMPLETA =============
novos_questionarios += '''      <!-- NR-01 e NR-17 - Versão Completa -->
      <div id="nr-completa" class="questionario card">
        <h2>📋 NR-01 e NR-17 - Avaliação Completa</h2>
        <p class="questionnaire-info">24 questões abrangentes sobre gestão de riscos e ergonomia baseadas nas normas regulamentadoras brasileiras</p>
        
        <h3 style="color: #2196f3; margin-top: 20px;">Gestão de Riscos Ocupacionais - NR-01 (12 questões)</h3>
'''

questoes_nr_completa_gestao = [
    ("nr_c_q1", "Você recebe treinamento adequado sobre os riscos do seu trabalho?", opcoes_freq),
    ("nr_c_q2", "A organização identifica e avalia os riscos psicossociais no trabalho?", opcoes_concordo),
    ("nr_c_q3", "Você participa de decisões sobre melhorias nas condições de trabalho?", opcoes_freq),
    ("nr_c_q4", "Existe um programa de gerenciamento de riscos implementado?", opcoes_concordo),
    ("nr_c_q5", "Você é informado sobre os resultados das avaliações de risco?", opcoes_freq),
    ("nr_c_q6", "Medidas de prevenção e controle de riscos são implementadas?", opcoes_freq),
    ("nr_c_q7", "Você tem acesso a equipamentos de proteção adequados?", opcoes_freq),
    ("nr_c_q8", "Existe um canal para relatar situações de risco?", opcoes_concordo),
    ("nr_c_q9", "A organização promove ações de saúde e segurança no trabalho?", opcoes_freq),
    ("nr_c_q10", "Você se sente seguro no seu ambiente de trabalho?", opcoes_concordo),
    ("nr_c_q11", "A organização realiza avaliações periódicas de riscos?", opcoes_freq),
    ("nr_c_q12", "Você recebe feedback sobre suas sugestões de melhoria?", opcoes_freq),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_nr_completa_gestao, 1):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''
        <h3 style="color: #2196f3; margin-top: 20px;">Ergonomia - NR-17 (12 questões)</h3>
'''

questoes_nr_completa_ergo = [
    ("nr_c_q13", "Seu posto de trabalho é ergonomicamente adequado?", opcoes_concordo),
    ("nr_c_q14", "Você realiza pausas adequadas durante a jornada de trabalho?", opcoes_freq),
    ("nr_c_q15", "Você sente desconforto físico durante ou após o trabalho?", [(0,"Sempre"),(1,"Frequentemente"),(2,"Às vezes"),(3,"Raramente"),(4,"Nunca")]),
    ("nr_c_q16", "Sua cadeira e mesa de trabalho são ajustáveis?", opcoes_concordo),
    ("nr_c_q17", "A iluminação do seu ambiente de trabalho é adequada?", opcoes_concordo),
    ("nr_c_q18", "O nível de ruído no ambiente é confortável?", opcoes_concordo),
    ("nr_c_q19", "A temperatura do ambiente é adequada?", opcoes_concordo),
    ("nr_c_q20", "Você tem espaço suficiente para realizar suas atividades?", opcoes_concordo),
    ("nr_c_q21", "Os equipamentos e ferramentas são ergonômicos?", opcoes_concordo),
    ("nr_c_q22", "Você recebe orientação sobre postura correta no trabalho?", opcoes_freq),
    ("nr_c_q23", "A organização realiza análise ergonômica do trabalho?", opcoes_concordo),
    ("nr_c_q24", "Você pode ajustar seu ritmo de trabalho conforme necessário?", opcoes_freq),
]

for i, (campo, titulo, opcoes) in enumerate(questoes_nr_completa_ergo, 13):
    novos_questionarios += criar_questao_radio(i, campo, titulo, opcoes)

novos_questionarios += '''        <button class="btn" onclick="calcularResultados('nr-completa')">Calcular Resultados</button>
      </div>

'''

# Juntar tudo
novo_content = parts[0] + novos_questionarios + insert_marker + parts[1]

# Salvar
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(novo_content)

print("✅ Todos os 6 questionários faltantes foram adicionados com sucesso!")
print("   - copsoq-completa (20 questões)")
print("   - hse-completa (35 questões)")
print("   - niosh-rapida (5 questões)")
print("   - niosh-completa (18 questões)")
print("   - nr-rapida (6 questões)")
print("   - nr-completa (24 questões)")
