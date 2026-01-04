# Problema Identificado: Falta Botão de Calcular

## Situação
- ✅ Questionário exibido corretamente
- ✅ Todas as 5 questões respondidas
- ✅ Barra de progresso funcionando
- ❌ **Botão "Calcular Resultados" não está presente no questionário COPSOQ**

## Causa
Ao revisar o código adicionado, percebi que adicionei o botão apenas para o questionário HSE:
```html
<button class="btn" onclick="calcularResultados('hse-rapida')">Calcular Resultados</button>
```

Mas **NÃO adicionei** o botão para o questionário COPSOQ.

## Solução
Preciso adicionar o botão "Calcular Resultados" no final do questionário COPSOQ (copsoq-rapida).
