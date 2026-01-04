// Teste automatizado de todas as metodologias
async function testarTodas() {
  const testes = [
    { metodo: 'copsoq', versao: 'rapida', questoes: ['copsoq_q1', 'copsoq_q2', 'copsoq_q3', 'copsoq_q4', 'copsoq_q5'], id: 'copsoq-rapida' },
    { metodo: 'hse', versao: 'rapida', questoes: ['hse_q1', 'hse_q2', 'hse_q3', 'hse_q4', 'hse_q5', 'hse_q6'], id: 'hse-rapida' },
    { metodo: 'hse', versao: 'completa', questoes: Array.from({length: 35}, (_, i) => `hse_c_q${i+1}`), id: 'hse-completa' },
    { metodo: 'niosh', versao: 'rapida', questoes: ['niosh_q1', 'niosh_q2', 'niosh_q3', 'niosh_q4', 'niosh_q5'], id: 'niosh-rapida' },
    { metodo: 'niosh', versao: 'completa', questoes: Array.from({length: 18}, (_, i) => `niosh_c_q${i+1}`), id: 'niosh-completa' },
    { metodo: 'nr', versao: 'rapida', questoes: ['nr_q1', 'nr_q2', 'nr_q3', 'nr_q4', 'nr_q5', 'nr_q6'], id: 'nr-rapida' },
    { metodo: 'nr', versao: 'completa', questoes: Array.from({length: 24}, (_, i) => `nr_c_q${i+1}`), id: 'nr-completa' }
  ];
  
  const resultados = [];
  
  for (const teste of testes) {
    try {
      // Resetar
      location.reload();
      await new Promise(r => setTimeout(r, 500));
      
      // Selecionar metodologia
      document.getElementById('metodologia').value = teste.metodo;
      mostrarQuestionario();
      await new Promise(r => setTimeout(r, 300));
      
      // Selecionar versão
      const versaoRadio = document.querySelector(`input[name="versao"][value="${teste.versao}"]`);
      if (versaoRadio) versaoRadio.click();
      await new Promise(r => setTimeout(r, 300));
      
      // Verificar se questionário apareceu
      const questionario = document.getElementById(teste.id);
      const visivel = questionario && questionario.offsetParent !== null;
      
      if (!visivel) {
        resultados.push({ id: teste.id, status: '❌ ERRO', mensagem: 'Questionário não apareceu' });
        continue;
      }
      
      // Responder questões
      teste.questoes.forEach(q => {
        const radio = document.querySelector(`input[name="${q}"][value="4"]`);
        if (radio) radio.checked = true;
      });
      
      // Calcular
      calcularResultados(teste.id);
      await new Promise(r => setTimeout(r, 500));
      
      // Verificar dashboard
      const dashboard = document.getElementById('dashboard');
      const dashboardVisivel = dashboard && dashboard.offsetParent !== null;
      
      resultados.push({
        id: teste.id,
        status: dashboardVisivel ? '✅ OK' : '⚠️ Dashboard não apareceu',
        questoes: teste.questoes.length
      });
      
    } catch (erro) {
      resultados.push({ id: teste.id, status: '❌ ERRO', mensagem: erro.message });
    }
  }
  
  console.table(resultados);
  return resultados;
}

console.log('Script carregado. Execute: testarTodas()');
