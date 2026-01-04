// Script de teste para todas as metodologias e versões

const testes = [
  { metodologia: 'copsoq', versao: 'rapida', questoes: 5 },
  { metodologia: 'copsoq', versao: 'completa', questoes: 20 },
  { metodologia: 'hse', versao: 'rapida', questoes: 6 },
  { metodologia: 'hse', versao: 'completa', questoes: 35 },
  { metodologia: 'niosh', versao: 'rapida', questoes: 5 },
  { metodologia: 'niosh', versao: 'completa', questoes: 18 },
  { metodologia: 'nr', versao: 'rapida', questoes: 6 },
  { metodologia: 'nr', versao: 'completa', questoes: 24 }
];

const resultados = [];

for (const teste of testes) {
  const id = `${teste.metodologia}-${teste.versao}`;
  const elemento = document.getElementById(id);
  
  if (!elemento) {
    resultados.push({
      id: id,
      status: '❌ ERRO',
      mensagem: 'Elemento não encontrado'
    });
    continue;
  }
  
  // Verificar se o elemento está visível
  const isVisible = elemento.offsetParent !== null;
  
  // Contar questões (radio buttons)
  const inputs = elemento.querySelectorAll('input[type="radio"]');
  const grupos = new Set();
  inputs.forEach(input => grupos.add(input.name));
  const numQuestoes = grupos.size;
  
  // Verificar botão de calcular
  const botao = elemento.querySelector('button[onclick*="calcularResultados"]');
  const temBotao = botao !== null;
  
  // Status
  const questoesOk = numQuestoes === teste.questoes;
  const status = questoesOk && temBotao ? '✅ OK' : '⚠️ PROBLEMA';
  
  resultados.push({
    id: id,
    status: status,
    questoesEsperadas: teste.questoes,
    questoesEncontradas: numQuestoes,
    temBotao: temBotao,
    visivel: isVisible
  });
}

console.table(resultados);
resultados;
